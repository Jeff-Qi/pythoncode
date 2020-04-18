#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2020/4/13 23:04
# @Author   :jerqi
# @Email    :270352195@qq.com
# @File     :ssh_ip_info.py
# -*- coding: utf-8 -*-
# @Author   :jerqi
# @Email    :270352195@qq.com
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#
#
# def pre(root: Node):
#     if root:
#         print(root.data)
#         pre(root.left)
#         pre(root.right)
#
#
# def pre_2(root: Node):
#     if not root:
#         return None
#     node_list = []
#     p = root
#     res = []
#     while p or len(node_list):
#         while p:
#             node_list.append(p)
#             res.append(p.data)
#             p = p.left
#         if len(node_list):
#             p = node_list.pop()
#             p = p.right
#
#
# import sys
# import requests
#
#
# def query_ip_addr(ip):
#     url = 'http://ip-api.com/json/' + ip
#     response = requests.get(url)
#
#     strpp = {}
#     strpp = response.json()   # 将返回的json信息传递给dic
#     # 下面就是直接从字典取值，显示。
#     print('*******************************')
#     print('您查询的IP地址 % s来源地是:' % (strpp.get('query')))
#     print("国家: %s" %(strpp. get('country')))
#     print("城市: %s" % (strpp.get('city')))
#     print("经纬度坐标: %s, %s" % (strpp. get('lat'), strpp. get('lon')))
#     print("运营商编号: %s" % (strpp.get('as')))
#     print("ISP服务商: %s" % (strpp.get('isp')))
#     print("数据来源<www. ip-api. com查询IP归属地>")
#     print('*******************************')
#
#
# if __name__ == '__main__':
#     ip = "185.153.196.230"
#     query_ip_addr(ip)
# import pymysql
#
#
# conn = pymysql.connect(host='129.204.80.144', user='jeff', password='123456', port=3306, db='d1')
# corsur = conn.cursor()
# import math
#
#
# def fun(n):
#     flag = True
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             print('not')
#             flag = False
#             return flag
#
#
# def function(a):
#     b = a[::-1]
#     if a == b:
#         print('%s 是回文!' % a)
#     else:
#         print('%s 不是回文！' % a)
#
#
# function('12231')


# import sys
#
#
# def fun(li_1, li_2):
#     li_3, li_4 = [], []
#     for i in range(len(li_1)):
#         if li_1[i] != li_2[i]:
#             li_3.append(int(li_1[i]))
#             li_4.append(int(li_2[i]))
#
#     a = abs(li_3[0] - li_4[0])
#     flag = True
#
#     for i in range(len(li_3)):
#         if abs(li_3[i] - li_4[i]) == a:
#             continue
#         else:
#             flag = False
#             print('NO')
#             return flag
#
#     if flag:
#         print('YES')
#         return flag
#
#
# def fun(li_1, li_2, le):
#     s1, s2 = set(li_1), set(li_2)
#     s3, s4 = s1 - s2, s2 - s1
#
#
# if __name__ == '__main__':
#     t = sys.stdin.readline().strip()
#     t = int(t)
#     print(t)
#     for i in range(t):
#         n = sys.stdin.readline().strip()
#         n = int(n)
#         print(n)
#         li1 = list(sys.stdin.readline().strip().split())
#         print(li1)
#         li2 = list(sys.stdin.readline().strip().split())
#         print(li2)
#         fun(li1, li2, n)
# s = 'string'
# li = list(s)
# li.reverse()
# print(str(li))
# print(li)
# from pyecharts import options as opts
# from pyecharts.charts import Bar, Grid, Line, Page, Pie
# from pyecharts.faker import Faker
#
#
# def bar_datazoom_slider() -> Bar:
#     c = (
#         Bar()
#         .add_xaxis(Faker.days_attrs)
#         .add_yaxis("商家A", Faker.days_values)
#         # .set_global_opts(
#         #     title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
#         #     datazoom_opts=[opts.DataZoomOpts()],
#         # )
#     )
#     return c
#
#
# def line_markpoint() -> Line:
#     c = (
#         Line()
#         .add_xaxis(Faker.choose())
#         .add_yaxis(
#             "商家A",
#             Faker.values(),
#             markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
#         )
#         .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
#     )
#     return c
#
#
# def pie_rosetype() -> Pie:
#     v = Faker.choose()
#     c = (
#         Pie()
#         .add(
#             "",
#             [list(z) for z in zip(v, Faker.values())],
#             radius=["30%", "75%"],
#             center=["25%", "50%"],
#             rosetype="radius",
#             label_opts=opts.LabelOpts(is_show=False),
#         )
#         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
#     )
#     return c
#
#
# def page_simple_layout():
#     page = Page(layout=Page.SimplePageLayout)
#     page.add(
#         bar_datazoom_slider(),
#         line_markpoint(),
#         pie_rosetype()
#     )
#     page.render("page_simple_layout.html")
#
#
# if __name__ == "__main__":
#     page_simple_layout()
#
#
# class TreeNode:
#     def __init__(self, date):
#         self.date = date
#         self.left = None
#         self.right = None
#
#
# def level_order(root: TreeNode):
#     if not root:
#         return None
#     else:
#         queue = [root]
#     for i in queue:
#         print(i.date)
#         if i.left:
#             queue.append(i.left)
#         if i.right:
#             queue.append(i.right)
# #
#
# if __name__ == '__main__':
#     n1 = TreeNode(1)
#     n2 = TreeNode(2)
#     n3 = TreeNode(3)
#     n2.left = n3
#     n2.right = n1
#     level_order(n2)
#
#
# class LinkNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# def rev(root: LinkNode):
#     pre, now, nex = None, root, root.next
#     while now:
#         now.next = pre
#         pre = now
#         now = nex
#         nex = nex.next
print('hello')
