# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#class DailyWikiItem(scrapy.Item):

# Data type that can hold on pieces information when you actually read from Spider
class Article(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
