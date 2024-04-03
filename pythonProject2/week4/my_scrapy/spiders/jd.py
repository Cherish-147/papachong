import bs4
import scrapy
from ..items import JdItem
from selenium import webdriver
import time
from loguru import logger
from selenium.webdriver.chrome.service import Service


class JdSpider(scrapy.Spider):
    name = 'jd_spider'
    allowed_domains = ['www.jd.com']
    key_word = 'python'
    start_urls = ['https://search.jd.com/Search?keyword=' + key_word + '&page=1']

    # name = 'jd_spider'
    # allowed_domains = ['www.jd.com']
    # key_word='python'
    # start_urls=['https://search.jd.com/Search?keyword=' + key_word +'&page=1' ]

    def __init__(self):
        service = Service(executable_path='F:\chromedriver\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        # selenium4.6以上版本采用以下写法，本机电脑中需要安装谷歌浏览器


    def login(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        logger.info('等待登录状态确认……')
        # while True:
        #     time.sleep(5)
        #     with open('jd_status.txt', 'r') as f:
        #         content = f.read()
        #     if content == '1':
        #         break
        logger.info('登录状态确认成功！爬虫继续执行')
        with open('jd_status.txt', 'w') as f:
            f.write('0')


    def parse(self, response):
        response = str(response).split(' ')[1].replace('>', "")
        self.login(response)
        page_num = 1
        for i in range(2):
            time.sleep(2)
            self.driver.get('https://search.jd.com/Search?keyword=' +
                            JdSpider.key_word + '&page=' + str(page_num))
            page_num += 2
            html = self.driver.page_source
            soup = bs4.BeautifulSoup(html, 'html.paser')
            ul_element = soup.find('ul', class_='gl-warp clearfix')
            li_elements = ul_element.find_all('li')
            for li_item in li_elements:
                item = JdItem()
                name_link_div = li_item.find('div', {'class': 'p-name p-name-type-2'})
                name = name_link_div.find('a').find('em').text
                item['name'] = name
                price_div = li_item.find('div', {'class': 'p-price'})
                price = price_div.find('strong').find('i').text
                item['price'] = price
                commit_div = li_item.find('div', {'class': 'p-commit'})
                commit_num = commit_div.find('strong').find('a').text
                item['commit_num'] = commit_num
                item['key_word'] = JdSpider.key_word
                item['sales'] = '京东'
                yield item

#
def close(self,spider,reason):
    self.driver.quit()
    logger.info('爬虫结束')
