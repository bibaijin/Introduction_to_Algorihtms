#!/usr/bin/python3
# Filename: Quick_Sort.py

"""快速排序

数组标号遵循 python 惯例，即含首不含尾。"""

def quick_sort(A, p, r):
    if p < r - 1:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    flag = A[r-1]   # 哨兵
    i = p-1 # 指向小于哨兵的数组尾部
    for j in range(p, r):
        if A[j] < flag:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r-1] = A[r-1], A[i+1]
    return i + 1

A = [2, 8, 7, 1, 3, 5, 6, 4]
print("原来的序列为：{}".format(A))
quick_sort(A, 0, len(A))
print("排序后的序列为：{}".format(A))
