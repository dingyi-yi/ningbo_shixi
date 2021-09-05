import re

import scrapy

from beike.items import ershoufangItem
class ErshoufangspiderSpider(scrapy.Spider):
    name = 'ershoufangspider'
    start_urls = ['https://wh.ke.com/ershoufang/']
    base_url = "https://wh.zu.ke.com/zufang/pg{}"
    header={

    }
    for i in range(2, 10):
        url = base_url.format(i)
        start_urls.append(url)

    def parse(self, response):

        all_data = response.xpath("//*/li[@class='clear']")
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        for data in all_data:
            try:
                item=ershoufangItem()
                item['title']=data.xpath("div[@class='info clear']/div[@class='title']/a/text()").extract()[0].strip()
                item['adress']=data.xpath("div[@class='info clear']/div[@class='address']/div[@class='flood']/div[@class='positionInfo']/a/text()").extract()[0].strip()
                housinfospan=data.xpath("div[@class='info clear']/div[@class='address']/div[@class='houseInfo']/text()").extract()
                housinfo_lsit=[]
                for info in housinfospan:
                    if zhPattern.search(info) is not None or re.match(r'[+-]?\d+$', info) is not None:
                        brif_m=info.replace("\n","")
                        brif_m=brif_m.replace(" ","")
                        housinfo_lsit.append(brif_m)

                item['houseinfo']=housinfo_lsit[0]
                item['totalPrice']=data.xpath("div[@class='info clear']/div[@class='address']/div[@class='priceInfo']/div[@class='totalPrice']/span/text()").extract()[0].strip()
                unitPrice=0
                try:
                    unitPrice=int(data.xpath("div[@class='info clear']/div[@class='address']/div[@class='priceInfo']/div[@class='unitPrice']/span/text()").extract()[0].strip())
                except Exception as e:
                    print(e)
                    unitPrice=0
                item['unitPrice']=unitPrice
                yield item
            except Exception as e:
                print(e)
                continue

        pass
