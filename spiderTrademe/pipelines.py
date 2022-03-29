# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class SpidertrademePipeline:
    # 抓取的数据存储在同目录下的data.csv文件中
    f = open('data.csv', 'w', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(['名字', '品牌', '型号', '出厂时间', '里程数', '售价'])
    def process_item(self, item, spider):
        self.writer.writerow([item['name'], item['make'], item['model'], item['F_time'], item['Odometer'], item['price']])
        return item
