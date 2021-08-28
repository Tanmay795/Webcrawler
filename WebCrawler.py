import scrapy


class Wiki(scrapy.Spider):
    name = "BIRD"
    start_urls = ['https://en.wikipedia.org/wiki/Bird']

    def parse(self, response):
         pass
