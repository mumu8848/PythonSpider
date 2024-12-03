from typing import Optional, Any

import scrapy
from scrapy.http import Request
from myScrapy.items import MyscrapyItem


class TipdmSpider(scrapy.Spider):
    name = "Tipdm"
    allowed_domains = ["www.tipdm.com"]
    start_urls = ["http://www.tipdm.com/xwzx/index.jhtml"]

    def parse_text(self,response):
        item = MyscrapyItem()

        # 文章标题
        item['title'] = response.xpath('//div[@class="artTitle"]/h1/text()').extract()

        # 文章发布时间
        item['time'] = response.xpath('//span[@class="date"]/text()').extract()

        # 文章浏览数
        item['view_count'] = response.xpath('//span[@class="view"]/text()').extract()

        # 文章正文
        text =  response.xpath('//div[@class="artCon"]//p/text()').extract()
        texts = ''
        for strings in text:
            texts = texts + strings + '\n'
        item['text'] = [texts.strip()]
        return item

    def parse_url(self,response):
        # 网页解析，获得文章网页 URL
        urls = response.xpath('//*[@id="t505"]/div/div[3]/h1/a/@href').extract()

        # 回调
        for url_sub in urls:
            url_base = 'http://www.tipdm.com/'
            yield Request(url_sub,callback=self.parse_text,dont_filter=True)

    def parse(self, response):
        # 网页解析
        number = int(response.xpath('//*[@id="t505"]/div[6]/div/a[6]/text()').extract()[0])

        # 网址拼接
        url_all = ['http://www.tipdm.com/xwzx/index_{}.jhtml#'.format(i) for i in range(3,4)]

        # 加入首页
        url_all.insert(0,'http://www.tipdm.com/xwzx/index.jhtml') # 加入第一页的内容

        # 回调
        for url in url_all:
            yield scrapy.Request(url,callback=self.parse_url,dont_filter=True)








