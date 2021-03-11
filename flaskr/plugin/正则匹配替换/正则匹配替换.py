#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


import json
import re


def newPrint(*c):
  # if debug:
  print(c)

with open('./source_content.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    user_data_string = json.dumps(json_data)
    new12123 = re.sub("sys_id.*?user_id", "sys_id\": \"ceui\",\"user_id", user_data_string)
    print(new12123)
    print("json.loads(new12123)", json.loads(new12123))
    # print('这是文件中的json数据：', json_data)
    # print('这是读取到文件数据的数据类型：', type(json_data))
