from scrapy.spiders import Spider
from pycoder.items import PycoderItem
from scrapy_splash import SplashRequest
import scrapy

class pycoderSpider(Spider):
    name = "pycoderSpider1"
    allowed_domains = ['pycoders.com']
    start_urls = ['http://pycoders.com/archive/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args= {'wait': 1}
            )

    def parse(self,response):
        items = []
        for listings in response.xpath('//div[@class="campaign"]'):
            item = PycoderItem()
            item['date'] = listings.xpath('text()').extract()
            item['title'] = listings.xpath('a/text()').extract()
            item['url'] = listings.xpath('a/@href').extract()
            items.append(item)
        return items
