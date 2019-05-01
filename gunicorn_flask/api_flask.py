# -*-coding:utf-8-*-
"""
api flask
author @boole
date 2019-05-01
"""


import datetime
import logging
import time
import json
from flask import Flask
from flask import request
from load_conf import read_conf
from handle.handle_action import handle_func

host = read_conf("dev", "host")
port = read_conf("dev", "port")
logpath = read_conf("dev", "logpath")

# 日志配置
dt = datetime.date.today().strftime("%Y%m%d")
logging.basicConfig(level=logging.DEBUG,
                    filename=logpath + 'api_run.log.' + dt,
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s | %(levelname)s | %(lineno)d | %(module)s | %(message)s')
logger = logging.getLogger(__name__)


app = Flask(__name__)  # 实例化flask


# post
@app.route('/apirun/judge', methods=['POST'])
def api_message():
    """
    api message application
    """
    startTime = time.time()
    dat = {}
    result = {}
    if request.headers['Content-Type'] == 'application/json':
        try:
            quest = json.dumps(request.json)
            dat = json.loads(quest)
        except Exception as e:
            msg = "The request is not legal, detail is %s" % str(e)
            logger.error(msg)
        # 对数据进行处理
        if dat != {}:
            result = handle_func(dat)
            msg = "success"
        else:
            msg = "dat is null"
    else:
        msg = "request unsupported"
        logger.error(msg)

    endTime = time.time()
    timeConsum = endTime - startTime
    ret = {"ret": {"api_ret": result, "TimeC": timeConsum}}
    logger.info({"ret": ret, "msg": msg})
    return json.dumps(ret)


if __name__ == '__main__':
    """
    example:
    curl -H "Content-type: application/json" -X POST http://host:port/apirun/judge -d '{}'
    """
    app.run(host=host, port=int(port), debug=True)

