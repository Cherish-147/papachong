import bs4
import scrapy
import requests
from ..items import blibliItem

class blibliSpider(scrapy.Spider):
    name = 'blibli'
    allowed_domains = ['blibli.com']
    start_urls = ['https://www.blibli.com/']

    def parse(self, response):
        bs =bs4.BeautifulSoup(response.text,'html.parser'
                        )
        datas = bs.find_all('div',class_='card-item')
        for data in datas:
            item = blibliItem
            item['video_title']= data.find('a',class_='video-card__content').text
            item['title']= data.find('p',class_='video-card__info').text
            item['up_name'] = data.find('span',class_='up-name__text').text
            item['playback'] = data.find('span',class_='play-text').text
            item['barrage'] = data.find('span',class_='line-text').text
            item['logo'] = data.find('span',class_='history-hint').text
        if data.find('span', class_='inq'):
            item['selogen'] = data.find('span', class_='inq').text
        else:
            item['selogen'] = ""
        print(item['title'] + ':' + item['selogen'])
        yield item