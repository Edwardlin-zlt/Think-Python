# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:07:42 2017

@author: Edward
"""
import math
a = float(raw_input())
b = float(raw_input())
c = float (raw_input())
A = (-(c ** 2.0)+(a ** 2)+(b **2))/(2.0*a*b)
C= math.acos(A)
C1 = (C / math.pi) * 180
print C1