# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:33:46 2017

@author: Edward
"""

x = int(raw_input("请输入要判断的数："))
num = x
num_p = 0
num_t = num

while num != 0:
    num_p = num_p * 10 + num %10
    num = num / 10
if num_p == num_t:
    #print " Matched "
    #判断素数
    for i in range(2,x):
        if x % i == 0:
            print "No"
            print i
            break
    else:
        print " Matched "
else:
    print " No "