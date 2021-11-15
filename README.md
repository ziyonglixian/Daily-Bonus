## 说明

基于 [Sitoi/dailycheckin](https://github.com/Sitoi/dailycheckin) 修改的签到工具：
1. 删除无用的推送消息
2. 统一签到消息格式
3. 取消 Bilibili 观看任务、分享任务（避免影响历史记录）
4. 添加百合会签到
5. 添加最终幻想14积分签到
   - 薛定谔の自动签到：经常遇到验证码，偶尔能签上🙊

|任务名称|名称|备注|
|---|---|---|
|ACFUN|[AcFun](https://www.acfun.cn/)|香蕉|
|BILIBILI|[Bilibili](https://www.bilibili.com)|漫画/直播签到，投币，银瓜子换硬币|
|CSDN|[CSDN](https://www.csdn.net/)|签到金，抽奖|
|MUSIC163|[网易云音乐](https://music.163.com/)|云贝，刷歌|
|PICACOMIC|[哔咔漫画](https://www.picacomic.com)|成长值|
|TIEBA|[百度贴吧](https://tieba.baidu.com/index.html)|经验值|
|V2EX|[V2EX](https://www.v2ex.com/)|铜币|
|YAMIBO|[百合会论坛](https://bbs.yamibo.com/forum.php)|对象|
|FFXIV|[艾欧泽亚积分兑换平台](https://actff1.web.sdo.com/20180707Jifen/index.html#/home)|积分|

### 推送配置

|Name|归属|属性|说明|
|---|---|---|---|
|_**DINGTALK_SECRET**_|钉钉|推送|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选|
|_**DINGTALK_ACCESS_TOKEN**_|钉钉|推送|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`|
|_**SCKEY**_|server 酱|推送|server 酱推送[官方文档](https://sc.ftqq.com/3.version) ,填写 `SCKEY` 代码即可|
|_**SENDKEY**_|server 酱 TURBO|推送|server 酱 TURBO 推送[官方文档](https://sct.ftqq.com/sendkey) ,填写 `SENDKEY` 代码即可|
|_**BARK_URL**_|BARK|推送|BARK 推送[使用](https://github.com/Sitoi/dailycheckin/issues/29) ,填写 `BARK_URL` 即可，例如: `https://api.day.app/DxHcxxxxxRxxxxxxcm/` |
|_**QMSG_KEY**_|qmsg 酱|推送|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,填写 `KEY` 代码即可|
|_**QMSG_TYPE**_|qmsg 酱|推送|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,如果需要推送到群填写 `group`,其他的都推送到 QQ |
|_**TG_BOT_TOKEN**_|telegram|推送|telegram 推送 `TG_BOT_TOKEN`|
|_**TG_USER_ID**_|telegram|推送|telegram 推送 `TG_USER_ID`，[How can I send a message to someone with my telegram bot using their Username](https://stackoverflow.com/questions/41664810/how-can-i-send-a-message-to-someone-with-my-telegram-bot-using-their-username)|
|_**TG_API_HOST**_|telegram|推送|Telegram api 自建的反向代理地址，例子：反向代理地址 http://aaa.bbb.ccc 则填写 aaa.bbb.ccc [简略搭建教程](https://shimo.im/docs/JD38CJDQtYy3yTd8/read)  |
|_**TG_PROXY**_|telegram|推送|Telegram 代理的信息，无密码例子: http://127.0.0.1:1080 有密码例子: http://username:password@127.0.0.1:1080|
|_**COOLPUSHSKEY**_|Cool Push|推送|[Cool Push](https://cp.xuthus.cc/) 推送的 `SKEY`|
|_**COOLPUSHQQ**_|Cool Push|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 QQ 推送，默认开启|
|_**COOLPUSHWX**_|Cool Push|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 微信 推送，默认关闭|
|_**COOLPUSHEMAIL**_|Cool Push|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 邮件 推送，默认关闭|
|_**QYWX_KEY**_|企业微信群机器人|推送|密钥，企业微信推送 `webhook` 后面的 `key` 详见[官方说明文档](https://work.weixin.qq.com/api/doc/90000/90136/91770) |
|_**QYWX_CORPID**_|企业微信应用消息|推送|corpid |
|_**QYWX_AGENTID**_|企业微信应用消息|推送|agentid  |
|_**QYWX_CORPSECRET**_|企业微信应用消息|推送|corpsecret |
|_**QYWX_TOUSER**_|企业微信应用消息|推送|touser |
|_**QYWX_MEDIA_ID**_|企业微信应用消息|推送|media_id [参考文档1](https://note.youdao.com/ynoteshare1/index.html?id=351e08a72378206f9dd64d2281e9b83b&type=note)  [参考文档2](https://note.youdao.com/ynoteshare1/index.html?id=1a0c8aff284ad28cbd011b29b3ad0191&type=note) |
|_**PUSHPLUS_TOKEN**_|pushplus|推送|用户令牌，可直接加到请求地址后，如：`http://www.pushplus.plus/send/{token}` [官方文档](https://www.pushplus.plus/doc/)|
|_**PUSHPLUS_TOPIC**_|pushplus|推送|群组编码，不填仅发送给自己 [官方文档](https://www.pushplus.plus/doc/)|
|_**FSKEY**_|飞书|推送|`https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxx` **xxxxxx** 部分就是需要填写的 FSKEY [自定义机器人指南](https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN)|
|_**MERGE_PUSH**_|合并推送|配置|true: 将推送消息合并；false: 分开推送|

### Web 签到配置

|Name|归属|属性|说明|
|---|---|---|---|
|_**BILIBILI**_.coin_num|[Bilibili](https://www.bilibili.com)|Web|Bilibili 每日投币数量|
|_**BILIBILI**_.coin_type|[Bilibili](https://www.bilibili.com)|Web|Bilibili 投币方式（默认为 0）1: 为关注用户列表视频投币 0: 为随机投币。如果关注用户发布的视频不足配置的投币数，则剩余部分使用随机投币|
|_**BILIBILI**_.silver2coin|[Bilibili](https://www.bilibili.com)|Web|Bilibili 是否开启银瓜子换硬币，默认为 True 开启|
|_**BILIBILI**_.cookie|[Bilibili](https://www.bilibili.com)|Web|Bilibili cookie|
|_**CSDN**_.cookie|[CSDN](https://www.csdn.net/)|Web|CSDN cookie|
|_**MUSIC163**_.phone|[网易云音乐](https://music.163.com/)|账号|网易云音乐 手机账号|
|_**MUSIC163**_.password|[网易云音乐](https://music.163.com/)|账号|网易云音乐 密码|
|_**TIEBA**_.cookie|[百度贴吧](https://tieba.baidu.com/index.html)|Web|百度贴吧 cookie|
|_**V2EX**_.proxy|[V2EX](https://www.v2ex.com/)|Web|V2EX 代理的信息，无密码例子: http://127.0.0.1:1080 有密码例子: http://username:password@127.0.0.1:1080|
|_**V2EX**_.cookie|[V2EX](https://www.v2ex.com/)|Web|V2EX cookie|
|_**YAMIBO**_.cookie|[百合会](https://bbs.yamibo.com/forum.php)|Web|百合会 cookie|
|_**FFXIV**_.username|[艾欧泽亚积分兑换平台](https://actff1.web.sdo.com/20180707Jifen/index.html#/home)|Web|最终幻想14 账号|
|_**FFXIV**_.password|[艾欧泽亚积分兑换平台](https://actff1.web.sdo.com/20180707Jifen/index.html#/home)|Web|最终幻想14 密码|
|_**FFXIV**_.area_name|[艾欧泽亚积分兑换平台](https://actff1.web.sdo.com/20180707Jifen/index.html#/home)|Web|最终幻想14 大区名|
|_**FFXIV**_.server_name|[艾欧泽亚积分兑换平台](https://actff1.web.sdo.com/20180707Jifen/index.html#/home)|Web|最终幻想14 服务器名|
|_**FFXIV**_.role_name|[艾欧泽亚积分兑换平台](https://actff1.web.sdo.com/20180707Jifen/index.html#/home)|Web|最终幻想14 角色名|


### APP 签到配置

|Name|归属|属性|说明|
|---|---|---|:---|
|_**ACFUN**_.phone|[AcFun](https://www.acfun.cn/)|APP|AcFun 手机账号|
|_**ACFUN**_.password|[AcFun](https://www.acfun.cn/)|APP|AcFun 密码|
|_**PICACOMIC**_.email|[哔咔漫画](https://www.picacomic.com)|APP| 哔咔漫画 账号|
|_**PICACOMIC**_.password|[哔咔漫画](https://www.picacomic.com)|APP| 哔咔漫画 密码|

### TG API 反向代理脚本

```js
const whitelist = ["/bot"];
const tg_host = "api.telegram.org";
addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request)) 
})

function validate(path) { 
    for (var i = 0; i < whitelist.length; i++) { 
        if (path.startsWith(whitelist[i])) 
            return true; 
    } 
    return false; 
} 

async function handleRequest(request) { 
    var u = new URL(request.url); 
    u.host = tg_host; 
    if (!validate(u.pathname)) 
        return new Response('Unauthorized', { 
            status: 403 
        }); 
    var req = new Request(u, {
        method: request.method, 
        headers: request.headers, 
        body: request.body 
    }); 
    const result = await fetch(req); 
    return result; 
}
```

## 腾讯云函数部署

详见 [腾讯云函数教程](https://sitoi.gitee.io/dailycheckin/tencent-scf/)，注意安装依赖包时使用以下语句：

```bash
pip3 install git+git://github.com/jckling/Daily-Bonus@dev --upgrade -t .
```

## 示例配置（单账户）

多账户配置参考[dailycheckin 示例](https://sitoi.github.io/dailycheckin/settings/#_9)，注意：
1. 自建 TG 反向代理配置 `TG_API_HOST` 即可；否则配置代理 `TG_PROXY`
   - 遇到超时问题，可以用 [飞书](https://www.feishu.cn/) 或 [Server 酱](https://sct.ftqq.com/) 替代，其他推送没用过
2. 若 cookie 中包含 `"` 则需要用进行转义（`\"`）
3. V2EX 必须配置代理 `proxy`

```json
{
  "FSKEY": "",
  "TG_BOT_TOKEN": "",
  "TG_USER_ID": "",
  "TG_API_HOST": "",
  "ACFUN": [
    {
      "phone": "",
      "password": ""
    }
  ],
  "BILIBILI": [
    {
      "coin_num": 0,
      "coin_type": 1,
      "silver2coin": false,
      "cookie": ""
    }
  ],
  "CSDN": [
    {
      "cookie": ""
    }
  ],
  "MUSIC163": [
    {
      "phone": "",
      "password": ""
    }
  ],
  "PICACOMIC": [
    {
      "email": "",
      "password": ""
    }
  ],
  "TIEBA": [
    {
      "cookie": ""
    }
  ],
  "V2EX": [
    {
      "proxy": "",
      "cookie": ""
    }
  ],
  "YAMIBO": [
    {
      "cookie": ""
    }
  ],
  "FFXIV": [
    {
      "username": "",
      "password": "",
      "area_name": "陆行鸟",
      "server_name": "",
      "role_name": ""
    }
  ]
}
```