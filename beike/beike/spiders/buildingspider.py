import scrapy

from beike.items import LouPanItem
class BuildingspiderSpider(scrapy.Spider):
    name = 'buildingspider'
    start_urls = ['https://wh.fang.ke.com/loupan/{17}']
    base_url = "https://wh.fang.ke.com/loupan/pg{}/"
    for i in range(18,100):
        url = base_url.format(i)
        start_urls.append(url)

    def parse(self, response):

        all_data = response.xpath("//ul[@class='resblock-list-wrapper']/li")
        for data in all_data:
            try:
                item=LouPanItem()
                item['name'] = data.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-name']/a/text()").extract()[0]
                state=data.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-name']/span[1]/text()").extract()[0]
                house_kind =data.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-name']/span[2]/text()").extract()[0]
                if state=="在售":
                    item["state"]=1
                elif state=="待售":
                    item["state"] = 2
                else:
                    item["state"] = 0
                # 房屋类型 1:住宅 2底商 3商业类 4别墅 5写字楼
                if house_kind=="底商":
                    item["house_kind"]=2
                elif house_kind=="商业类" or house_kind=="商业":
                    item["house_kind"] = 3
                elif house_kind=="别墅":
                    item["house_kind"] = 4
                elif house_kind=="写字楼":
                    item["house_kind"] = 5
                else:
                    item["house_kind"] = 1

                item['adress']=data.xpath("div[@class='resblock-desc-wrapper']/a[@class='resblock-location']/text()").extract()[1]
                housetype_span= data.xpath("div[@class='resblock-desc-wrapper']/a[@class='resblock-room']/span")
                acreage="暂无"
                housetype_list=[]
                for housetype in housetype_span:
                    if "建面" in housetype.xpath("text()").extract()[0]:
                        acreage=housetype.xpath("text()").extract()[0]
                    else:
                        housetype_list.append(housetype.xpath("text()").extract()[0])
                item['acreage']=acreage
                item['housetype_list']='/'.join(housetype_list)



                a_price=data.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-price']/div["
                                         "@class='main-price']/span[@class='number']/text()").extract()[0]
                average_price=0
                if a_price=="价格待定":
                    average_price=0
                else:
                    average_price=int(a_price)

                item['average_price']=average_price
                print(average_price)
                if data.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-price']/div[""@class='second']"):
                    total_price = data.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-price']/div["
                                             "@class='second']/text()").extract()[0]
                else:
                    total_price="暂无"
                item['total_price']=total_price
                advantage_span=data.xpath("div[@class='resblock-desc-wrapper']/div[@class='resblock-tag']/span")
                advantage_lsit=[]
                for advantage in advantage_span:
                    advantage_lsit.append(advantage.xpath("text()").extract()[0])
                item['advantage']="/".join(advantage_lsit)

                yield item
            except Exception as e:
                print(e)
                continue
