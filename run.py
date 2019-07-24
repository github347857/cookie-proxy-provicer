# cookie代理池第一版
# 提供cookie获取API，基础cookie需要手动维护进数据库
#以爬虫的名字来区分，字段详细说明查看db.py文件

import sys
import io
from tools.scheduler import Scheduler
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()

if __name__ == '__main__':
    main()