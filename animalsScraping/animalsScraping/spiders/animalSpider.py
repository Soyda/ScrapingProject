import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from animalsScraping.items import AnimalsscrapingItem


class AnimalspiderSpider(CrawlSpider):
    name = 'animalSpider'
    allowed_domains = ['a-z-animals.com']
    start_urls = ['https://a-z-animals.com/animals']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="container"]/ul/li/a[starts-with(@href, "https://a-z-animals.com/animals/")]'), callback='parse_animal', follow=True),
    )

    def parse_animal(self, response):
        # item = {}
        item = AnimalsscrapingItem()

        item['name'] = response.xpath('//h1/text()').get()

        sck = response.xpath("//div[@class='col-lg-6']/dl/dt/a/text()").getall()
        scv = response.xpath("//div[@class='col-lg-6']/dl/dd/text()").getall()
        item['scientific_classification'] = {sck[i]:scv[i] for i in range(len(sck))}

        conservation_status_list = ['Extinct', 'Extinct in the wild', 'Critically endangered', 'Endangered', 'Vulnerable', 'Near Threatened', 'Least Concern', 'Data deficient', 'Not evaluated', 'Not Listed']
        item['conservation_status'] = response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[0] if response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[0] in conservation_status_list else 'Not evaluated'
        item['locations'] = response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[1:] if response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()[0] in conservation_status_list else response.xpath('//div[@class="col-lg-6"]/ul/li/a/text()').getall()
        
        # fk = response.xpath('//div[@class="col-md-6"]/div/dt/a/text()').getall()
        # fv = response.xpath('//div[@class="col-md-6"]/div/dd/text()').getall()
        # group_behavior = response.xpath('//div[@class="col-md-6"]/div/dd/ul/li/text()').getall()
        # if 'Group Behavior' in fk : fv.insert(fk.index('Group Behavior'), group_behavior)
        # item['Facts'] = {fk[i]:fv[i] for i in range(len(fk)) if fk[i]!='Location'}

        pck = response.xpath("//div[@class='col-lg-4']/dl/dt/a/text()").getall()
        pcv = response.xpath("//div[@class='col-lg-4']/dl/dd/text()").getall()
        if 'Color' in pck :
            colors_list = response.xpath("//div[@class='col-lg-4']/dl/dd/ul/li/text()").getall()
            pcv.insert(0, colors_list)
        item['physical_characteristics'] = {pck[i]:pcv[i] for i in range(len(pck))}

        # return item
        yield item

# scientific classification keys response.xpath("//div[@class='col-lg-6']/dl/dt/a/text()").getall()
# scientific classification values response.xpath("//div[@class='col-lg-6']/dl/dd/text()").getall()
# sck = response.xpath("//div[@class='col-lg-6']/dl/dt/a/text()").getall()
# scv = response.xpath("//div[@class='col-lg-6']/dl/dd/text()").getall()
# {sck[i]:scv[i] for i in range(len(sck))}

# facts keys response.xpath('//div[@class="col-md-6"]/div/dt/a/text()').getall()
# facts values response.xpath('//div[@class="col-md-6"]/div/dd/text()').getall()
                            #list of Group Behavior response.xpath('//div[@class="col-md-6"]/div/dd/ul/li/text()').getall()
# fk = response.xpath('//div[@class="col-md-6"]/div/dt/a/text()').getall()
# fv = response.xpath('//div[@class="col-md-6"]/div/dd/text()').getall()
# group_behavior = response.xpath('//div[@class="col-md-6"]/div/dd/ul/li/text()').getall()
# if 'Group Behavior' in fk : fv.insert(fk.index('Group Behavior'), group_behavior)
# {fk[i]:fv[i] for i in range(len(fk)) if fk[i]!='Location'}


# Physical Characteristics keys response.xpath("//div[@class='col-lg-4']/dl/dt/a/text()").getall()
# Physical Characteristics values response.xpath("//div[@class='col-lg-4']/dl/dd/text()").getall()
                                # list of colors response.xpath("//div[@class='col-lg-4']/dl/dd/ul/li/text()").getall()
# pck = response.xpath("//div[@class='col-lg-4']/dl/dt/a/text()").getall()
# pcv = response.xpath("//div[@class='col-lg-4']/dl/dd/text()").getall()
# colors_list = response.xpath("//div[@class='col-lg-4']/dl/dd/ul/li/text()").getall()
# pcv.insert(0, colors_list)
# {pck[i]:pcv[i] for i in range(len(pck))}
