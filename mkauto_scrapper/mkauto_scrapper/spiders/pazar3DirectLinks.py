import scrapy


class Pazar3DirectLinksSpider(scrapy.Spider):
    name = 'pazar3DirectLinksSpider'
    start_urls = ['https://www.pazar3.mk/oglasi/vozila/avtomobili?Page=1&Sort=DateDesc']  # added sorting
    pageNum = 1

    def parse(self, response):
        # i chose to use xpath selectors, you can use css selectors if you want
        links = response.xpath('//div[@class=\'result-content\']/div[@class=\'row\']//a[@class=\'Link_vis\']/@href')

        for link in links:
            yield {
                "link": link.extract()
            }

        if self.pageNum <= 1800:
            yield scrapy.Request(
                url=f"https://www.pazar3.mk/oglasi/vozila/avtomobili?Page={self.pageNum}&Sort=DateDesc",
                callback=self.parse)
        self.pageNum += 1

