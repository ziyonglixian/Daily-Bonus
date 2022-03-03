# -*- coding: utf-8 -*-
# @File     : main.py
# @Time     : 2021/10/18 19:49
# @Author   : Jckling

import json
import os
import time

import requests
from dailycheckin import CheckIn


class Ffxiv(CheckIn):
    name = "最终幻想14"

    def __init__(self, check_item: dict):
        self.check_item = check_item
        self.cookies = {}

    # 登录
    def login(self):
        username = self.check_item.get("username")
        password = self.check_item.get("password")
        headers = {
            "Host": "cas.sdo.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "script",
            "Referer": "https://login.u.sdo.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,da;q=0.5",
            "Cookie": "CASCID=CIDF4FE36AE09944418AEBD8394F75B8ED3; hasAdsr=1",
        }

        params = {
            "_": int(round(time.time() * 1000)),
            "appId": "100001900",
            "areaId": "1",
            "authenSource": "2",
            "autoLoginFlag": "0",
            "callback": "staticLogin_JSONPMethod",
            # "customSecurityLevel": "2",
            "frameType": "3",
            "inputUserId": username,
            # "isEncrypt": "1",
            "locale": "zh_CN",
            "password": password,
            "productId": "2",
            "productVersion": "v5",
            "scene": "login",
            "serviceUrl": "https://actff1.web.sdo.com/20180707jifen/Server/SDOLogin.ashx?returnPage=index.html",
            "tag": "20",
            "usage": "aliCode",
            "version": "21",
        }

        url = "https://cas.sdo.com/authen/staticLogin.jsonp"
        r = requests.get(url, headers=headers, params=params)
        self.set_cookies(r.cookies.items())

        # 获取 ticket 字段
        text = r.text
        text = text[text.find("(") + 1: text.rfind(")")]
        obj = json.loads(text)
        msg = [{"name": "账号信息", "value": username}]
        if "ticket" in obj["data"]:
            msg += [{"name": "登录信息", "value": "登录成功"}]
            return obj["data"]["ticket"], msg
        elif "captchaParams" in obj["data"]:
            msg += [{"name": "登录信息", "value": "要求通过验证码"}]
        else:
            msg += [{"name": "登录信息", "value": f'登录失败，{obj["data"]["failReason"]}'}]
        return "", msg

    # 设置 cookies
    def set_cookies(self, items):
        for i in items:
            self.cookies.setdefault(i[0], i[1])

    # 获取 cookies
    def get_cookies(self, ticket):
        params = {
            "_": "1617715671699",
            "appId": "100001900",
            "areaId": "1",
            "authenSource": "2",
            "callback": "getPromotionInfo_JSONPMethod",
            "frameType": "3",
            "locale": "zh_CN",
            "productId": "2",
            "productVersion": "v5",
            "scene": "login",
            "serviceUrl": "https://actff1.web.sdo.com/20180707jifen/Server/SDOLogin.ashx?returnPage=index.html",
            "tag": "20",
            "usage": "aliCode",
            "version": "21",
            "customSecurityLevel": "2",
        }

        url = "https://cas.sdo.com/authen/getPromotionInfo.jsonp"
        r = requests.get(url, params=params, cookies=self.cookies)
        self.set_cookies(r.cookies.items())

    # 认证
    def auth(self, ticket):
        params = {
            "returnPage": "index.html",
            "ticket": ticket,
        }

        url = "https://actff1.web.sdo.com//20180707jifen/Server/SDOLogin.ashx"
        r = requests.get(url, params=params, cookies=self.cookies)
        self.set_cookies(r.cookies.items())

    # 选择角色
    def select_role(self):
        server_name = self.check_item.get("server_name")
        area_name = self.check_item.get("area_name")
        role_name = self.check_item.get("role_name")
        if area_name == "陆行鸟":
            ipid = "1"
        elif area_name == "莫古力":
            ipid = "6"
        elif area_name == "猫小胖":
            ipid = "7"
        elif area_name == "豆豆柴":
            ipid = "8"

        params = {
            "method": "queryff14rolelist",
            "ipid": ipid,
            "i": "0.6531217873613295",
        }

        url = "http://act.ff.sdo.com/20180707jifen/Server/ff14/HGetRoleList.ashx"
        r = requests.get(url, params=params, cookies=self.cookies)

        # 获取角色 id
        obj = r.json()
        attach = obj["Attach"]
        role = "{0}|{1}|{2}"
        for r in attach:
            if r["worldnameZh"] == server_name and r["name"] == role_name:
                role = role.format(r["cicuid"], r["worldname"], r["groupid"])
                break

        # 选择角色
        areaid = ipid
        params = {
            "method": "setff14role",
            "AreaId": areaid,
            "AreaName": area_name,
            "RoleName": "[%s]%s" % (server_name, role_name),
            "Role": role,
            "i": "0.16795254979041618",
        }

        r = requests.post(url, params=params, cookies=self.cookies)
        obj = r.json()
        if obj["Success"]:
            return [{"name": "角色信息", "value": f"{area_name}-{server_name}-{role_name}"}]
        else:
            return [{"name": "角色信息", "value": f'角色选择失败，{obj["Message"]}'}]

    # 签到
    def check_in(self):
        params = {
            "method": "signin",
            "i": "0.8613162421160268"
        }

        url = "http://act.ff.sdo.com/20180707jifen/Server/User.ashx"
        r = requests.post(url, params=params, cookies=self.cookies)

        obj = r.json()
        if obj["Success"]:
            return [{"name": "签到信息", "value": "签到成功"}]
        else:
            return [{"name": "签到信息", "value": f'签到失败，{obj["Message"]}'}]

    # 查询积分
    def query_points(self):
        params = {
            "method": "querymystatus",
            "i": "0.6792009762893907"
        }

        url = "http://act.ff.sdo.com/20180707jifen/Server/User.ashx"
        r = requests.post(url, params=params, cookies=self.cookies)

        obj = r.json()
        points = json.loads(obj["Attach"])["Jifen"]
        return [{"name": "积分信息", "value": f"当前积分为: {points}"}]

    def main(self):
        ticket, msg = self.login()
        if ticket != "":
            self.get_cookies(ticket)
            self.auth(ticket)
            msg += self.select_role()
            msg += self.check_in()
            msg += self.query_points()

        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _check_item = datas.get("FFXIV", [])[0]
    print(FF14(check_item=_check_item).main())
