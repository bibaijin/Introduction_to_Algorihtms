#!/usr/bin/python3
# Filename: data.py

'''产生随机序列'''

import random

def generate():
    '''产生随机序列'''
    A = list(range(100))
    random.shuffle(A)
    print('随机数列为：', A)
    return A

def output(A):
    print('排序后的数列为：', A)
