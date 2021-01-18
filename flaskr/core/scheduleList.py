# -*- coding: utf-8 -*-
"""
@Author ： Alvin.Liu
"""
"""
利用schedule执行两个不同的间隔时间的任务
一个job间隔1秒钟
一个job2间隔2秒钟
"""



import schedule
import time
import random

def job(name):
    print('My name is :', name)


def job2():
    print('我是你得不到的爸爸')

name = 'alvin liu'
schedule.every(1).seconds.do(job, name)
schedule.every(2).seconds.do(job2)


while True:
    schedule.run_pending()
    time.sleep(1)

