# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:51:41 2017

@author: Edward
"""

# Think python, Chapter 2

width = 17
height = 12.0 
delimiter = "."
print width/2
print width/2.0
print height/3
print 1+2*5
print delimiter*5

# Exercise 2.4 page.26
#1
r = 5
pi = 3.141592657
volume = (4/3) * pi * r ** 3
print volume
volume = 4 / 3 * pi * r ** 3
print volume
volume = (4 / 3) * pi * (r**3)
print volume
print r ** 3
print pi * r ** 3
print (4 / 3.0) * pi * r ** 3 # caution 'floor division'
#2
bp = 24.95
discount = 0.4
sc_1=3
sc_2 = 0.75
total_c = bp*60*0.4+sc_1+ sc_2 * 59
print total_c
#3
leave = 6*3600+52*60
ep = 8*60+15
tempo= 7*60+12
back = leave + ep *2 +tempo *3
print back
back_h = back /3600
print back_h
back_m = (back - back / 3600 * 3600) / 60
print str(back_h)+":" + str(back_m)