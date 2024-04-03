import pymysql
import pandas as pd


class MyScrapyPipeline:
    def __init__(self):
        self.count = 0
        self.df = pd.DataFrame(columns=['index', 'title', 'publish', 'score', 'selogen', 'source', 'type'])
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
        # 针对不同的爬虫进行不同的保存处理，对应spiders/poetry.py 的name
        if spider.name == 'poetry_spider':  # 如果是诗歌爬虫
            with open('poetrys.text', 'w', encoding='utf-8') as f:  # 以追加模式打开文件
                f.write(item['poetrys'])  # 将诗歌内容写入文件
        elif spider.name == 'douban_spider':
            # 将数据编辑成excel数据格式
            df_cell = pd.DataFrame({
                'index': [self.count],
                'title': [item.get('title', '')],
                'publish': [item.get('publish', '')],
                'score': [item.get('score', '')],
                'selogen': [item.get('selogen', '')],
                'source': ['豆瓣读书'],
                'type': ['Top250']
            })
            self.count += 1
            self.df = pd.concat([self.df, df_cell], ignore_index=True)

            # 保存到数据库
            sql = '''insert into douban_top(title,publish,score,selogn,source,type)
                    values(%s,%s,%s,%s,%s,%s)'''
            self.cursor.execute(sql, (
                item.get('title', ''),
                item.get('publish', ''),
                item.get('score', ''),
                item.get('selogen', ''),
                '豆瓣读书',
                'Top250'
            ))
            self.conn.commit()
        elif spider.name == 'jd_spider':
            sql = '''insert into jd_goods(name,price,commit_num,key_word,sales)
                    values(%s,%s,%s,%s,%s,%s)'''
            self.cursor.execute(sql, (
                item.get('name', ''),
                item.get('price', ''),
                item.get('commit_num', ''),
                item.get('key_word', ''),
                item.get('sales', '')
            ))
            self.conn.commit()
        return item

    def close_spider(self, spider):
        # 爬取豆瓣时，将数据保存到excel中
        if spider.name == 'douban_spider':
            self.df.to_excel('douban_top.xlsx', index=False)
            self.cursor.close()
            self.conn.close()
