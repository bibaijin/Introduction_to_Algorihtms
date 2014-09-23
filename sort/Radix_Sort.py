#!/usr/bin/python3
# Filename: Radix_Sort.py

"""基数排序"""

# from Counting_Sort import counting_sort

def radix_sort(A, d):
    """基数排序

    1. A 为整数数组，位数相等
    2. d 为位数
    3. 不是在原数组操作"""
    S = [tuple(map(int, str(A[i]))) for i in range(len(A))] # 将整数分割成d位
    for i in range(0, d):
        S = counting_sort(S, d - 1 - i, 9)

    return [int(''.join(map(str, S[i]))) for i in range(len(S))]    # 变回整数

def counting_sort(S, index, k):
    """在每一位上的排序
    
    1. k + 1 进制"""

    C = [0] * (k + 1)
    B = [0] * len(S)
    for j in range(0, len(S)):
        C[S[j][index]] = C[S[j][index]] + 1   # C[i] 包含 i 出现的次数

    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]    # C[i] 包含 <= 的元素个数

    for j in range(len(S) - 1, -1, -1): # 为了稳定性，必须倒序
        B[C[S[j][index]] - 1] = S[j]
        C[S[j][index]] = C[S[j][index]] - 1

    return B

A = [329, 457, 657, 839, 436, 720, 355]
print("原来的序列为：{}".format(A))
B = radix_sort(A, 3)
print("排序后的序列为：{}".format(B))
