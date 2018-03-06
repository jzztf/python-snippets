#!/usr/bin/env python3
#coding=utf-8

import csv,os

os.makedirs('headerRemoved',exist_ok=True)

def removeCsvHeader():
    for csvfile in os.listdir('.'):
        if csvfile.endswith(".csv"):
            with open(csvfile,'r') as f:
                reader = csv.reader(f)
                newCsvfile = os.path.join('headerRemoved',csvfile)
                with open(newCsvfile,'w') as new_f:
                    writer = csv.writer(new_f)
                    for line in reader:
                        if reader.line_num == 1:
                            continue
                        else:
                            writer.writerow(line)

removeCsvHeader()

# 测试
#with open("bank-data.csv",'r') as f:
    #reader = csv.reader(f)
    #reader_list = list(reader)
    #print(reader_list[:3])

#with open("headerRemoved/bank-data.csv",'r') as f:
    #reader = csv.reader(f)
    #reader_list = list(reader)
    #print(reader_list[:3])
