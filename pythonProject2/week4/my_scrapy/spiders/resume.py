import scrapy  # 导入Scrapy库
from bs4 import BeautifulSoup  # 导入BeautifulSoup库
from ..items import ResumeItem  # 导入自定义的ResumeItem类


# 定义一个名为resumeSpider的爬虫类，继承自Scrapy的Spider类
class resumeSpider(scrapy.Spider):
    name = "resume_spider"  # 设置爬虫名称
    start_urls = ['http://127.0.0.1:9001/resume']  # 初始爬取的URL列表

    def parse(self, response):  # 定义解析方法，处理响应的HTML内容
        html = response.text  # 获取网页内容的文本形式
        soup = BeautifulSoup(html, 'html.parser')  # 使用BeautifulSoup解析HTML内容
        contents = soup.find_all('td')  # 查找所有class为'resume'的元素
        print(contents)
        print('-------------------------------')
        get_html_resumes = ''  # 初始化一个变量来存储简历信息的HTML内容
        for value in contents:  # 遍历找到的所有简历元素
            # print(value.text+"\n")
            # print(value.find('h2').text + "\n" )
            get_html_resumes += value.text+"\n"
            # get_html_resumes += value.find('h2').text + "\n"  # 获取简历标题并添加到变量中
            # get_html_resumes += value.find('td').text + "\n"  # 获取简历内容段落并添加到变量中
        print('get_html_resumes',get_html_resumes)  # 打印获取到的简历信息（可以改为存储到文件或数据库）
        item = ResumeItem()  # 创建一个ResumeItem对象
        item['resumes'] = get_html_resumes  # 将简历信息存储到ResumeItem对象中的'resumes'字段
        yield item  # 使用yield语句将ResumeItem对象传递给引擎处理
