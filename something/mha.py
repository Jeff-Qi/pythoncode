# -*- coding: utf-8 -*-
# @Time :2020/2/27 18:07
# @Author   :jerry qi
# @Email    :270352195@qq.com
import os
import requests


def get_manager_and_node():
    url_m = '''https://github.com/yoshinorim/mha4mysql-manager/releases/download/v0.58/mha4mysql-manager-0.58-0.el7.centos.noarch.rpm'''
    url_n = '''https://github.com/yoshinorim/mha4mysql-node/releases/download/v0.58/mha4mysql-node-0.58-0.el7.centos.noarch.rpm'''
    filename_m = url_m.split("/")[-1]
    filename_n = url_n.split('/')[-1]
    print('tarting download ...')
    req_m = requests.get(url_m)
    req_n = requests.get(url_n)
    if req_m.status_code != 200 or req_n.status_code != 200:
        print('Fail!')
        return
    try:
        with open(filename_m, 'wb') as f:
            f.write(req_m.content)
            print('Manager download success!')
        with open(filename_n, 'wb') as f:
            f.write(req_n.content)
            print('Node success!')
    except Exception as e:
        print(e)


def install_software(manager_node=None):
    print('Starting install node ...')
    os.system('yum localinstall -y mha4mysql-node-0.58-0.el7.centos.noarch.rpm')
    print('node ok!')
    if manager_node:
        print('Starting install manager ...')
        os.system('yum localinstall -y mha4mysql-manager-0.58-0.el7.centos.noarch.rpm')
        print('manager ok!')


def write_conf():
    print('Staring create conf file for MHA ...')


if __name__ == '__main__':
    print('Starting MHA install ...')
    get_manager_and_node()
    is_manager = input('Whether chose to manager node Y/N ? (Default N)')
    install_software(is_manager)
