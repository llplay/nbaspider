# -*- coding: utf-8 -*-
from scrapy.utils.project import get_project_settings
from spiders.NbaSpider import NbaSpider
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
import spiders.NbaSpider
from model.config import DBSession
from model.rule import Rule
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings


def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Closing reactor", level=log.INFO)
    reactor.stop()

# log.start(loglevel=log.DEBUG)
# settings = Settings()
settings = get_project_settings()
# crawl responsibly
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
crawler = CrawlerProcess(settings)
# stop reactor when spider closes
# crawler.signals.connect(spider_closing, signal=signals.spider_closed)
# crawler.configure()

crawler.crawl(NbaSpider())
crawler.start()
# reactor.run()

# settings = Settings()

# crawl settings
# settings = get_project_settings()
# settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
# settings.set("ITEM_PIPELINES" , {
#     'pipelines.DuplicatesPipeline': 200,
#     # 'pipelines.CountDropPipline': 100,
#     'pipelines.DataBasePipeline': 300,
# })

# process = CrawlerProcess(settings)
# process.crawl(spiders.NbaSpider)
# process.start()
# db = DBSession()
# rules = db.query(Rule).filter(Rule.enable == 1)
# for rule in rules:
#     process.crawl(spiders.nba,rule)
# process.start()
