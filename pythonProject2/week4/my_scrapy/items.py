# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PoetryItem(scrapy.Item):
    # # define the fields for your item here like:
    # # name = scrapy.Field()
    # pass
    poetrys = scrapy.Field()

class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    publish = scrapy.Field()
    score = scrapy.Field()
    selogen = scrapy.Field()

class JdItem(scrapy.Item):
    price= scrapy.Field()
    name = scrapy.Field()
    commit_num = scrapy.Field()
    key_word = scrapy.Field()
    sales = scrapy.Field()

class ResumeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    resumes = scrapy.Field()