# -*- coding: utf-8 -*-
import scrapy


class S2Spider(scrapy.Spider):
    name = 's2'
    allowed_domains = ['http://58.com']
    start_urls = ['http://http://58.com/']

    def parse(self, response):
        pass
