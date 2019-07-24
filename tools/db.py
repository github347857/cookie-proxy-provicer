# 说明代理池表中各字段含义
# spiderName：爬虫名称
# keyValue：'X':表示该条cookie存储的是cookie的键值对,SPACE:表示存储的是拼接完整的cookie
# cookieName：cookie中的name值
# value：cookie中的value值，（keyValue=space 时表示一条完整的cookie）
# orgin:目标网站

# 数据库交互模块
from tools.setting import MONGO_USER,MONGO_PWD,MONGO_HOST,MONGO_DB
from urllib.parse import quote_plus
import pymongo
import random
# 代理池数据库连接
class MongoDBClient(object):

    def __init__(self):
        """
        初始化
        """
        self.client = pymongo.MongoClient(
            "mongodb://%s:%s@%s" % (quote_plus(MONGO_USER), quote_plus(MONGO_PWD), MONGO_HOST))
        self.mymongodb = self.client[MONGO_DB]


    # 代理随机获取功能
    def get_cookie(self,spiderName,keyValue=''):

        mypool = self.mymongodb['cookieProxyPool']
        myquery = {"spiderName": spiderName,'keyValue':keyValue}
        cookieList = mypool.find(myquery)
        list = []
        number = {}
        num = 0
        for co in cookieList:
            list.append(co)
            number[str(num)] = co['number']
            num = num + 1

        if list:
            # 随机返回一条cookie
            if not keyValue:
                num = random.randrange(0,len(list))
                return list[num].get('value')
            else:
                # 随机返回一套cookie的键值对
                num = random.randrange(0,len(number))
                key = number[str(num)]
                cookie={}
                for li in list:
                    if li['number'] == key:
                        cookie[li['cookieName']] = li['value']

                return cookie
        else:
            return 'NO'

    # 返回当前代理池存在的代理
    def get_all(self,spiderName=''):
        mypool = self.mymongodb['cookieProxyPool']
        myquery = {}
        if spiderName:
            myquery['spiderName'] = spiderName
        cookieList = mypool.find(myquery)

        if cookieList:

            cookList = []
            for co in cookieList:
                co.pop('_id')
                cookList.append(co)

            return cookList

        else:
            return '代理池枯竭'


if __name__ == '__main__':

    run = MongoDBClient()

    agent = run.get_cookie('11','')
    # agent = run.get_all()
    print(str(agent))


