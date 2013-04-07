#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");
u"""
微信server 进程
简单处理微信api调用
使用tornado来做server端
微信需要80端口可以配置nginx
"""

import tornado.ioloop
import tornado.web
from weixinxml import reply_text_user
from translate import translate
import xmltodict
translate = translate()


class MainHandler(tornado.web.RequestHandler):
    u"""
    tornado的webserver
    """
    def get(self):
        u"""
        获取微信认证信息
        """
        echo = self.get_argument('echostr')
        print echo
        print self
        self.write(echo)

    def post(self):
        u"""
        微信post调用接口
        查询google翻译后返回结果
        """
        recv = xmltodict.parse(self.request.body)['xml']
        hellotext = u"""欢迎关注en2zh机器人,
                        en2zh是一个自动翻译的机器人,
                        你输入的任何英文en2zh将会为你翻译成中文"""
        try:
            if recv.get('Event') == 'subscribe':
                text_reply = reply_text_user(recv['ToUserName'],
                                             recv['FromUserName'],
                                             recv['CreateTime'],
                                             'text',
                                             hellotext)

            else:
                text = recv['Content'].strip()
                en2zh = translate.en2zh(text)
                text_reply = reply_text_user(recv['ToUserName'],
                                             recv['FromUserName'],
                                             recv['CreateTime'],
                                             'text',
                                             en2zh)
        except:
            text_reply = reply_text_user(recv['ToUserName'],
                                         recv['FromUserName'],
                                         recv['CreateTime'],
                                         'text',
                                         hellotext)
        self.write(text_reply)
        return


def run(host='127.0.0.1', port=8889):
    u"""
    args:
        host: server ip can be 127.0.0.1 0.0.0.0
        port: server post
    """
    application = tornado.web.Application([
        (r"/en2zh/", MainHandler),
    ])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
