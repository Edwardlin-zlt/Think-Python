# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 15:29:06 2017

@author: Edward
"""

def print_twice(t):
    print t
    print t
def do_twice(j,i):   #j就是函数名了
    j(i)            #j()是 function call（函数调用） 
    j(i)
def do_four(j,i):
    do_twice(j,i)
    do_twice(j,i)
do_four(print_twice,'Edward')