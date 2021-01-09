#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

"""
装饰器的目的是对函数进行扩展
"""

def begin_end(oldfunc):
    """
    手动定义一个装饰器
    """

    # 参数的装包
    def newfunc(*args, **kwargs):

        print('函数开始执行了~~~~~~~~~')
        # 参数的解包
        result = oldfunc(*args, **kwargs)
        print('函数执行完成了~~~~~~~~~~~')
        return result
    return newfunc

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

a = begin_end(add)
m = begin_end(mul)

print(a(12, 32))
print(m(10, 20))


# 装饰器的用法
@begin_end
def sayHello():
    print('hello 弟弟？')

sayHello()