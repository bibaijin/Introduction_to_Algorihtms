#!/usr/bin/python3
# Filename: Merge_Sort.py

'''合并排序'''

import data
# import tracemalloc

# tracemalloc.start()

def merge(A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = [A[p + i] for i in range(n1)]
    L.append(float('inf'))
    R = [A[q + j] for j in range(n2)]
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge_sort(A, p, r):
    if p < (r - 1):
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)

A = data.generate()
merge_sort(A, 0, len(A))
data.output(A)

# 估计内存使用
# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('filename')

# print("[ Top 10 ]")
# for stat in top_stats[:10]:
    # print(stat)
