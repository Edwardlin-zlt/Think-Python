# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:38:02 2017

@author: Edward
"""

import math  
def quadratic_equation(a, b, c):  
    t = math.sqrt(pow(b, 2) - 4 * a * c)  
    if(pow(b, 2) - 4 * a * c) > 0:  
        return (-b + t) / (2 * a), (-b - t) / (2 * a)     
    elif (pow(b, 2) - 4 * a * c) == 0:   
        return (-b + t) / (2 * a)  
    else:  
        return None  
print quadratic_equation(10, 40, 15)  