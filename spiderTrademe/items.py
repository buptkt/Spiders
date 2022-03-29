# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidertrademeItem(scrapy.Item):
    # 车的名字
    name = scrapy.Field()
    # 品牌，厂商
    make = scrapy.Field()
    # 车型号
    model = scrapy.Field()
    # 出厂时间
    F_time = scrapy.Field()
    # 里程数
    Odometer = scrapy.Field()
    # 价格
    price = scrapy.Field()
    pass

