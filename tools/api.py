# API接口模块
from flask import Flask, g,request
from tools.db import MongoDBClient
import json
__all__ = ['app']
app = Flask(__name__)

# 连接数据库

@app.route('/')
def index():
    return '<p>Welcome to Cookie Proxy Pool System </p>' \
           '<p>/cookie  随机返回一个cookie  参数：name：爬虫名，key:cookie是否是键值对（默认空为完整一条cookie）   </p>' \
           '<p>/all     返回代理池中所有的cookie信息  </p>'

# 获取代理
@app.route('/cookie', methods = ['get'])
def get_proxy():
    reqValue = request.values
    # 链接传回的参数
    para={}
    for i in reqValue:
        # i = eval(i)  # 百度str 怎么转成dic ,有两种方法，eval()和exec()函数实现
        para[i] = i

    if not para:

        return 'NO'

    try:
        para.pop('name')
    except:
        pass
    try:
        para.pop('key')
    except:
        pass

    if para:
        return 'NO'


    spiderName = request.values.get('name')
    keyValue = ''
    if request.values.get('key'):
        keyValue = request.values.get('key')
    conn = MongoDBClient()
    agent = conn.get_cookie(spiderName = spiderName,keyValue = keyValue)
    if keyValue:
        return json.dumps(agent,ensure_ascii=False)
    else:
        return agent

@app.route('/all', methods=['get'])
def get_all():
    spiderName = request.values.get('key')
    print(spiderName)
    conn = MongoDBClient()
    agent = conn.get_all()
    return json.dumps(agent,ensure_ascii=False)
