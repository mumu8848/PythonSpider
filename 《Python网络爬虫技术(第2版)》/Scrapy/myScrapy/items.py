# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Items将会流向Item Pipelines
class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    time = scrapy.Field()
    view_count = scrapy.Field()
