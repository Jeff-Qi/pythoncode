#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2020/4/13 23:04
# @Author   :jerqi
# @Email    :270352195@qq.com
# @File     :ip_report_picture.py
# 审计linux中ssh登录失败的日志，去重统计尝试暴力登录的ip地址，转储到数据库中，并对其进行地区查询
from time import sleep
import requests
import pymysql
import os


class ConnectToMysql:
    def __init__(self, host_ip='129.204.80.144', user_name='jeff', pass_word='123456', port_default=3306, db_name='d1'):
        self.host = host_ip
        self.user = user_name
        self.password = pass_word
        self.port = port_default
        self.db = db_name
        self.connect = None
        self.cursor = None

    def get_conn(self):
        if not self.connect:
            conn = pymysql.connect(host=self.host,
                                   user=self.user,
                                   passwd=self.password,
                                   port=self.port,
                                   db=self.db)
            self.connect = conn

    def get_cursor(self):
        if not self.connect:
            self.get_conn()
        if not self.cursor:
            self.cursor = self.connect.cursor()

    def exec_sql(self, sql):
        if not self.cursor:
            self.get_cursor()
        self.cursor.execute(sql)
        self.connect.commit()

    def close_all(self):
        if self.cursor:
            self.cursor.close()
        if self.connect:
            self.connect.close()


class Action:
    def __init__(self, f, obj: ConnectToMysql):
        self.obj = obj
        self.li = []
        self.file = f

    def read_ip(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                for i in f.readlines():
                    data = i.split()
                    count, ip = data[0], data[1]
                    if self.search_in_db(ip):
                        self.update_old_ip(ip, count)
                    else:
                        try:
                            dic = self.get_ip_info(ip)
                            data.append(dic.get('country'))
                            data.append(dic.get('regionName'))
                            data.append(dic.get('city'))
                            self.add_new_ip(data)
                        except Exception:
                            print('www.ip_api.com time out!')
                            print('wait 10s and try again!')
                            sleep(10)
                            self.li.append(data)
        else:
            print('file is not exist program quit!')
        self.solve_timeout()

    def solve_timeout(self):
        if self.li:
            try:
                data = self.li.pop()
                count, ip = data[0], data[1]
                dic = self.get_ip_info(ip)
                data.append(dic.get('country'))
                data.append(dic.get('regionName'))
                data.append(dic.get('city'))
                self.add_new_ip(data)
            except Exception:
                print('your network is not stable! please check you network and later try again!')

    def search_in_db(self, ip):
        sql = "select 1 from ip_addr_info where ip_addr = '%s'" % ip
        self.obj.exec_sql(sql)
        res = self.obj.cursor.fetchone()
        return res

    @staticmethod
    def get_ip_info(ip):        # get the json message of the ip address
        url = 'http://ip-api.com/json/' + ip
        res = requests.get(url)
        dic = res.json()
        return dic

    def add_new_ip(self, data):
        sql = '''insert into ip_addr_info
                (count_time, ip_addr, country, cs, city) 
                values
                (%s, '%s', '%s', '%s', '%s')''' % (data[0], data[1], data[2], data[3], data[4])
        self.obj.exec_sql(sql)
        print(data[1] + ' add to the database!')

    def update_old_ip(self, ip, count):
        sql = "update ip_addr_info set count_time = %s where ip_addr = '%s'" % (count, ip)
        self.obj.exec_sql(sql)
        print(ip + ' has update!')

    def get_top(self, number):
        sql = "select count_time, ip_addr, country, city from ip_addr_info order by count_time desc limit %s" % number
        self.obj.exec_sql(sql)
        res = self.obj.cursor.fetchall()
        return res

    def run(self):
        self.read_ip()
        self.obj.close_all()
        print('finish!')


def get_conn_obj():
    return ConnectToMysql()


if __name__ == '__main__':
    db = ConnectToMysql()
    file = input('input the path to the ip file:')
    actor = Action(file, db)
    actor.run()
