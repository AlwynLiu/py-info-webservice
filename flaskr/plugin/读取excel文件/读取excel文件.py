#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


import json


from openpyxl import load_workbook
# workbook = xlrd.open_workbook_xls('202102养固健内销明细.xlsx')
workbook = load_workbook('202102养固健内销明细.xlsx')

# print(workbook.sheetnames)

# current_sheet = workbook['明细']
# detail_sheet_json = []
# for i in range(1, current_sheet.max_row + 1):
#     sub_data = {}
#     sub_data['order'] = current_sheet.cell(i, 1).value
#     sub_data['wechat_name'] = current_sheet.cell(i, 2).value
#     sub_data['employee_id'] = current_sheet.cell(i, 3).value
#     sub_data['employee_name'] = current_sheet.cell(i, 4).value
#     detail_sheet_json.append(sub_data)
    
# print(detail_sheet_json)

address_sheet = workbook['配送地址']
address_sheet_json = []
for i in range(1, address_sheet.max_row + 1):
    if address_sheet.cell(i, 1).value != '配送至':
        sub_data = {}
        sub_data['branch_company'] = address_sheet.cell(i, 1).value
        sub_data['address'] = address_sheet.cell(i, 2).value
        sub_data['consignee'] = address_sheet.cell(i, 3).value
        sub_data['consignee_tel'] = address_sheet.cell(i, 4).value
        address_sheet_json.append(sub_data)
# print('配送地址的数据：', address_sheet_json)
for i in address_sheet_json:
    print('配送的地址项：', i)

# worksheets = workbook.sheet_names()
# print('worksheets is %s' %worksheets)
