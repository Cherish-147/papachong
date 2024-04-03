import tkinter
from  tkinter import *
import tkinter.filedialog
from op_scrapy import Op_scrapy
import time,threading

class My_tk():
    def __init__(self,tk):
        self.op_scrapy = Op_scrapy()

        self.root = tk
        self.root.title('爬虫程序')
        self.root.geometry('500x300')
        self.choice_frame = Frame(self.root)
        self.blibli_button = Button(self.choice_frame,text='爬取B站',command=self.show_blibli)
        self.choice_frame.pack()
        self.blibli_button.pack(side=LEFT)
        with open('blibli.txt','w') as f:
            f.write('爬取B站')

    def show_blibli(self):
        self.choice_frame.pack_forget()
        self.build_blibli_frame()

    def build_blibli_frame(self):
        self.blibli_frame = Frame(self.root,height=50,width=100)
        self.blibli_frame.pack(anchor='center')
        go_back_button = Label(self.blibli_frame,text='请选择爬取的B站分区：',command=self.show_blibli_choice)
        go_back_button.pack(anchor='w')
        self.go_spider_button= Button(self.blibli_frame,text='开始爬取',command=self.start_spider)
        self.go_spider_button.pack(anchor='center')
        self.spidering_info = Listbox(self.blibli_frame, width=30)
        self.spidering_info.pack(anchor='center')

    def go_spider_blibli(self):
        self.spidering_info.delete(0,END)
        self.spidering_info.insert(END,'开始爬取')
        self.the_running_info = threading.Thread( target==self.show_running_info)
        self.the_running_info.start()
        op_result = self.op_scrapy.start('blibli')


    def show_blibli_choice(self):
        self.blibli_frame.pack_forget()
        self.blibli_choice_frame = Frame(self.root,height=50,width=100)

    def back(self):
        if 'blibli_frame'in dir(self):
            self.blibli_frame.destroy()
            delattr(self,'blibli_frame')
        self.choice_frame.pack()  # 显示初始的选择框架
        print(self.op_scrapy.spider_pid)  # 打印爬虫进程ID
        self.op_scrapy.stop_scrapy()
