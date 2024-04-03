# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyScrapyPipeline:
    def process_item(self, item, spider):
        # 针对不同的爬虫进行不同的保存处理，对应spiders/poetry.py 的name
        if spider.name == 'poetry_spider': # 如果是诗歌爬虫
            with open('poetrys.text','w',encoding='utf-8') as f: # 以追加模式打开文件
                f.write(item['poetrys'])  # 将诗歌内容写入文件
        elif spider.name == 'resume_spider':
            with open('resumes.text', 'w', encoding='utf-8') as f:
                f.write(item['resumes'])
