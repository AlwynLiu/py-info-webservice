#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


# 闭包使用的目的是为了数据安全

# 形成闭包的条件
# 1、函数嵌套
# 2、将内部函数作为返回值返回
# 3、内部函数必须要使用到外部函数的变量
def make_numbers():
    """
        求数的平均数
    """
    nums = []

    def averager(n):
        nums.append(n)
        return sum(nums)/len(nums)

    return averager

averager = make_numbers()

print(averager(10))
print(averager(20))
print(averager(30))
print(averager(40))