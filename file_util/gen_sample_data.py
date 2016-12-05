# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description="日数据组合程序")
parser.add_argument(
    "-f", "--file", help="日数据文件", default="data.csv")

args = parser.parse_args()

gen_target = lambda x: 5 if x>0.03 else 4 if x>0.01 else 3 if x>-0.01 else 2 if x>-0.03 else 1

file_obj = open(args.file)
all_lines = file_obj.readlines()
file_obj.close()
line_number = len(all_lines)

# 将数据转换为整数数组
# 兼容2/3，采用list()，否则在3中返回map对象
# data = list(map(lambda x: list(map(lambda y: int(y), x.strip().split(','))), all_lines))
# 实际是可以在后面进行转换
data = list(map(lambda x: x.strip(), all_lines))

feature_file = open("feature.txt", "w")
target1_file = open("target1.txt", "w")
target5_file = open("target5.txt", "w")
target10_file = open("target10.txt", "w")
# 进行合并
for i in range(0, (line_number - 40)):
    # print("Enter, i = %d" % (i))
    line_to_be_write = ""
    for j in range(30):
        # line_to_be_write += (data[i + j] + ",")
        line_to_be_write += (data[i + j][9:] + ",")
    # print(line_to_be_write[:-1])
    feature_file.writelines(line_to_be_write[:-1] + "\n")
    # print(int(data[i + 30].split(",")[4]) / int(data[i + 29].split(",")[4]))
    # print(int(data[i + 34].split(",")[4]) / int(data[i + 29].split(",")[4]))
    # print(int(data[i + 39].split(",")[4]) / int(data[i + 29].split(",")[4]))
    target1_file.writelines(
        str(int(data[i + 30].split(",")[4]) / int(data[i + 29].split(",")[4])) + "\n")
    gain1 = int(data[i + 30].split(",")[4]) / int(data[i + 29].split(",")[4]) - 1
    print(str(gen_target(gain1)))
    target5_file.writelines(
        str(int(data[i + 34].split(",")[4]) / int(data[i + 29].split(",")[4])) + "\n")
    target10_file.writelines(
        str(int(data[i + 39].split(",")[4]) / int(data[i + 29].split(",")[4])) + "\n")
feature_file.close()
target1_file.close()
target5_file.close()
target10_file.close()
