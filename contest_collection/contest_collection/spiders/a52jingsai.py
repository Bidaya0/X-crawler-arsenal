# -*- coding: utf-8 -*-
import scrapy


class A52jingsaiSpider(scrapy.Spider):
    name = '52jingsai'
    allowed_domains = ['52jingsai.com']
    start_urls = ['http://52jingsai.com/']

    def parse(self, response):
        pass
