#!/usr/bin/python3
# Filename: Max_Subarray.py

'''在数字序列中寻找和最大的连续子列'''

def Find_Max_Crossing_Subarray(A, low, mid, high):
    left_total = - float('Inf')
    total = 0
    for i in range(mid - 1, low - 1, -1):
        total = total + A[i]
        if total > left_total:
            left_total = total
            max_left = i
    right_total = - float('Inf')
    total = 0
    for i in range(mid, high):
        total = total + A[i]
        if total > right_total:
            right_total = total
            max_right = i
    return (max_left, max_right + 1, left_total + right_total)

def Find_Maximum_Subarray(A, low, high):
    if high - 1 == low:
        return (low, high, A[low])
    mid = (low + high) // 2
    left_low, left_high, left_total = Find_Maximum_Subarray(A, low, mid)
    right_low, right_high, right_total = Find_Maximum_Subarray(A, mid, high)
    cross_low, cross_high, cross_total = Find_Max_Crossing_Subarray(A, low, mid, high)
    if left_total >= right_total and left_total >= cross_total:
        return (left_low, left_high, left_total)
    elif right_total >= left_total and right_total >= cross_total:
        return (right_low, right_high, right_total)
    else:
        return (cross_low, cross_high, cross_total)

with open('data.txt', 'r') as f:
    line = f.read()
    A = list(map(int, line.split()))

low, high, total = Find_Maximum_Subarray(A, 0, len(A))
print('low: {0}, high:  {1}, total: {2}'.format(low, high, total))
