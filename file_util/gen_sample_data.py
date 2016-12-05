# -*- coding: utf-8 -*-
import datetime

file_obj = open('data.csv')
all_lines = file_obj.readlines()
line_number = len(all_lines)

# 将数据转换为整数数组
# 兼容2/3，采用list()，否则在3中返回map对象
# data = list(map(lambda x: list(map(lambda y: int(y), x.strip().split(','))), all_lines))
# 实际是可以在后面进行转换
data = list(map(lambda x: x.strip(), all_lines))

# 进行合并
for i in range(0, (line_number - 40)):
    # print("Enter, i = %d" % (i))
    line_to_be_write = ""
    for j in range(30):
    	line_to_be_write += (data[i + j] + " ")
    print(line_to_be_write)
    print(int(data[i + 30].split(",")[3]) / int(data[i + 29].split(",")[3]))
    print(int(data[i + 34].split(",")[3]) / int(data[i + 29].split(",")[3]))
    print(int(data[i + 39].split(",")[3]) / int(data[i + 29].split(",")[3]))

# # print((datetime.datetime.strptime(all_lines[1].split("\t")[0], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(all_lines[0].split("\t")[0], "%Y-%m-%d %H:%M:%S")).total_seconds())
