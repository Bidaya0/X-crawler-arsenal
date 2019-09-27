# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ContestCollectionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    anno_time = scrapy.Field()
    abstract = scrapy.Field()
    description = scrapy.Field()
    views = scrapy.Field()
    appendix = scrapy.Field()