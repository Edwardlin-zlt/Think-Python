# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:41:08 2017

@author: Edward
"""

weight = float(raw_input('weight(Kg) = '))
high = float(raw_input('high(M) = '))
BMI = weight / (high ** 2)
print '{:.2f}'.format(BMI)
