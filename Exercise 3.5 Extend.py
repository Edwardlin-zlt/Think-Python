# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:13:32 2017

@author: Edward
"""

def print_grid1(x,y): #第一行
    print str(x),str(y)*4,
    print str(x),str(y)*4,str(x)
def print_grid2(x):  #第二行
    print str(x),' '*4,
    print str(x),' '*4,str(x)
def print_twice(j): #5行一组，打印两次
    j()
    j()
def print_four(j,i):  #打印同样的四行
    j(i)
    j(i)
    j(i)
    j(i)
def print_grid3(): #五行一组（第一行及其之后的四行）
    print_grid1(1,2)
    print_four(print_grid2,5)
def print_grid(): #打印两组加上结尾一行，结尾一行等同于第一行
    print_twice(print_grid3)
    print_grid1(3,4)
print_grid()