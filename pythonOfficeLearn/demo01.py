#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: demo01.py
# Author: Adonis
# Mail: clarenceguo2060@gmail.com
# Created Time:  2022-7-13-09-00-00
# Description: 素数判断
#############################################
import sys

number = int(sys.argv[1])
if number != 1:
    for i in range(2, number):
        if number % i == 0:
            print('false')
            break
    else:
        print('true')

else:
    print('false')
