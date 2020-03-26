#! /usr/bin/env bash

curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=${WECHAT_QY_BOT_KEY}' \
   -H 'Content-Type: application/json' \
   -d '
   {
        "msgtype": "text",
        "text": {
            "content": "hello world"
        }
   }'