# Scrapy settings for beike project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'beike'

SPIDER_MODULES = ['beike.spiders']
NEWSPIDER_MODULE = 'beike.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'beike (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Cookie': 'lianjia_uuid=c9f90954-55c4-40b0-8ddc-405ad281268d; crosSdkDT2019DeviceId=-574usk-osz0zr-buoo1wdw0n8jgul-dogka5elb; UM_distinctid=17b05719ecb63a-0c44acbb171249-4373266-1fa400-17b05719ecc6eb; _ga=GA1.2.1125531566.1627883938; _gid=GA1.2.270359125.1627883938; _jzqckmp=1; ke_uuid=a8f62ab17a9ef1c8aa6f52ccdbb73872; _jzqa=1.3880557964365069000.1627883938.1627883938.1627894322.2; select_city=420100; CNZZDATA1254525948=1429226494-1627894014-https%3A%2F%2Fnb.fang.ke.com%2F|1627894014; CNZZDATA1255633284=1113832701-1627893959-https%3A%2F%2Fnb.fang.ke.com%2F|1627893959; sajssdk_2015_cross_new_user=1; _qzja=1.2070744705.1627894343875.1627894343875.1627894343876.1627894672462.1627895906519.0.0.0.3.1; _qzjto=3.1.0; srcid=eyJ0IjoiXCJ7XFxcImRhdGFcXFwiOlxcXCJjYzQzMDdhMGE4ZmRlZDkwZGYxNGYwZWI5NmJmZDAyNDc0NTg2ZDEwZGUzNTA5ZDNlNGRjMGFiMDMwNTQxMmQ1ZjM5ZTY0MTQyMjdhZWU0YWNjZTZkMWVlOGRiMzFmNmU1MDEyNWNjNDlkMzBlYzZjYWY0ODI3MjBhMDlkNjI1NWYwNGMyMjFjZDY3YzliMzBjMjIzMzA1MWM5ZDkzZGRkZjc2NTRmNjMyNDBjNzEzYzAzMzNiNDkxNTZmMmZkMjg5Y2Y4NDk1YjZkMWM5NWMyMTA2NWRiOGM2MGJhMzVmMGVmMWNlMzQzYzM3ZTg3YzFjOGJlMTJmYjY4M2I4MGFlNGEyZTk4OGRhNmQ2MDM1OTkwNjFlMmQ3ZTdiZjllZDJlZjYxYjNhYjg2OWFmYjAyNTNkMGNkYzFkY2RhODI4NzlmZDBlM2JlN2FiNzI3YzUzYzQxODEzYWZiMTNhNDNlXFxcIixcXFwia2V5X2lkXFxcIjpcXFwiMVxcXCIsXFxcInNpZ25cXFwiOlxcXCIxMDRjOWM0YVxcXCJ9XCIiLCJyIjoiaHR0cHM6Ly93aC5mYW5nLmtlLmNvbS9sb3VwYW4vIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; sensorsdata2015jssdkcross={"distinct_id":"17b0615a10923e-06eea2d889dd2e-4373266-2073600-17b0615a10ae79","$device_id":"17b0615a10923e-06eea2d889dd2e-4373266-2073600-17b0615a10ae79","props":{"$latest_traffic_source_type":"直接流量","$latest_referrer":"","$latest_referrer_host":"","$latest_search_keyword":"未取到值_直接打开"}}; cy_ip=223.104.247.141; lianjia_ssid=99907b79-c94a-44e6-b4dc-54947c29bfeb; f-token=3PYAsI68pQJSTeDgmjJUQMGk2qdHxf++kA8338wdpHQXBmikzqinRTK4nIuk8Hm2DJVJjKJd4cNsCKEP4GucDX77RLBjetx1qhJAJwFNn+y7G3nieyttACHsnRx4UXaDcb9v19f3ixnGaexS3NdlJtBNrg==; digv_extends={"utmTrackId":""}; CNZZDATA1255604082=1491084094-1627893935-https%3A%2F%2Fnb.fang.ke.com%2F|1627915537; __xsptplusUT_788=1; lj_newh_session=eyJpdiI6IjJkcENJNGppWVBGa21SNlVETnBUc1E9PSIsInZhbHVlIjoiTlJKOWFGR2tIM0Vhc0tuR0Z3TmZqaHlNb3RXclRYQWVPZzdXUXh4Mkw0Mzl1c2p5Zjg1NStkb3dQUzZvMjVyXC9Mcm1FZmRiYTZnNkcyK05jendjb093PT0iLCJtYWMiOiI2NTdiZTRmOTUwYjBiMGJlZTdiYjI0NGI0OTYwYzhhNTI5NGEyYmIzYTU1MjlmNDlhNzNhNDRlYTQ5Y2U4MTkyIn0=; __xsptplus788=788.3.1627917184.1627917184.1#4|||||### ',
 'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'beike.middlewares.BeikeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'beike.middlewares.BeikeDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'beike.pipelines.BeikePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'PraProject.settings'
# 手动初始化Django：
import django
django.setup()
