import scrapy


class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    start_urls = ["https://tripadvisor.com"]

    def parse(self, response):
        pass
