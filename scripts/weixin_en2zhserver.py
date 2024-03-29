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

from weixin_en2zh.weixin import run
import os
import sys
print os.getcwd()
DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
NAME_FILE = os.path.relpath(__file__)


def main():
    import argparse
    usage = u"启动微信服务"
    p = argparse.ArgumentParser(description=usage)
    p.add_argument('-H', '--host', type=str,
                   default='127.0.0.1',
                   help=u"weixin host")
    p.add_argument('-P', '--port', type=int,
                   default=8889,
                   help=u"server port")
    args = p.parse_args()
    print "run server at{host}:{port}".format(host=args.host, port=args.port)
    run(args.host, args.port)

if __name__ == "__main__":
    main()
