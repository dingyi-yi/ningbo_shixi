# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from beike.items import LouPanItem
from beike.items import ershoufangItem
from beike.items import zufangItem


class BeikePipeline:
    def process_item(self, item, spider):
        # 写入json文件
        item.save()
        # if isinstance(item, LouPanItem):
        #     item.save()
        #     pass
        # elif isinstance(item, ershoufangItem):
        #     item.save()
        #     pass
        # elif isinstance(item, zufangItem):
        #     item.save()
        #     pass
        return item

