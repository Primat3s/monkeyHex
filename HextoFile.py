#-*- coding:utf-8 -*-
import binascii

hex_data = ''
split_data = []

def readFile():
    with open("test2.png", "rb") as f:
        data = f.read()
    global hex_data
    hex_data = binascii.b2a_hex(data).decode('ascii').upper()

def splitData():
    global hex_data, split_data
    split_data = list(map(''.join, zip(*[iter(hex_data)]*2)))

def printData():
    global hex_data, split_data
    row_size = int(len(split_data)/16)
    if len(split_data) % 16 != 0 or len(split_data) < 16:
        row_size = row_size + 1
    for index, value in enumerate(split_data, start=1):
        print(value, end=' ')
        if index % 16 == 0:
            print('\n')


readFile()
splitData()
printData()