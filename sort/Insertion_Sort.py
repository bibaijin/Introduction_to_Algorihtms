#!/usr/bin/python3
# Filename: Insertion_Sort.py

'''插入排序'''

import data
# import tracemalloc

# tracemalloc.start()

A = data.generate()

# 核心算法
for j in range(1,len(A)):
    key = A[j]
    # 将 A[j] 插入排好序的 A[1...j-1]
    i = j-1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key

data.output(A)

# 估计内存使用
# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('filename')

# print("[ Top 10 ]")
# for stat in top_stats[:10]:
    # print(stat)
