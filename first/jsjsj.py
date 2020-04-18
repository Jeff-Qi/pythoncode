# -*- coding: utf-8 -*-
# @Time :2020/1/22 22:12
# @Author   :jerry qi
# @Email    :270352195@qq.com

import access
import pymysql

conn = pymysql.connect(
    host='106.14.145.0',
    port=3306,
    user='jeff',
    password='123456',
    db='jsjsj'
)
cursor = conn.cursor()

def insert_student_teacher_info():
    for i in range(2004, 2031):
        name = access.fun_get_name()
        sql = """
        insert into student_school_info
        (user_id,user_real_name,user_role)
        values
        (%d,'%s',%d)
        """ % (i, name, 1)
        cursor.execute(sql)

    for i in range(3005, 3101):
        sql = """
        insert into student_school_info
        (user_id,user_real_name,user_role)
        values
        (%d,'%s',%d)
        """ % (i, access.fun_get_name(), 2)
        cursor.execute(sql)


def insert_student_info():
