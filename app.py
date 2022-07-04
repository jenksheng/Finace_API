# 导包
import os
import random
import logging
# 获取文件地址
BASE_FILE = os.path.dirname(os.path.abspath(__file__))

# 定义URL
BASE_URL = "http://user-p2p-test.itheima.net"

# 随机获取3为英文字母
a = random.sample("asdfasfa",3)
b = "".join(a)
logging.info(b)
print(b)
