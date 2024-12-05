# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MyscrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class MyscrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class RandomUserAgent(object):
    user_agent_list = [
        "Mozilla/5.0(Macintosh;Intel Mac 0s X10 10 1)ApplewebKit/537.36 (KHTML,like Gecko)Chrome/41.0.2227.1 Safari/537.36",
        "User-Agent:Mozilla/5.0(Macintosh;U;Intel Mac 0s x10 6 8;en-us) AppleWebKit/534.50(KHTM,like Gecko)Version/5.1 Safari/534.50",
        "Mozilla/5.0(Macintosh;Intel Mac0sX1082)AppleWebKit/537.13 (KHTMLlike Gecko)Chrome/24.0.1290.1 Safari/537.13",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
        "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Mozilla/5.0(windowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Mozilla/5.0(compatible;MSIE 10.0; windows NT 6.2;ARM; Trident/6.0)"
        ]

    def process_request(self,request,spider):

        useragent = random.choice(self.user_agent_list)
        request.headers.setdefault("User-Agent",useragent)

class RandomProxy(object):
    PROXIES = [
        {'ip_port':'111.8.60.9:8123','user_passwd':'user1:pass1'},
        {'ip_port':'101.71.27.120:80','user_passwd':'user2:pass2'},
        {'ip_port':'122.96.59.104:80','user_passwd':'user3:pass3'},
        {'ip_port':'122.224.249.122:8088','user_passwd':'user4:pass4'}
    ]

    def process_request(self,request,spider):
        if proxy['user_pass'] is None:
            request.meta['proxy'] = "http://" + proxy['ip_port']
        else:
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])

            request.headers['Proxy-Authorization'] = 'Basic' + base64_userpasswd
            request.meta['proxy'] = "http://"+proxy['ip_port']