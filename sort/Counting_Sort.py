#!/usr/bin/python3
# Filename: Counting_Sort.py

"""计数排序"""

def counting_sort(A, k):
    """计数排序

    A 为需要排序的序列，k 为 A 中元素的最大值"""

    C = [0] * (k + 1)
    B = [0] * len(A)
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1   # C[i] 包含 i 出现的次数

    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]    # C[i] 包含 <= 的元素个数

    for j in range(0, len(A)):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B

A = [2, 5, 3, 0, 2, 3, 0, 3, 23, 1, 7, 3, 99]
print("原来的序列为：{}".format(A))
B = counting_sort(A, 500)
print("排序后的序列为：{}".format(B))
