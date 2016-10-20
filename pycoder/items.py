# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PycoderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    status = scrapy.Field()
    visit = scrapy.Field()
    vgoal = scrapy.Field()
    hgoal = scrapy.Field()
    home = scrapy.Field()
    pass
