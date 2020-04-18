# -*- coding: utf-8 -*-
# @Time :2020/2/11 20:16
# @Author   :jerry qi
# @Email    :270352195@qq.com


class Node(object):
    def __init__(self, data, next_node = None):
        self.__data = data
        self.__next = next_node

    @property   # 该装饰器，将 data 变成只读属性
    def data(self):
        return self.__data

    @data.setter    # setter 装饰后，可以对属性进行修改
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        self.__next = next_node


class SinglyLinkedList(object):
    def __init__(self):
        self.__head = Node(None)

    def find_by_values(self, value):
        node = self.__head.next_node
        if (node is not None) or (node.data is not value):
            node = node.next_node
        return node

    def find_by_index(self, index):
        node = self.__head.next_node
        pos = 0
        if (node is None) or (index <= 0):
            return
        while (pos < index) and (node is not None):
            node = node.next_node
            pos = pos + 1
        return node

    def insert_into_head(self, value):
        new_node = Node(value)
        head_node = self.__head.next_node
        new_node.next_node = head_node.next_node
        head_node.next_node = new_node

    def insert_into_last(self, value):
        new_node = Node(value)
        p_node = self.__head.next_node
        while p_node.next_node is not None:
            p_node = p_node.next_node
        new_node.next_node = p_node.next_node
        p_node.next_node = new_node

    def reversed(self):
        pre_node = None
        now_node = self.__head.next_node
        then_node = self.__head.next_node.next_node
        if now_node is None:
            return now_node
        if then_node is None:
            return then_node
        while now_node.next_node is not None:
            now_node.next_node = pre_node
            pre_node = now_node
            now_node = then_node
            then_node = then_node.next_node
        now_node.next_node = pre_node
        self.__head.next_node = now_node

    def has_ring(self):
        fast = self.__head.next_node
        slow = self.__head.next_node
        while fast is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast is slow:
                return True
        return False

    def find_mid_node(self):
        fast = self.__head.next_node
        slow = self.__head.next_node
        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node
        return slow

    def delete_last_index(self, n):
        fast = self.__head.next_node
        slow = self.__head.next_node
        pos = 0
        while pos < n:
            fast = fast.next_node
            pos = pos + 1
        while fast is not None:
            t = slow
            fast = fast.next_node.next_node
            slow = slow.next_node
        t.next_node = slow.next_node

    def merge_tow_to_one(self, first_link, second_link):
        f_1 = first_link.next_node
        s_1 = second_link.next_node
        f_2 = first_link.next_node.next_node
        s_2 = first_link.next_node.next_node
        if f_1.data < s_1.data:
            self.merge_fun(f_1, f_2, s_1, s_2)
            second_link = None
            return first_link
        else:
            self.merge_fun(s_1, s_2, f_1, f_2)
            first_link = None
            return  second_link

    def merge_fun(self, p, q, m, n):
        while q is not None:
            if q.data >= m.data:
                m.next_node = q
                p.next_node = m
                p = m
                m = n
                n = n.next_node
                continue
            else:
                p = q
                q = q.next_node
        p.next_node = m
