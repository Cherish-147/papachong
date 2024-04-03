import bs4
import scrapy
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ['book.douban.com']
    # 第一贝
    # https://book.douban.com/top250?start=日
    # 第二页
    # https://book.douban.con/top250?start=25
    # 产第三页
    # https://book.douban.com/top250?start=50
    start_urls = []
    for x in range(10):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    # def parse(self, response):
    #     # Create a BeautifulSoup object using the response text and the 'html.parser' format
    #     bs = bs4.BeautifulSoup(response.text, 'html.parser')
    #     # Find all 'tr' tags with the class 'item'
    #     datas = bs.find_all('tr', class_="item")
    #     # Loop through each 'tr' tag
    #     for data in datas:
    #         # Create a new DoubanItem object
    #         item = DoubanItem()
    #         # Find the title of the book from the 'a' tag
    #         item['title'] = data.find_all('a')[1]['title']
    #         # Find the publish date of the book from the 'p' tag with the class 'pl'
    #         item['publish'] = data.find('p', class_='pl').text
    #         # Find the score of the book from the 'span' tag with the class 'rating_nums'
    #         item['score'] = data.find('span', class_='rating_nums').text
    #         # Check if the book has a selenium quote
    #         if data.find('span', class_='inq'):
    #             # If it does, find the selenium quote from the 'span' tag with the class 'inq'
    #             item['selogen'] = data.find('span', class_='inq').text
    #         else:
    #             # If it doesn't, set the selenium quote to an empty string
    #             item['selogen'] =""
    #         # Print the title and selenium quote
    #         print(item['title']+':' + item['selogen'])
    #         # Yield the DoubanItem object
    #         yield item


        def parse(self, response):
            # 创建一个BeautifulSoup对象，使用response文本和'html.parser'格式
            bs = bs4.BeautifulSoup(response.text, 'html.parser')
            # 查找所有class为'item'的'tr'标签
            datas = bs.find_all('tr', class_="item")
            # 遍历每个'tr'标签
            for data in datas:
                # 创建一个新的DoubanItem对象
                item = DoubanItem()
                # 从'a'标签中查找书名
                item['title'] = data.find_all('a')[1]['title']
                # 从'p'标签中查找出版日期
                item['publish'] = data.find('p', class_='pl').text
                # 从'span'标签中查找评分
                item['score'] = data.find('span', class_='rating_nums').text
                # 检查该书是否有selenium注释
                if data.find('span', class_='inq'):
                    # 如果有的话，从'span'标签中查找selenium注释
                    item['selogen'] = data.find('span', class_='inq').text
                else:
                    # 如果没有，设置selenium注释为空字符串
                    item['selogen'] = ""
                # 打印书名和selenium注释
                print(item['title'] + ':' + item['selogen'])
                # 返回DoubanItem对象
                yield item
