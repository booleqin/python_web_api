# -*-coding:utf-8 -*-
"""
加载配置信息
author @boole
date 2019-05-01
"""

import os
import configparser


def read_conf(name1, name2):
    """
    读取配置信息
    :param name1:
    :param name2:
    :return: info
    """
    conf_dir = os.path.abspath(os.path.join(os.getcwd(), "./conf/global.conf"))
    cp = configparser.ConfigParser()
    cp.read(conf_dir)
    info = cp.get(name1, name2)
    return info


if __name__ == '__main__':
    d = "dev"
    h = "host"
    host = read_conf(d, h)
    print(host)

