# -*- coding: utf-8 -*-

name_map = {
    "ACFUN_ACCOUNT_LIST": "ACFUN",
    "BILIBILI_COOKIE_LIST": "BILIBILI",
    "CSDN_COOKIE_LIST": "CSDN",
    "MUSIC163_ACCOUNT_LIST": "MUSIC163",
    "PICACOMIC_ACCOUNT_LIST": "PICACOMIC",
    "TIEBA_COOKIE_LIST": "TIEBA",
    "V2EX_COOKIE_LIST": "V2EX",
    "YAMIBO_COOKIE_LIST": "YAMIBO",
    "FFXIV_ACCOUNT_LIST": "FFXIV"
}

change_key_map = {
    "ACFUN_ACCOUNT_LIST": {"acfun_password": "password", "acfun_phone": "phone"},
    "BILIBILI_COOKIE_LIST": {
        "bilibili_cookie": "cookie",
        "coin_num": "coin_num",
        "coin_type": "coin_type",
        "silver2coin": "silver2coin",
    },
    "CSDN_COOKIE_LIST": {"csdn_cookie": "cookie"},
    "MUSIC163_ACCOUNT_LIST": {"music163_password": "password", "music163_phone": "phone"},
    "PICACOMIC_ACCOUNT_LIST": {"picacomic_email": "email", "picacomic_password": "password"},
    "TIEBA_COOKIE_LIST": {"tieba_cookie": "cookie"},
    "V2EX_COOKIE_LIST": {"v2ex_cookie": "cookie", "v2ex_proxy": "proxy"},
    "YAMIBO_COOKIE_LIST": {"yamibo_cookie": "cookie"},
    "FFXIV_ACCOUNT_LIST": {"ffxiv_username": "username", "ffxiv_password": "password", "area_name": "area_name",
                           "server_name": "server_name", "role_name": "role_name"}
}


def format_data(data):
    flag = False
    new_data = {}
    for key, value in data.items():
        if name_map.get(key):
            flag = True
            if isinstance(value, list):
                for one in value:
                    if isinstance(one, dict):
                        if name_map.get(key) not in new_data.keys():
                            new_data[name_map.get(key)] = []
                        for k2, v2 in change_key_map[key].items():
                            try:
                                one[v2] = one.pop(k2)
                            except Exception as e:
                                print(e)
                        new_data[name_map.get(key)].append(one)
            if not new_data.get(name_map.get(key)):
                new_data[name_map.get(key)] = value
        else:
            new_data[key] = value
    return flag, new_data
