#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2020/4/13 23:04
# @Author   :jerqi
# @Email    :270352195@qq.com
# @File     :ip_report_picture.py
import ip_addr_info


class Report:
	def __init__(self):
		self.conn = ip_addr_info.ConnectToMysql()
			
	def get_count_top(self, number=10):
		sql = '''select count_time as Times, ip_addr as IP, country as Country, city as City
		from ip_addr_info
		order by Times desc
		limit %s''' % number
		self.conn.exec_sql(sql)
		res = self.conn.cursor.fetchall()
		for i in res:
			print('访问次数：%-10s IP地址：%-15s 归属国家：%-10s 所在城市：%-10s' % (i[0], i[1], i[2], i[3]))

	def get_country_top(self, number=10):
		sql = '''select country as Country, count(country) as Times,
		count(country)/(select count(*) from ip_addr_info) as Ratio
		from ip_addr_info
		group by country
		order by Times desc
		limit %s''' % number
		self.conn.exec_sql(sql)
		res = self.conn.cursor.fetchall()
		for i in res:
			print('IP归属国家：%-15s IP个数：%-15s 占比：%-10s' % (i[0], i[1], i[2]))

	def running(self):
		while True:
			print('*' * 30)
			print('1. IP地址访问统计信息')
			print('2. IP地址归属国家统计信息')
			print('0. 退出')
			print('*' * 30)
			choice = int(input('选择信息报告类型：'))
			if choice == 1:
				num = input('输入显示行数（默认10）：')
				if num:
					self.get_count_top(int(num))
				else:
					self.get_count_top()
			elif choice == 2:
				num = input('输入显示行数（默认10）：')
				if num:
					self.get_country_top(int(num))
				else:
					self.get_country_top()
			elif choice == 0:
				print('退出')
				self.conn.close_all()
				return None
			else:
				print('错误输入！请重新输入')
				continue


def get_report_obj():
	return Report()


if __name__ == '__main__':
	rep = Report()
	rep.running()

