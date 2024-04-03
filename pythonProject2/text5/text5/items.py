# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Text5Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class blibliItem(scrapy.Item):

    video_cards = scrapy.Field()

    title = scrapy.Field()

    up_name = scrapy.Field()

    playback = scrapy.Field()

    barrage= scrapy.Field()

    logo= scrapy.Field()
