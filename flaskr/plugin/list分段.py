#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(number_list), 10):
    print(number_list[i:i+10])
    
    
number_list1 = [3, 1, 2, 4]
print(number_list1[1::])
