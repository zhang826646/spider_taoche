# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class ScItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class ScItem(scrapy.Item):
    # define the fields for your item here like:
    c_title = scrapy.Field()   #车辆
    c_href=scrapy.Field()      #链接
    c_year=scrapy.Field()      #年份
    c_mileage=scrapy.Field()   #公里数
    c_city=scrapy.Field()     #城市
    c_score=scrapy.Field()    #价钱

    #二级
    c_pinpai=scrapy.Field()
    c_xinghao=scrapy.Field()
    c_suozaidi = scrapy.Field()
    c_fadongji = scrapy.Field()
    c_qudong = scrapy.Field()
    c_jibie = scrapy.Field()
    c_pailiang = scrapy.Field()
    c_youhao = scrapy.Field()
    c_chicun = scrapy.Field()
    c_leixing = scrapy.Field()
    c_hxrl = scrapy.Field()


