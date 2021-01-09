#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

# def fn(a:int, b:bool, str='hello') -> int:
#     """
#     文档字符串的示例：
#     函数的作用：
#     函数的参数：
#         a: 作用，类型，默认值
#         b:……
#         c:……
#     """
#     return 10
#
# help(slice)


def huiwen(s):
    """
    递归判断字符串是否是回文
    """
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return huiwen(s[1:-1])

print(huiwen('abcba'))