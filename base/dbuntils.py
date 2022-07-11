"""
封装数据的方法
"""
# 导包
import pymysql

# 定义类
class DButils:
    # 初始化函数
    def __init__(self):
        self.conn = None

    # 建立连接
    def __get_conn(self):
        conn = pymysql.connect(
            host="",
            user="",
            password="",
            database="",
            autocommit=True

        )
        return conn
    # 获取游标
    def __get_cursor(self):
        # 获取游标
        cursor = self.__get_conn().cursor()
        return cursor
    # 执行sql
    def exe_sql(self):
        pass
    # 关闭游标
    def __close_cuesor(self):
        self.__get_cursor().close()
    # 关闭连接
    def __colse_conn(self):
        self.__get_conn().close()