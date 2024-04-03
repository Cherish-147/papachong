# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
import pandas as pd



class MyScrapyPipeline:
    def __init__(self):
        self.count = 0
        self.df = pd.DataFrame(columns=['video_cards', 'title', 'up_name', 'plackback', 'barrage', 'logo'])
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='scrapy_test',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()
        self.count = 1

    def process_item(self, item, spider):
        if spider.name == 'bilibili':
            df_cell = pd.DataFrame({

                'video_cards': [item['video_cards']],
                'title': [item['title']],
                'up_name': [item['up_name']],
                'plackback': [item['plackback']],
                'barrage': [item['barrage'],
                'logo' :  [item['logo']],
                charset='utf8',
                self.count += 1
                self.df = pd.concat([self.df, df_cell], ignore_index=True)
                sql = '''insert into douban_top(title,publish,score,selogn,source,type)
                                        values(%s,%s,%s,%s,%s,%s)'''
                self.cursor.execute(sql, (
                    item.get('video_cards', ''),
                    item.get('title', ''),
                    item.get('up_name', ''),
                    item.get('plackback', ''),
                    item.get('barrage', ''),
                    item.get('logo', ''),
                    'bilibili',
                    '入站必刷'
                ))
                self.conn.commit()

    def close_spider(self, spider):
            # 爬取豆瓣时，将数据保存到excel中
        if spider.name == 'douban_spider':
            self.df.to_excel('douban_top.xlsx', index=False)
            self.cursor.close()
            self.conn.close()
