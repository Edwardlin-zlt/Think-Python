# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:57:09 2017

@author: Edward
"""

n = int (raw_input())
s = n % 60
n = n / 60
m = n % 60
h = n / 60
print h," ",m," ",s