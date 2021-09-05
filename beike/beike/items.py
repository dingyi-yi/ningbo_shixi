# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from managesit.models import Building_Info
from managesit.models import SecondHouse_Info
from managesit.models import Renting_Info


class LouPanItem(DjangoItem):
    """
    楼盘
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Building_Info
    pass


class ershoufangItem(DjangoItem):
    """
    二手房
    """
    django_model = SecondHouse_Info
    pass


class zufangItem(DjangoItem):
    """
    租房
    """
    django_model = Renting_Info
    pass
