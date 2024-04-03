from tkinter import *
from my_scrapy.op_scrapy11 import Op_scrapy  # 导入自定义的 Op_scrapy 模块
import time


class My_tk():
    def __init__(self, tk):
        self.op_scrapy = Op_scrapy()  # 初始化 Op_scrapy 对象用于网页抓取
        # 界面基本设置
        self.root = tk
        self.root.title('我的scrapy 爬虫')  # 设置窗口标题
        self.root.geometry('300x300')  # 设置窗口的初始大小
        # 创建初始爬虫功能选择按钮
        self.choice_frame = Frame(self.root)
        self.poetry_button = Button(self.choice_frame, text='爬取古诗', command=self.show_poetry)
        self.choice_frame.pack()  # 将选择框架打包
        self.poetry_button.pack(side=LEFT)  # 将古诗按钮放置在左侧

    def show_poetry(self):
        # 隐藏选择页面，显示为爬取古诗的页面
        self.choice_frame.pack_forget()  # 隐藏选择框架
        self.build_poetry_frame()  # 构建古诗抓取页面

    def build_poetry_frame(self):
        # 古诗抓取页面
        self.poetry_frame = Frame(self.root, height=50, width=100)  # 创建一个新的框架用于古诗抓取
        self.poetry_frame.pack(anchor='center')  # 将古诗框架打包居中显示
        go_back_button = Button(self.poetry_frame, text='返回', command=self.back)  # 返回按钮
        go_back_button.pack(anchor='w')  # 将返回按钮放置在左侧
        self.go_spider_button = Button(self.poetry_frame, text='爬取故事', command=self.go_spider_poetry)
        self.go_spider_button.pack(anchor='center')  # 将爬虫按钮放置在中间
        self.spidering_info = Listbox(self.poetry_frame, width=30)  # 用于显示抓取信息的列表框
        self.spidering_info.pack(anchor='center')  # 将列表框打包居中显示

    def go_spider_poetry(self):
        # 开始进行古诗抓取的函数
        self.spidering_info.insert('end', '开始爬虫')  # 插入一条消息表示抓取开始
        self.show_running_info()  # 调用函数显示抓取过程中的运行信息
        op_result = self.op_scrapy.start('poetry')  # 开始抓取古诗
        if op_result == False:
            self.spidering_info.insert('end', '爬虫失败！')  # 插入一条消息表示抓取失败
        else:
            self.spidering_info.insert('end', '爬虫完成')  # 插入一条消息表示抓取完成

    def show_running_info(self):
        # 显示抓取过程中的运行信息的函数
        running = True
        time1 = int(time.time())
        self.spidering_info.insert('end', '爬虫中……')  # 插入一条消息表示抓取正在进行中
        while running:
            now_time = int(time.time() - time1)
            if now_time % 2 == 0:
                running = self.op_scrapy.check_scrapying()  # 检查抓取是否仍在运行中
        self.spidering_info.insert('end', '爬取数据完毕')  # 插入一条消息表示抓取完成

    def back(self):
        # 返回到上一个选择界面的函数
        if 'poetry_frame' in dir(self):
            self.poetry_frame.destroy()  # 销毁古诗框架（控件）
            delattr(self, 'poetry_frame')  # 删除古诗框架属性

        self.choice_frame.pack()  # 显示初始的选择框架
        print(self.op_scrapy.spider_pid)  # 打印爬虫进程ID
        self.op_scrapy.stop_scrapy()  # 停止抓取进程
