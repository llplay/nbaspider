from scrapy.spiders import Spider
from pycoder.items import PycoderItem
from scrapy_splash import SplashRequest
import scrapy
import scrapy.item
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class NbaSpider(Spider):
    name = "nba"
    allowed_domains = ['qq.com']
    start_urls = ['http://nba.stats.qq.com/schedule/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args= {'wait': 0.5}
            )

    def parse(self,response):
        items = []
        stream = response.xpath('//div[@class="stream"]')
        streamStr = stream.xpath('//div[@class="stream"]/text()').extract()
        if len(streamStr) < 10:
            return items
        #print(stream.extract())
        for itemOne in stream:
            #print(itemOne.xpath('./div[@class="item"]/div[@class="date"]/text()'))
            listtime = itemOne.xpath('./div[@class="item"]/div[@class="list-time"]')
            #print(listtime)
            date = itemOne.xpath('./div[@class="item"]/div[@class="date"]/text()').extract()
            print len(date)
            print len(listtime)
            index = 0;
            for listOne in listtime:
                #print(listOne)
                row = listOne.xpath('./div[@class="row odd\'"]')
                #print(row.extract())
                for rowOne in row:
                    item = PycoderItem()
                    item['date'] = date[index]
                    item['time'] = rowOne.xpath('./div[@class="time"]/text()').extract()[0]
                    item['status'] = rowOne.xpath('./div[@class="status"]/text()').extract()[0]
                    item['visit'] = rowOne.xpath('./div[@class="visit"]/a/span[@class="chname"]/text()').extract()[0]
                    item['vgoal'] = rowOne.xpath('./div[@class="goal"]/span[@class="visit"]/text()').extract()
                    item['hgoal'] = rowOne.xpath('./div[@class="goal"]/span[@class="home"]/text()').extract()
                    item['home'] = rowOne.xpath('./div[@class="home"]/a/span/text()').extract()[0]
                    items.append(item)
                row = listOne.xpath('./div[@class="row even\'"]')
                for rowOne in row:
                    item = PycoderItem()
                    item['date'] = date[index]
                    item['time'] = rowOne.xpath('./div[@class="time"]/text()').extract()[0]
                    item['status'] = rowOne.xpath('./div[@class="status"]/text()').extract()[0]
                    item['visit'] = rowOne.xpath('./div[@class="visit"]/a/span[@class="chname"]/text()').extract()[0]
                    item['vgoal'] = rowOne.xpath('./div[@class="goal"]/span[@class="visit"]/text()').extract()
                    item['hgoal'] = rowOne.xpath('./div[@class="goal"]/span[@class="home"]/text()').extract()
                    item['home'] = rowOne.xpath('./div[@class="home"]/a/span/text()').extract()[0]
                    items.append(item)
                index = index + 1
        return items