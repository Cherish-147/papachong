import time, psutil, subprocess, multiprocessing  # 导入库和模块
from scrapy.crawler import CrawlerProcess  # 导入Scrapy框架中的CrawlerProcess
from scrapy.utils.project import get_project_settings  # 导入Scrapy框架中的get_project_settings
from text5.spiders.blibili import blibliSpider

class Op_scrapy():
    def __init__(self):
        self.spider_pid = 123456

    def start(self,spider_name):
        if spider_name == 'blibli':
            spider = blibliSpider
        else:
            return False
        self.the_scrapy = multiprocessing.Process(target=start_crawl, args=(spider,))
        self.the_scrapy.start()
        self.spider_pid=self.the_scrapy.pid
        return True
    def stop_scrapy(self):
        if self.spider_pid in psutil.pids():
            print('scrapy还在运行！')
            time.sleep(1)
            subprocess.Popen('taskkill/pid %d /f')% self.spider_pid,shell=True)


    def check_scrapying(self):
            if self.spider_pid in psutil.pids():
                return True
            else:
                return False
def start_crawl(spider):  # 启动爬虫的函数
    process = CrawlerProcess(get_project_settings())  # 创建一个爬虫进程
    process.crawl(spider)  # 启动指定的爬虫
    process.start()  # 开始爬取过程