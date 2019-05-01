# gunicorn flask
gunicorn部署flask实现多并发wab api

## 主要环境
python: 3.6.5
gunicorn: 19.9.0
flask: 1.0.2

## 服务启动
通过 service_run 启动：./service_run start
参数说明：
[start|stop|restart|reload|status|version]
start: 启动
stop: 停止
restart: 重启
reload: 重载
status: 状态
version: 版本

## 调用服务
    curl -H "Content-type: application/json" -X POST http://host:port/apirun/judge -d '{"a": 1, "b": 2}'
返回：
    {"ret": {"api_ret": {"a": 1, "b": 2}, "TimeC": 0.0012149810791015625}}

## 附（定时加载）
对于需要处理较大数据时，可以采用预加载的方式将数据先加载到内存中，flask提供APScheduler实现
    # 每隔1小时加载一次
    class Config(object):
        JOBS=[
            {
                'id':'job1',
                'func':'api_flask:job',
                'trigger':'interval',
                'seconds':3600
            }
        ]
        SCHEDULER_API_ENABLED = True

    def Preloading():
        """
        每次启动时对content进行一次加载
        """
        content = fun()
        return content
    content = Preloading()

    def job():
        """
        定时处理的任务
        """
        global content
        content = fun()
        # print (content)

    app.config.from_object(Config())  # 为实例化的flask引入配置
    scheduler=APScheduler()  # 实例化APScheduler
    scheduler.init_app(app)  # 把任务列表放进flask
    scheduler.start()  # 启动任务列表
在api 中直接使用全局变量content即可
