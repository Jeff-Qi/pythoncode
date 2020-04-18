#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2020/4/15 11:33
# @Author   :jerqi
# @Email    :270352195@qq.com
# @File     :heap.py


class Heap:
    def __init__(self):
        self.count = 0
        self.li = []
        self.max = 0

    def heap(self, n):
        self.max = n
        self.li.append('#')

    def heap_dh(self, n, i):       # 从上往下堆化
        while True:
            maxpos = i
            li = self.li
            if i * 2 <= n and li[i] < li[i * 2]:
                maxpos = i * 2
            if i * 2 + 1 <= n and li[maxpos] < li[i * 2 + 1]:
                maxpos = i * 2 + 1
            if maxpos == i:
                break
            li[maxpos], li[i] = li[maxpos], li[i]
            i = maxpos

    def insert(self, data):     # 从下往上堆化
        if self.count >= self.max:
            return
        self.count += 1
        self.li.append(data)
        p = self.count
        while p // 2 > 0 and self.li[p] > self.li[p // 2]:
            self.li[p], self.li[p // 2] = self.li[p // 2], self.li[p]
            p = p // 2

    def delete(self):
        if self.count <= 0:
            return
        li = self.li
        li[1] = li[self.count]
        self.count -= 1
        self.heap_dh(self.count, 1)

    def build_heap(self):
        i = self.count // 2
        while i >= 1:
            self.heap_dh(self.count, 1)

    def sort_heap(self):
        self.build_heap()
        k = self.count
        while k >= 1:
            print(self.li[1])
            self.li[1], self.li[k] = self.li[k], self.li[1]
            k -= 1
            self.heap_dh(k, 1)
