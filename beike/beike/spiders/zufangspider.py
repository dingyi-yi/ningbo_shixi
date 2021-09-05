import re

import scrapy

from beike.items import zufangItem
class ZufangspiderSpider(scrapy.Spider):
    name = 'zufangspider'
    allowed_domains = ['nb.fang.ke.com']
    start_urls = ['https://wh.zu.ke.com/zufang/']
    base_url = "https://wh.zu.ke.com/zufang/pg{}/"
    for i in range(2,50):
        url = base_url.format(i)
        start_urls.append(url)

    def parse(self, response):
        all_data = response.xpath("//div[@class='content__list']/div[@class='content__list--item']")
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        for data in all_data:
            item=zufangItem()
            item['title']=data.xpath("div[@class='content__list--item--main']/p[1]/a/text()").extract()[0].strip()
            brif_div=data.xpath("div[@class='content__list--item--main']/p[2]/text()").extract()
            brif_introduction=[]
            for brif in brif_div:
                if zhPattern.search(brif)!=None or  re.match(r'[+-]?\d+$', brif)!=None:
                    brif_m=brif.replace("\n","").strip()
                    brif_introduction.append(brif_m)
            item['brif_introduction']="/".join(brif_introduction)
            advantage_i=data.xpath("div[@class='content__list--item--main']/p[3]/i")
            advantage_list=[]
            for advantage in advantage_i:
                advantage_list.append(advantage.xpath("text()").extract()[0])
            item['advantage']="/".join(advantage_list)
            price=0
            try:
                price=int(data.xpath("div[@class='content__list--item--main']/span/em/text()").extract()[0].strip())
            except Exception as e:
                print(e)
                price=0
            item['price']=price
            yield item



