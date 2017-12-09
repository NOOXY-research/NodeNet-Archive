# nodenet/interface/consoles/commons.py
# Description:
# "commons.py" provide commons console function that can be use widely.
# Copyright 2018 NOOXY. All Rights Reserved.

from nodenet.imports.commons import *
import nodenet.variables as var
import subprocess as sp

def logo():
    print('')
    sp.call('echo -e "\e[1m\e[31m88b 88  dP\'Yb   dP\'Yb  Yb  dP Yb  dP  TM\e[0m"',shell=True)
    sp.call('echo -e "\e[1m\e[34m88Yb88 dP   Yb dP   Yb  YbdP   YbdP\e[0m"',shell=True)
    sp.call('echo -e "\e[1m\e[32m88 Y88 Yb   dP Yb   dP  dPYb    88   \e[0m"',shell=True)
    sp.call('echo -e "\e[1m\e[33m88  Y8  YbodP   YbodP  dP  Yb   88  \e[39m NodeNet.\e[0m "',shell=True)
    print('')
    print(var.nodenet['Copyright'])
    print('')
    print(var.nodenet['Version'])
    print('For more information or update ->'+var.nodenet['Website']+'.')
    print('')

def log(tag_name, message):
    message = message.replace('\n', '\n'+tag(tag_name))
    print(tag(tag_name)+message)

def tag(tag_name):
    tag_length = 10
    padding_left = int((tag_length-len(tag_name))/2)
    padding_right = tag_length-padding_left-len(tag_name)
    string = '['+'.'*padding_left+tag_name+'.'*padding_right+'] '
    return string
