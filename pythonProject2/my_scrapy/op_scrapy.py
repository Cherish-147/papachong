import time, psutil, subprocess, multiprocessing  # 导入库和模块
from scrapy.crawler import CrawlerProcess  # 导入Scrapy框架中的CrawlerProcess
from scrapy.utils.project import get_project_settings  # 导入Scrapy框架中的get_project_settings
from my_scrapy.spiders.poetry import poetrySpider  # 导入自定义的诗歌爬虫
from my_scrapy.spiders.resume import resumeSpider

class Op_scrapy():  # 定义一个类Op_scrapy
    def __init__(self):
        self.spider_pid = 123456  # 初始化爬虫进程的 PID


    def start(self, spider_name):   # 定义启动爬虫的方法start
        if spider_name == 'poetry':  # 如果爬虫名为'poetry'
            spider = poetrySpider  # 设置爬虫为诗歌爬虫
        elif spider_name =='resume':
            spider = resumeSpider
        else:
            return  # 其他情况下返回
        self.the_scrapy = multiprocessing.Process(target=start_crawl, args=(spider,))  # 创建多进程实例，目标为start_crawl方法
        self.the_scrapy.start()  # 启动多进程
        self.spider_pid = self.the_scrapy.pid  # 获取启动的爬虫进程的PID


    # ================如果scrapy还在运行，那么杀死进程================
    def stop_scrapy(self):  # 定义停止爬虫的方法stop_scrapy
        #根据pid判断，如果scrapy还在运行，那么结束进程，
        #同时设定爬取详情窗口的is_scrapying为Flash种植tree里的循环'''
        if self.spider_pid in psutil.pids():  # main.py的继承类定义了改id，运行爬虫时设定 # 如果爬虫进程仍在运行
            print('scrapy还在运行！')  # 输出提示信息
            time.sleep(1)  # 等待1秒
            subprocess.Popen("taskkill /pid %s /f" % self.spider_pid, shell=True)  # 使用subprocess结束爬虫进程
    # ================如果scrapy还在运行，那么杀死进程================


    def check_scrapying(self):  # 定义检查爬虫状态的方法check_scrapying
        if self.spider_pid in psutil.pids():   # 检查爬虫进程是否在运行
            return True  # 如果在运行，返回True
        else:
            return False  # 如果不在运行，返回False


def start_crawl(spider):# 启动爬虫的函数
    process = CrawlerProcess(get_project_settings())  # 创建一个爬虫进程
    process.crawl(spider)  # 启动指定的爬虫
    process.start()  # 开始爬取过程