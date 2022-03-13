import scrapy


class Reklama5DirectLinksSpider(scrapy.Spider):
    name = 'reklama5DirectLinksSpider'
    start_urls = [
        'http://reklama5.mk/Search?q=&city=&sell=0&sell=1&buy=0&buy=1&trade=0&trade=1&includeOld=0&includeOld=1&includeNew=0&includeNew=1&private=0&company=0&page=1&SortByPrice=0&zz=1&cat=24']  # added sorting
    pageNum = 2

    def parse(self, response):
        # i chose to use xpath selectors, you can use css selectors if you want
        links = response.xpath('//div[@class=\'clear-padding text-center\']//a[@class=\'SearchAdTitle\']/@href')

        for link in links:
            yield {
                "link": link.extract()
            }

        if self.pageNum <= 1052:
            yield scrapy.Request(
                url=f"http://reklama5.mk/Search?q=&city=&sell=0&sell=1&buy=0&buy=1&trade=0&trade=1&includeOld=0&includeOld=1&includeNew=0&includeNew=1&private=0&company=0&page={self.pageNum}&SortByPrice=0&zz=1&cat=24",
                callback=self.parse)
        self.pageNum += 1
