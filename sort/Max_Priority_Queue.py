#!/usr/bin/python3
# Filename: Max_Priority_Queue.py

import Heap
class Max_Priority_Queue(Heap):
    """最大优先级队列。

    1. 使用最大堆实现；
    2. 若返回 -1，则说明越界
    """
    def __init__(self, queue=[]):
        super().__init__(queue)
        super().build_max_heap()

    def insert(self, key):
        self.heap.append(-float('inf'))
        self.increase_key(len(self.heap), key)

    def maximum(self):
        return self.heap[0]

    def extract_max(self):
        if len(self.heap) < 1:
            print("队列长度为 0 ！")
            return -1
        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        super().max_heapify(1)
        return maximum

    def increase_key(self, i, key):
        if key < self.heap[i-1]:
            print("新键比旧键小！")
            return
        self.heap[i-1] = key
        while self.heap[i-1] > self.heap[super().parent(i)-1]:
            tmp = self.heap[i-1]
            self.heap[i-1] = self.heap[super().parent(i)-1]
            self.heap[super().parent(i)-1] = tmp
            i = super().parent(i)
