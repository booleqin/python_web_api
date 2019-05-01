# -*-coding:utf-8-*-
"""
gunicorn start flask api
author @boole
date 2019-05-01
"""

import multiprocessing
from load_conf import read_conf

host = read_conf("dev", "host")
port = read_conf("dev", "port")
pidpath = read_conf("dev", "pidpath")
logpath = read_conf("dev", "logpath")
cpu_cnt = multiprocessing.cpu_count()  # 计算cpu数 一般并发数为cpu * 2 + 1

bind = ":".join(list([host, port]))
backlog = 2048
workers = cpu_cnt * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
reload = True
reload_engine = "auto"
debug = True
proc_name = 'gunicorn_flask.proc'
pidfile = pidpath + "gunicorn.pid"
logfile = logpath + "debug.log"
loglevel = 'info'
