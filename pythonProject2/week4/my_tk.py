import tkinter
from tkinter import *
import tkinter.filedialog
# from my_scrapy.op_scrapy11 import Op_scrapy  # 导入自定义的 Op_scrapy 模块
# from my_scrapy.op_scrapy import Op_scrapy  # 导入自定义的 Op_scrapy 模块
from op_scrapy import Op_scrapy  # 导入自定义的 Op_scrapy 模块
import time, threading


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
        self.douban_button = Button(self.choice_frame, text='爬取豆瓣', command=self.show_douban)
        self.douban_button.pack(side=LEFT)
        self.jd_button = Button(self.choice_frame, text='爬取京东', command=self.show_jd)
        self.jd_button.pack(side=LEFT)
        with open('jd_status.txt', 'w') as f:
            f.write('0')

    def show_poetry(self):
        # 隐藏选择页面，显示为爬取古诗的页面
        # self.Tid = False
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
        self.the_running_info = threading.Thread(target=self.show_running_info)
        self.the_running_info.start()
        op_result = self.op_scrapy.start('poetry')  # 开始抓取古诗
        if op_result == False:
            self.spidering_info.insert('end', '爬虫失败！')  # 插入一条消息表示抓取失败
        # else:
        #     self.spidering_info.insert('end', '爬虫完成')  # 插入一条消息表示抓取完成

    def show_douban(self):
        # 隐藏【选择】界面，显示为爬取【获取古诗】界面
        # self.Tid = False
        self.choice_frame.pack_forget()  # 隐藏选择框架
        self.build_douban_frame()

    def build_douban_frame(self):
        # 豆瓣页面
        self.douban_frame = Frame(self.root, height=50, width=100)  # 创建一个新的框架用于古诗抓取
        self.douban_frame.pack(anchor='center')  # 将古诗框架打包居中显示
        go_back_button = Button(self.douban_frame, text='返回', command=self.back)  # 返回按钮
        go_back_button.pack(anchor='w')  # 将返回按钮放置在左侧
        self.go_spider_button = Button(self.douban_frame, text='豆瓣读书TOP', command=self.go_spider_douban)

        self.go_spider_button.pack(anchor='center')  # 将爬虫按钮放置在中间
        self.spidering_info = Listbox(self.douban_frame, width=30)  # 用于显示抓取信息的列表框
        self.spidering_info.pack(anchor='center')  # 将列表框打包居中显示

    def go_spider_douban(self):
        # 开始进行豆瓣网页抓取的函数
        self.spidering_info.insert('end', '开始爬虫')  # 插入一条消息表示抓取开始
        self.go_spider_button.config(state=tkinter.DISABLED)
        self.the_running_info = threading.Thread(target=self.show_running_info)
        self.the_running_info.start()
        op_result = self.op_scrapy.start('douban')
        if op_result == False:
            self.spidering_info.insert('end', '爬虫方案有误')
            # 插入一条消息表示抓取失败

    def show_jd(self):
        # 隐藏选择界面，显示为爬取获取京东界面
        # self.Tid =Flase
        self.choice_frame.pack_forget()
        self.build_jd_frame()

    def build_jd_frame(self):
        # 京东界面
        self.jd_frame = Frame(self.root, height=50, width=100)
        self.jd_frame.pack(anchor='center')
        go_back_button = Button(self.jd_frame, text='返回', command=self.back)
        go_back_button.pack(anchor='w')
        self.go_spider_button = Button(self.jd_frame, text='京东商品数据', command=self.go_spider_jd)
        self.go_spider_button.pack(anchor='center')
        self.go_jd_login = Button(self.jd_frame, text='浏览器已确认登录后，点击', command=self.update_jd_login_status)
        self.go_jd_login.pack(anchor='center')
        self.spidering_info = Listbox(self.jd_frame, width=30)
        self.spidering_info.pack(anchor='center')
        self.go_jd_login.config(state=tkinter.DISABLED)

    def go_spider_jd(self):
        # 京东爬虫
        self.spidering_info.insert('end', '开始爬取京东商品数据……')
        self.go_spider_button.config(state=tkinter.DISABLED)
        self.the_running_info = threading.Thread(target=self.show_running_info)
        self.the_running_info.start()
        op_result = self.op_scrapy.start('jd')
        self.go_jd_login.config(state=tkinter.NORMAL)
        if op_result == False:
            self.spidering_info.insert('end', '爬虫方案有误！！')

    def update_jd_login_status(self):
        self.spidering_info.insert('end', '浏览器已确认登录，爬虫继续……')
        with open('jd_status.txt', 'w') as f:
            f.write('1')

    def show_running_info(self):
        # 显示抓取过程中的运行信息的函数
        running = True
        time1 = int(time.time())
        self.spidering_info.insert('end', '爬虫中……')  # 插入一条消息表示抓取正在进行中
        self.spidering_info.insert('end', '爬虫线程id：' + str(self.op_scrapy.spider_pid))
        self.spidering_info.insert('end', '爬虫线程运行中')
        while running:
            now_time = int(time.time() - time1)
            if now_time % 2 == 0:
                if self.op_scrapy.spider_pid != 123456:
                    running = self.op_scrapy.check_scrapying()  # 检查抓取是否仍在运行中
        self.spidering_info.insert('end', '爬虫线程关闭')  # 插入一条消息表示抓取完成
        self.go_spider_button.config(state=tkinter.NORMAL)
        if 'jd frame' in dir(self):
            self.go_jd_login.config(state=tkinter.DISABLED)

    def back(self):
        # 返回到上一个选择界面的函数
        if 'poetry_frame' in dir(self):
            self.poetry_frame.destroy()  # 销毁古诗框架（控件）
            delattr(self, 'poetry_frame')  # 删除古诗框架属性
        elif 'douban_frame' in dir(self):
            self.douban_frame.destroy()
            delattr(self, 'douban_frame')
        elif 'jd_frame' in dir(self):
            self.jd_frame.destroy()
            delattr(self, 'jd_frame')

        self.choice_frame.pack()  # 显示初始的选择框架
        print(self.op_scrapy.spider_pid)  # 打印爬虫进程ID
        self.op_scrapy.stop_scrapy()  # 停止抓取进程
