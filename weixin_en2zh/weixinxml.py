#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reply_text_user(FromUserName,
                    ToUserName,
                    CreateTime,
                    MsgType,
                    Content):
    u"""
    文字回复

    : Parameters
        `FromUserName` : str
            发送者id
        `ToUserNam` : str
            发送给
        `CreateTime` : str
            创建时间
        `MsgType` : str
            消息类型
        `Content` : str
            消息正文
    """
    xml = u"""
           <xml>
 <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
 <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
 <CreateTime>{CreateTime}</CreateTime>
 <MsgType><![CDATA[{MsgType}]]></MsgType>
 <Content><![CDATA[{Content}]]></Content>
 <FuncFlag>0</FuncFlag>
 </xml>
           """
    xml = xml.format(FromUserName=FromUserName,
                     ToUserName=ToUserName,
                     CreateTime=CreateTime,
                     MsgType=MsgType,
                     Content=Content)
    return xml.replace('\n', '').strip()


def reply_html_user(**args):
    u"""
    html形式回复微信调用

    : Parameters

        `args` : kwargs
            kwargs

            * ToUserName
            * FromUserName
            * CreateTime
            * news
            * Content
            * items_args

    """
    args['ArticleCount'] = len(args['items_args'])
    xml = u"""
<xml>
 <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
 <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
 <CreateTime>{CreateTime}</CreateTime>
 <MsgType><![CDATA[news]]></MsgType>
 <Content><![CDATA[{Content}]]></Content>
 <ArticleCount>{ArticleCount}</ArticleCount>
 <Articles>
 {items}
 </Articles>
 <FuncFlag>1</FuncFlag>
 </xml>
"""
    item = u"""<item>
 <Title><![CDATA[{Title}]]></Title>
 <Description><![CDATA[{Description}]]></Description>
 <PicUrl><![CDATA[{Picurl}]]></PicUrl>
 <Url><![CDATA[{Url}]]></Url>
 </item>"""
    items = ''.join([item.format(**i).replace('\n', '\n').strip()
                     for i in args['items_args']])
    xml = xml.format(items=items, **args)
    return xml.replace('\n', '\n').strip()

if __name__ == "__main__":
    print reply_text_user('ssdd', '1312', '12312312', '312312', '131231')
    kwargs = {'ToUserName': 'dwdwdwedw',
              'FromUserName': 'sdasfsafas',
              'CreateTime': '231312312',
              'ArticleCount': u'中国测试',
              'items_args': []}
    print reply_html_user(**kwargs)
