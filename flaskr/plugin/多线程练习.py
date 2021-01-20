# -*- coding: utf-8 -*-
"""
@Author ： Alvin.Liu
"""

import threading
import time


# # 当前线程对象
# t = threading.current_thread()
# # 当前线程名
# print(t.name)
# print(threading.active_count())
# t = threading.main_thread()
# print(t.name)


def thread_body():
    t = threading.current_thread()
    for n in range(5):
        print('第{0}次执行线程{1}\n'.format(n, t.name))
        time.sleep(2)
    print('线程{0}执行完成'.format(t.name))


t1 = threading.Thread(target=thread_body)
t2 = threading.Thread(target=thread_body, name='MyThread')
t1.start()
t2.start()
