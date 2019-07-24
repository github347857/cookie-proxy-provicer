from multiprocessing import Process
from tools.api import app
from tools.setting import API_HOST,API_PORT

class Scheduler():
    def schedule_api(self):
        """
        开启API
        """
        print('API服务启动')
        app.run(API_HOST, API_PORT)

    def run(self):
        # 获取代理API接口
        api_process = Process(target=self.schedule_api)
        api_process.start()