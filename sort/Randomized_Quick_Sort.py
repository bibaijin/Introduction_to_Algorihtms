#!/usr/bin/python3
# Filename: Randomized_Quick_Sort.py

"""快速排序（含随机化）

数组标号遵循 python 惯例，即含首不含尾。"""

from random import randint
from Quick_Sort import partition

def randomized_quick_sort(A, p, r):
    if p < r - 1:
        q = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q)
        randomized_quick_sort(A, q+1, r)

def randomized_partition(A, p, r):
    i = randint(p, r-1)
    A[i], A[r-1] = A[r-1], A[i]
    return partition(A, p, r)

A = [2, 8, 7, 9, 1, 3, 100, 5, 6, 4]
print("原来的序列为：{}".format(A))
randomized_quick_sort(A, 0, len(A))
print("排序后的序列为：{}".format(A))
