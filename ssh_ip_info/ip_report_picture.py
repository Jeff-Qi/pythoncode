#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2020/2/13 23:04
# @Author   :jerqi
# @Email    :270352195@qq.com
# @File     :ip_report_picture.py
from pyecharts.faker import Faker
from pyecharts.charts import Bar, Pie, Map, Page
from pyecharts import options as opts
import ip_addr_info


def make_pie(t, c, count):
    name = t + '.html'
    c = (
        Pie().add(
            "",
            [list(z) for z in zip(c, count)],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        ).set_global_opts(title_opts=opts.TitleOpts(title=t))
    )
    return c


class ReportPicture:
    def __init__(self):
        self.conn = ip_addr_info.get_conn_obj()

    def ip_addr_top_bar(self):
        sql = '''
        select count_time, ip_addr, country, city
        from ip_addr_info
        order by count_time desc'''
        self.conn.exec_sql(sql)
        res = self.conn.cursor.fetchall()
        bar = Bar()
        ip_list, count = [], []
        for i in range(5):
            ip_list.append(res[i][1])
            count.append(res[i][0])
        bar.add_xaxis(ip_list)
        bar.add_yaxis('IP地址尝试连接次数TOP5', count)
        # bar.render('IP地址尝试次数.html')
        return bar

    def ip_addr_world_pie(self):
        num = 5
        sql = '''
        select country, count(country), count(country)/(select count(1) from ip_addr_info)
        from ip_addr_info
        group by country
        order by count(country) desc'''
        self.conn.exec_sql(sql)
        res = self.conn.cursor.fetchall()
        country = [c[0] for c in res[0: num]]
        country.append('Others')
        times = [t[1] for t in res[0: num]]
        times.append(sum([x[1] for x in res[num::1]]))
        return make_pie('IP地址世界分布', country, times)

    def ip_addr_china_pie(self):
        num = 5
        sql = '''
        select cs, count(cs), count(cs)/(select count(1) from ip_addr_info where country = 'China')
        from ip_addr_info
        where country='China'
        group by cs
        order by count(cs) desc'''
        self.conn.exec_sql(sql)
        res = self.conn.cursor.fetchall()
        cs = [c[0] for c in res[0: num: 1]]
        cs.append('Others')
        times = [c[1] for c in res[0: num: 1]]
        times.append(sum([x[1] for x in res[num:: 1]]))
        return make_pie('IP地址中国分布', cs, times)

    def page_simple_layout(self):
        page = Page(layout=Page.SimplePageLayout)
        page.add(
            self.ip_addr_top_bar(),
            self.ip_addr_world_pie(),
            self.ip_addr_china_pie()
        )
        page.render("IP地址信息汇总图.html")


if __name__ == '__main__':
    rp = ReportPicture()
    rp.page_simple_layout()
    rp.conn.close_all()