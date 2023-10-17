import os
import glob
import pandas as pd

# 设置目标文件夹路径和合并后的文件名
folder_path = r'D:\work\bgy\finance\1st'
output_file_name = r'D:\work\bgy\finance\merged.xlsx'

# 获取目标文件夹中所有的Excel文件
all_files = glob.glob(os.path.join(folder_path, '*.xls*'))

# 将Excel文件读入DataFrame，并添加到一个列表中
df_list = []
for file in all_files:
    df = pd.read_excel(file)
    print('------', df)
    df_list.append(df)

# 将DataFrame列表合并成一个大的DataFrame，并将其写入到Excel文件中
writer = pd.ExcelWriter(output_file_name)
for i, df in enumerate(df_list):
    df.to_excel(writer, 'sheet{}'.format(i+1), index=False)
writer.close()
