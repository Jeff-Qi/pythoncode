# -*- coding: utf-8 -*-
# @Time :2020/3/8 23:47
# @Author   :jerry qi
# @Email    :270352195@qq.com
import random


# 冒泡排序
import time


def mps(l):  # l is list and n is the list size
    n = len(l)
    if n <= 1:
        return
    print(l)
    s = time.time()
    flag = False
    for i in range(n):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                flag = True
        if not flag:
            break
    end = time.time()
    print(l)
    print(end - s)


# 插入排序
def crs(l):  # l is list and the n is the list's size
    n = len(l)
    if n <= 1:
        return
    for i in range(1, n):
        tmp = l[i]
        j = i - 1
        while j >= 0 and l[j] > tmp:
            l[j + 1], j = l[j], j - 1
        l[j + 1] = tmp
    print(l)


# 选择排序
def xzs(l):
    print(l)
    n = len(l)
    # for i in range(n - 1):
    #     for j in range(i + 1, n):
    #         if l[i] > l[j]:
    #             l[i], l[j] = l[j], l[i]   # 找出最小值交换次数过多，应该直接找到最小值，内循环完毕交换一次
    for i in range(n):
        min_index = i
        min_value = l[i]
        for j in range(i, n):
            if l[j] < min_value:
                min_index = j
                min_value = l[j]
        l[i], l[min_index] = l[min_index], l[i]
    print(l)


# 归并排序
def gbs(l, low, high):  # l is list, low is the first element equal l[0], high is the last element equal l[len - 1]
    if low >= high:
        return
    mid = low + (high - low) // 2
    gbs(l, low, mid)
    gbs(l, mid + 1, high)
    merge(l, low, mid, high)


def merge(l, low, mid, high):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if l[i] <= l[j]:
            tmp.append(l[i])
            i = i + 1
        else:
            tmp.append(l[j])
            j = j + 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(l[start:end + 1])
    l[low:high + 1] = tmp


# 快速排序
def kss(l, low, high):
    if low >= high:
        return
    k = random.randrange(low, high)
    l[low], l[k] = l[k], l[low]
    pivot = partition_two_way(l, low, high)
    kss(l, low, pivot-1)
    kss(l, pivot + 1, high)


def partition(l, low, high):
    pivot, i = l[low], low
    for j in range(low + 1, high + 1):
        if l[j] <= pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[low], l[i] = l[i], l[low]
    return i


def partition_two_way(l, low, high):
    pivot, i, j = l[low], low, high
    while i < j:
        while l[j] > pivot:
            j = j - 1
        while i <= j and l[i] <= pivot:     # 如果是这种写法 while l[i] <= pivot and i <= j:  着中写法存在越界问题
            i = i + 1
        if i < j:
            l[i], l[j] = l[j], l[i]
    l[j], l[low] = l[low], l[j]
    return j


# 桶排序
def tps(l):
    pass


# 计数排序
def jss(l):
    pass


# 基数排序
def jss_1(l):
    pass


# 二分查找
def efcz(l):
    pass


if __name__ == '__main__':
    unsort_list = [random.randrange(1, 10000) for i in range(10000)]
    li = [4, 3, 2, 1]
    mps(unsort_list)
    # crs(unsort_list, 20)
    # xzs(unsort_list)
    # print(li)
    # # gbs(unsort_list, 0, 9)
    # kss(li, 0, len(li) - 1)
    # print(li)
