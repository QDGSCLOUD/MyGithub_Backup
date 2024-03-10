# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CheckipdomainItem(scrapy.Item):
    entrepreneur =  scrapy.Field()
    enterprise_nature =  scrapy.Field()
    ICP  =  scrapy.Field()
    address =  scrapy.Field()
    property = scrapy.Field()
    industry_service =  scrapy.Field()
    repsent_people =  scrapy.Field()

