# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from SC.items import ScItem

class TaocheSpider(scrapy.Spider):
    name = 'taoche'
    allowed_domains = ['taoche.com']
    start_urls = ['https://beijing.taoche.com/jeep/']


    # with open(r'C:\Users\Administrator\SC\city_list.txt', 'r') as fp:
    #     city_list = fp.readlines()
    #
    # with open(r'C:\Users\Administrator\SC\pinpai_list.txt', 'r') as fp:
    #     pinpai_list = fp.readlines()
    #
    # city_list = list(set(city_list))
    # pinpai_list = list(set(pinpai_list))
    #
    # for pinpai in pinpai_list:
    #     for city in city_list:
    #         url = 'https://{}.taoche.com{}'.format(city.strip(), pinpai.strip())
    #         start_urls.append(url)
    def vlist(self,list):
        if len(list)==0:
            return ''
        else:
            return list[0]

    def parse(self, response):
        total_page=response.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()').extract()
        total=self.vlist(total_page)
        total=int(total) if total else 0
        for page in range(1,total+1,1):
            persent_page_url=response.url+'?page='+str(page)
            yield scrapy.Request(url=persent_page_url,callback=self.list_parse)


    def list_parse(self,response):
        car_list=response.xpath('//ul[@class="gongge_ul"]/li')
        for car in car_list:
            c_title=car.xpath('./div[@class="gongge_main"]/a/span/text()').extract()[0]
            c_href=car.xpath('.//div[@class="gongge_main"]/a/@href').extract()[0]
            c_year = car.xpath('.//div[@class="gongge_main"]/p/i[1]/text()').extract()[0]
            c_mileage = car.xpath('.//div[@class="gongge_main"]/p/i[2]/text()').extract()[0]
            # c_city = car.xpath('.//div[@class="gongge_main"]/p/i[3]/text()').extract()[0]
            c_score = car.xpath('.//div[@class="gongge_main"]/div[@class="price"]/i[@class="Total brand_col"]/text()').extract()[0]
            c_y_score = car.xpath('.//div[@class="gongge_main"]/div[@class="price"]/i[@class="onepaynor"]/text()').extract()[0]
            # print(c_title,c_year,c_mileage.strip(),c_score,c_y_score)
            url=urljoin('http:',c_href)
            item=ScItem()
            item['c_title']=c_title
            item['c_href'] = url
            item['c_year'] = c_year
            item['c_mileage'] = c_mileage
            # item['c_city'] = c_city
            item['c_score'] = c_score
            yield scrapy.Request(url=url,callback=self.detail_parse,meta={'item':item})
 
    #二级页面
    def detail_parse(self,response):
        #获取item模型
        item=response.request.meta['item']
        #解析
        canshu_list=response.xpath('//div[@class="col-xs-6 parameter-configure-list"]/ul/li')
        #品牌型号
        pinpai_xinghao=canshu_list[0].xpath('./span/a/text()').extract()
        pinpai=pinpai_xinghao[0]
        xinghao=pinpai_xinghao[1]

        #车源所在地
        suozaidi=canshu_list[1].xpath('./span/text()').extract()[0]

        #发动机
        fadongji=canshu_list[2].xpath('./span/text()').extract()[0]

        #驱动方式
        qudong = canshu_list[3].xpath('./span/text()').extract()[0]

        #车辆级别
        jibie = canshu_list[4].xpath('./span/a/text()').extract()[0]

        #排量
        pailiang = canshu_list[5].xpath('./span/a/text()').extract()[0]

        #油耗
        youhao = canshu_list[6].xpath('./span/text()').extract()[0]

        #长宽高
        chicun = canshu_list[7].xpath('./span/text()').extract()[0]
        #车身类型
        leixing = canshu_list[8].xpath('./span/text()').extract()[0]
        #后配箱容量
        hxrl = canshu_list[9].xpath('./span/text()').extract()[0]


        print(pinpai,xinghao,suozaidi,fadongji,qudong,jibie.strip(),pailiang.strip(),youhao,chicun,leixing,hxrl)
        item['c_pinpai']=pinpai
        item['c_xinghao']=xinghao
        item['c_suozaidi']=suozaidi
        item['c_fadongji'] = fadongji
        item['c_qudong'] = qudong
        item['c_jibie'] = jibie.strip()
        item['c_pailiang'] = pailiang.strip()
        item['c_youhao'] = youhao
        item['c_chicun'] = chicun
        item['c_leixing'] = leixing
        item['c_hxrl'] = hxrl

        yield item
