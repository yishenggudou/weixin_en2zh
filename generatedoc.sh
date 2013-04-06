#!/bin/bash
#Author: timger <yishenggudou@gmail.com>
#weibo <http://t.sina.com/zhanghaibo>
#@yishenggudou http://twitter.com/yishenggudou
module_dir=$1
sphinx_workplace="sphinxdoc"
sphinx-apidoc -o $sphinx_workplace -H $module_dir $module_dir
sphinx-build $sphinx_workplace doc
