import scrapy
import json
from Trademe.spiderTrademe.items import SpidertrademeItem

class TrademeSpider(scrapy.Spider):
    name = 'spiderTrademe'
    allowed_domains = ['trademe.co.nz']
    # start_urls = ['https://api.trademe.co.nz/v1/search/general.json?make=BMW&auto_category_jump=false&rows=10000&return_canonical=true&return_metadata=true&return_ads=true&return_empty_categories=true&return_super_features=true&return_did_you_mean=true&canonical_path=/motors/cars&return_variants=true&snap_parameters=true']
    start_urls = ['https://api.trademe.co.nz/v1/search/general.json']
    page = 1

    # 每次请求先构造好参数，page递增
    def formRequests(self):
        params = {
            'page': str(self.page),
            'rows': '500',
            'return_canonical': 'true',
            'return_metadata': 'true',
            'return_ads': 'true',
            'return_empty_categories': 'true',
            'return_super_features': 'true',
            'return_did_you_mean': 'true',
            'canonical_path': '/motors/cars',
            'return_variants': 'true',
            'snap_parameters': 'true'
        }
        # 拼接URL
        url = self.start_urls[0] + "?"
        for key in params.keys():
            url += f'{key}={params[key]}&'
        url.strip('&')
        self.page += 1
        return url

    def start_requests(self):
        yield scrapy.Request(url=self.formRequests(), callback=self.parse, dont_filter=True)

    def parse(self, response):
        data = json.loads(response.text)['List']
        # 将对应数据传给item
        for each in data:
            item = SpidertrademeItem()
            item['name'] = each['Title']
            item['make'] = each['Make']
            item['model'] = each['Model']
            item['F_time'] = each['Year']
            item['Odometer'] = each['Odometer']
            item['price'] = each['StartPrice']
            yield item
        yield scrapy.Request(url=self.formRequests(), callback=self.parse, dont_filter=True)
