import scrapy
from Test.items import TestItem
import re

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://www.neu.edu.cn']

    def parse(self, response):
        item = TestItem()
        #  "src": "/_upload/article/images/21/bb/b1d12d144ea0b1fc844b79131c70/6b2c1b61-8e9f-4c11-bf7c-fdf525e8627d.jpg"
        item["image_urls"] = re.findall(r'\"src\":\s\"(.*[jpg|png])\"', response.text)
        return item
