#!/usr/bin/python3
# Filename: Heap_Sort.py

class Heap:
    """堆排序。

    1. 为了运算和理解的方便，节点索引从 1 开始；
    2. 利用列表实现
    3. 为最大堆排序"""
    def __init__(self, heap=[]):
        self.heap = heap

    def parent(self, index): 
        "求父节点索引"
        return index // 2

    def left_child(self, index): 
        "求左子节点索引"
        return 2 * index

    def right_child(self, index):
        "求右子节点索引"
        return 2 * index + 1

    def max_heapify(self, index, n=None):
        """维护最大堆特性。
        
        对于以 index 为顶点、到第 n 个节点的子堆，假定其左子堆和右子堆满足最大堆特性，本方
        法使它自己也满足最大堆特性。"""
        if n is None:
            n =len(self.heap)
        l = self.left_child(index)
        r = self.right_child(index)
        max = index
        if l <= n and self.heap[l-1] > self.heap[index-1]:
            max = l
        if r <= n and self.heap[r-1] > self.heap[max-1]:
            max = r
        if max != index:
            tmp = self.heap[index-1]   # 交换 self.heap[index-1] 和 self.heap[max-1]
            self.heap[index-1] = self.heap[max-1]
            self.heap[max-1] = tmp
            self.max_heapify(max, n)  # 令 self.heap[index-1] 逐层下沉，直至其较大为止

    def build_max_heap(self):
        "构建最大堆"
        # n = len(heap)
        for i in range(len(self.heap) // 2, 0, -1):
            self.max_heapify(i)

def heap_sort(A):
    h = Heap(A)
    h.build_max_heap()
    for i in range(len(h.heap), 1, -1):
        tmp = h.heap[i-1]
        h.heap[i-1] = h.heap[0]
        h.heap[0] = tmp
        h.max_heapify(1, i-1)

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print("原来的序列为：{0}".format(A))
heap_sort(A)
print("排序后的序列为：{0}".format(A))
