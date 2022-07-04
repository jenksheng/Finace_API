"""
打印日志类代码封装
初始化日志配置
1、初始化日志对象
2、设置日志级别
3、创建控制台体制处理器和文件日志处理器
4、设置日志格式 创建格式化器
5、将格式化器设置到日志器中
6、将日志处理器添加到日志对象
"""
# 导包
import logging
from logging import handlers
import os
import app
import time
# 初始化日志配置
def init_log_config():
    pass
    #1、初始化日志对象
    logger = logging.getLogger()
    # 2、设置日志级别
    logger.setLevel(logging.INFO)
    # 3、创建控制台体制处理器和文件日志处理器
    sh = logging.StreamHandler()
    logfile = app.BASE_FILE + os.sep + "/log/log{}.log".format(time.strftime("%Y%m%d - %H%M%S"))
    # 设置请求的时间M  次数和一起执行的函数
    fh = logging.handlers.TimedRotatingFileHandler(logfile,when="M",interval=5,backupCount=5,encoding="utf-8")
    # 4、设置日志格式 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 5、将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 6、将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)

