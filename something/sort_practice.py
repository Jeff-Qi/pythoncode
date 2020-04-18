# -*- coding: utf-8 -*-
# @Time :2020/2/25 17:07
# @Author   :jerry qi
# @Email    :270352195@qq.com
import random
from typing import List


def bubble(li: List, le: int):
    if le <= 1:
        return
    for i in range(le):
        flag = False
        for j in range(0, le - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                flag = True
        if not flag:
            break
    print(bubble.__name__, li)


def insert(li: List, le: int):
    for i in range(1, le):
        j, tmp = i - 1, li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


def select(li: List, le: int):
    for i in range(le):
        min_index, min_value = i, li[i]
        for j in range(i, le):
            if li[j] < min_value:
                min_value, min_index = li[j], j
        li[i], li[min_index] = li[min_index], li[i]


def gb(li, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    gb(li, low, mid)
    gb(li, mid + 1, high)
    merger(li, low, mid, high)


def merger(li, low, mid, high):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(li[start: end + 1])
    li[low: high + 1] = tmp


def fast(li, low, high):
    if low >= high:
        return
    number = random.randrange(low, high)
    li[high], li[number] = li[number], li[high]
    p = partition(li, low, high)
    fast(li, low, p - 1)
    fast(li, p + 1, high)


def partition(li, low, high):
    i, value = low, li[high]
    for j in range(low, high):
        if li[j] <= value:
            li[i], li[j] = li[j], li[i]
            i += 1
    li[i], li[high] = li[high], li[i]
    return i


def half(li, low, high, value):
    while low <= high:
        mid = low + (high - low) // 2
        if li[mid] < value:
            low = mid + 1
        elif li[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1


def creat_li(n):
    return [random.randrange(1, 10 * n) for i in range(n)]


if __name__ == '__main__':
    bubble(creat_li(10), 10)
    insert(creat_li(10), 10)
    select(creat_li(10), 10)
    gb(creat_li(10), 0, 9)
    fast(creat_li(10), 0, 9)
    test_li = sorted(creat_li(10))
    test_number = random.choice(test_li)
    result = half(test_li, 0, 10, test_number)
