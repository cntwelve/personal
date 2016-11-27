# -*- coding: utf-8 -*-
import datetime

file_obj = open('putty.log')
all_lines = file_obj.readlines()
line_number = len(all_lines)
for i in range(line_number):
    all_lines[i] = all_lines[i].replace("\n", "")
# print(all_lines[0])
# print(all_lines[0].replace("\n", "").split("\t"))

for i in range(0, (line_number - 4)):
    # print("Enter, i = %d" % (i))
    line_to_be_write = ""
    line_to_be_write += all_lines[i].split("\t")[1]
    for j in range(1, 5):
        # print("   --- j = %d" % (j))
        if (datetime.datetime.strptime(all_lines[i + j].split("\t")[0], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(all_lines[i].split("\t")[0], "%Y-%m-%d %H:%M:%S")).total_seconds() <= 300:
            line_to_be_write += (" " + all_lines[i + j].split("\t")[1])
        else:
            break
    print(line_to_be_write)

# print((datetime.datetime.strptime(all_lines[1].split("\t")[0], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(all_lines[0].split("\t")[0], "%Y-%m-%d %H:%M:%S")).total_seconds())
