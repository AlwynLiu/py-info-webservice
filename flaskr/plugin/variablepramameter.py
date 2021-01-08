#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


import schedule


# 不定长参数求和
def sum(*nums):
    result = 0
    for n in nums:
        result += n
    print(result)


sum(1, 2, 3, 4, 5)   # 15
sum(1, 3, 4)


# 不定长参数混用
# def show(a, *b, c):
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
#
#
# show(1, 2, 3, 4, c=5)


# def func(a, b, **nums):
#     print("a = ", a)
#     print("b = ", b)
#     print("nums = ", nums)
#
#
# func(a=1,b=2,c=21,d=18,e=20)

#
# # 函数的解包
# def func(a, b, c):
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
# # 定义一个元组数据
# t = (10, 15, 20)
# # 传递实参时，可以在序列类型的参数前添加*，自动会将序列中的元素依次作为参数传递
# func(*t)

#
# # 函数的解包
# def func(a, b, c):
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
# # 定义一个字典
# t = {'a': 10, 'b': 15, 'c': 20}
# # 通过**对字典进行解包
# func(**t)