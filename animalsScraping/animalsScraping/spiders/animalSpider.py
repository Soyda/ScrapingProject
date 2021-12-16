import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AnimalspiderSpider(CrawlSpider):
    name = 'animalSpider'
    allowed_domains = ['a-z-animals.com']
    start_urls = ['https://a-z-animals.com/animals']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="container"]/ul/li/a[starts-with(@href, "https://a-z-animals.com/animals/")]'), callback='parse_animal', follow=True),
    )

    def parse_animal(self, response):
        item = {}
        item['Name'] = response.xpath('//h1/text()').get()
        # item['Scientific Classification'] = 
        conservation_status_list = ['Extinct', 'Extinct in the wild', 'Critically endangered', 'Endangered', 'Vulnerable', 'Near Threatened', 'Least Concern', 'Data deficient', 'Not evaluated', 'Not Listed']
        item['Conservation Status'] = response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[0] if response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[0] in conservation_status_list else 'Not evaluated'
        item['Locations'] = response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[1:] if response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[0] in conservation_status_list else response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()


        return item
