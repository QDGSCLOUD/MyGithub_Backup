# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    score = scrapy.Field()
    num = scrapy.Field()
    href = scrapy.Field()
    director = scrapy.Field()
    protagonist = scrapy.Field()
    alias = scrapy.Field()
    pass
