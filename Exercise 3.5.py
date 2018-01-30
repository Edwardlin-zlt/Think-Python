# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 15:59:03 2017

@author: Edward
"""

def print_grid1():
    print '+','-'*4,
    print '+','-'*4,'+'
def print_grid2():
    print '|',' '*4,
    print '|',' '*4,'|'
def print_twice(j):
    j()
    j()
def print_four(j):
    j()
    j()
    j()
    j()
def print_grid3():
    print_grid1()
    print_four(print_grid2)
def print_grid():
    print_twice(print_grid3)
    print_grid1()
print_grid()