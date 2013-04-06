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
import urllib,urllib2
from pyquery import PyQuery as Q
u"""
google翻译的简单实现
为验证是否非限制调用次数
"""


class translate(object):
    u"""
    处理翻译请求
    调用google translate翻译
    
    """

    def __init__(self):
        self.url='http://translate.google.cn/translate_t'
       
    def translate(self,lin,lout,text):
        u"""
        :Parameters

            `lin`: str
                传入的字符串的语言类型
            `lout`: str
                需要翻译成的字符串的类型
            `text`: str
                需要转换的文本
        """
        values={'hl':'zh-CN','ie':'UTF-8','text':text,'langpair':"%s|%s" % (lin, lout)}
        data = urllib.urlencode(values)
        req = urllib2.Request(self.url, data)
        req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
        response = urllib2.urlopen(req)
        text = response.read()
        rst = Q(text)('#result_box').text()
        return rst

    def en2zh(self,text):
        u"""
        英文翻译成中文
        """
        return self.translate('en','zh-CN',text)

    def zh2en(self,text):
        u"""
        中文翻译成英文
        """
        return self.translate('zh-CN','en',text)


if __name__ == "__main__":
    a = translate()
    print a.en2zh('hello')
    print a.zh2en('你好')
