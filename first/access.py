# -*- coding: utf-8 -*-
# @Time :2020/2/2 10:59
# @Author   :jerry qi
# @Email    :270352195@qq.com

import random


def fun_get_name():
    first_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    second_name = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    xing = random.choice(first_name)
    ming = "".join(random.choice(second_name) for i in range(2))
    name = xing + ming
    return name


def fun_get_object():
    school_object = ['物联网工程', '软件工程', '通信工程', '信息安全', '工艺设计', '机械制造', '国际贸易', '汉语言文学',
                 '车辆工程', '农业机械装备']
    get_object = random.choice(school_object)
    return get_object


def main():
    print("this is main function")


if __name__ == '__main__':
    main()
    print(__name__)
