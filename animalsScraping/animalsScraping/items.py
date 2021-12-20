# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimalsscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    scientific_classification = scrapy.Field()
    conservation_status = scrapy.Field()
    locations = scrapy.Field()
    physical_characteristics = scrapy.Field()
    
