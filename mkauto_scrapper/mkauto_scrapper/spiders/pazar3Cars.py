import scrapy
import json

# change this to your path
with open('C:\\Users\\Urim\\Desktop\\projects\\mkauto\\mkauto_scrapper\\pazar3DirectLinks.json') as f:
    data = json.load(f)


class Pazar3CarsSpider(scrapy.Spider):
    name = 'pazar3CarsSpider'
    start_urls = list(map(lambda x: f"http://pazar3.mk{x['link']}", data))

    def __init__(self, start_from, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = self.start_urls[int(start_from): int(start_from) + 300]

    def parse(self, response):
        yield {
            "title": response.xpath('//h1[@class=\'h3 d-inline\']/text()').extract_first(),
            "currentPrice": response.xpath('//strong[@class=\'text-success\']/text()').extract_first(),
            "oldPrice": response.xpath('//del[@class=\'text-muted\']/text()').extract_first(),
            "sellerName": response.xpath(
                '(//div[@class="card-body text-center"]/div[1]/strong[@class="h4"])[1]/text()').extract_first(),
            "sellerNumber": response.xpath('(//div[@class="card-body text-center"]/a/@href)[1]').extract_first(),
            "date": response.xpath('//blockquote//mark/text()').extract_first(),
            "img_links": response.xpath('//div[@class=\'carousel-inner\']/div/a/@href').extract(),
            "description": response.xpath(
                '(//div[@class=\'ad-details\']/div[@class=\'row\'][2]/div[1]/div/div[@class=\'row\']/div/div)[1]/text()').extract_first(),
            "adType": response.xpath('//div[@class="card-body"]/div/div[1]/div/a/div/text()').extract_first(),
            "sellerType": response.xpath('//div[@class="card-body"]/div/div[2]/div/a/div/text()').extract_first(),
            "productionYear": response.xpath(
                '//div[@class="card-body"]/div/div[3]/div/div[2]/a/text()').extract_first(),
            "transmissionType": response.xpath(
                '//div[@class="card-body"]/div/div[4]/div/div[2]/a/text()').extract_first(),
            "mileage": response.xpath('//div[@class="card-body"]/div/div[5]/div/div[2]/a/text()').extract_first(),
            "fuelType": response.xpath('//div[@class="card-body"]/div/div[6]/div/div[2]/a/text()').extract_first(),
            "registrationType": response.xpath(
                '//div[@class="card-body"]/div/div[7]/div/div[2]/a/text()').extract_first(),
            "color": response.xpath('//div[@class="card-body"]/div/div[8]/div/a/div/text()').extract_first(),
            "location": response.xpath('//div[@class="card-body"]/div/div[9]/div/a/div/text()').extract_first(),
            "carType": response.xpath('//div[@class="card-body"]/div/div[10]/div/div/a/div/text()').extract_first(),
            "maker": response.xpath('//div[@class="card-body"]/div/div[11]/div/a/div/text()').extract_first(),
            "model": response.xpath('//div[@class="card-body"]/div/div[12]/div/a/div/text()').extract_first(),
            "url": response.request.url
        }
