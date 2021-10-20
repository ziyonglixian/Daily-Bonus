# -*- coding: utf-8 -*-
# @File     : main.py
# @Time     : 2021/10/12 15:18
# @Author   : Jckling

import json
import os

import requests
from bs4 import BeautifulSoup
from dailycheckin import CheckIn
from lxml import html


class Yamibo(CheckIn):
    name = "百合会"

    def __init__(self, check_item: dict):
        self.check_item = check_item

    @staticmethod
    def fhash(session):
        url = "https://bbs.yamibo.com/forum.php"
        r = session.get(url)
        tree = html.fromstring(r.text)
        hash = tree.xpath('//input[@name="formhash"]')[0].attrib['value']
        return hash

    @staticmethod
    def sign(session, hash):
        url = "https://bbs.yamibo.com/plugin.php?id=study_daily_attendance:daily_attendance&fhash=" + hash
        r = session.get(url)
        tree = html.fromstring(r.text)
        if "签到成功" in r.text or "已签到" in r.text:
            msg = [
                {"name": "账户信息", "value": tree.xpath('//ul[@id="mycp1_menu"]/a/text()')[0]},
                {"name": "签到信息", "value": tree.xpath('//div[@id="messagetext"]/p/text()')[0]}
            ]
        elif "登录" in r.text:
            msg = [
                {"name": "签到信息", "value": "登录失败，Cookie 可能已经失效"},
            ]
            return msg
        else:
            msg = [
                {"name": "账户信息", "value": "未知错误"},
            ]
        return msg

    @staticmethod
    def credit(session, msg):
        url = "https://bbs.yamibo.com/home.php?mod=spacecp&ac=credit&op=base"
        r = session.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        tree = html.fromstring(str(soup))
        credit = tree.xpath('//ul[@class="creditl mtm bbda cl"]/li/text()')
        data = [i.strip() for i in credit]
        msg += [
            {"name": "对象", "value": data[0]},
            {"name": "积分", "value": data[1]},
            {"name": "总积分", "value": data[2]},
            {"name": "规则", "value": "总积分 = 积分 + 对象/3"},
        ]
        return msg

    def main(self):
        cookie = {item.split("=")[0]: item.split("=")[1] for item in self.check_item.get("cookie").split("; ")}
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies, cookie)
        session.headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,da;q=0.5",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
                "Referer": "https://bbs.yamibo.com/forum.php",
                "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                "sec-ch-ua-mobile": "?0",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "Connection": "keep-alive",
                "Host": "bbs.yamibo.com",
            }
        )

        checkin_msg = self.sign(session, self.fhash(session))
        msg = self.credit(session, checkin_msg)
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _check_item = datas.get("YAMIBO", [])[0]
    print(Yamibo(check_item=_check_item).main())
