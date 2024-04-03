import scrapy  #导入scrapy
from bs4 import BeautifulSoup  #从bs4模块导入BeautifulSoup类
from ..items import PoetryItem

class poetrySpider(scrapy.Spider):  #定义名为poetrySpider的类，同时该类继承scrapy.Spider类
    name = "poetry_spider"  #用name指代字符串poetry_spider

    start_urls = ['http://127.0.0.1:9000']  #爬虫开始爬取的url地址  #start_urls = ['http://127.0.0.1:9000/resume']

    def parse(self, response):  #定义名为parse的方法，当Scrapy下载完一个页面并生成一个response对象会调用这个方法，response包含页面内容
        html = response.text  #将response对象中的内容用html指代
        soup = BeautifulSoup(html,'html.parser')  #利用BeautifulSoup的构造函数将html解析为soup，使用html.parser作为解析器
        contents = soup.findAll(class_='view_text')  #利用BeautifulSoup的findAll方法查找class属性值为view_text的内容，并用contents指代  #contents = soup.findAll(class_='resume')
        get_html_poetrys = ''  #设置名为get_html_poetrys的空字符串
        for value in contents:
            get_html_poetrys += value.find('h2').text + "\n"
            get_html_poetrys += value.find('p').text + "\n"
        print('get_html_poetrys',get_html_poetrys)
        item = PoetryItem()  #创建一个PoetryItem对象，用item指代
        item['poetrys'] = get_html_poetrys  #将get_html_poetrys的内容赋予item的poetrys字段
        yield item  #使用yield关键字返回item对象
