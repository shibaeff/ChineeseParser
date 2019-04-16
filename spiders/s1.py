# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
import pickle

import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 
# Accessing variables.
S1_SEEDS = os.getenv('S1_SEEDS')

def hash_url():
    S1Spider.count += 1
    return S1Spider.count

class S1Spider(scrapy.Spider):
    name = 's1'
    allowed_domains = S1_SEEDS
    start_urls = ['http://anshun.liebiao.com/jinrongdaikuan/']
    count = 0
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse"
        )
    ]

    custom_settings = {
        'DEPTH_LIMIT': 100,
        # 'DOWNLOADER_MIDDLEWARES' : {
        #         'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        #         'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        #     }
        'DNS_TIMEOUT': 720,
        'DOWNLOAD_TIMEOUT': 720
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        links = response.xpath("//a/@href").extract()
        links = [item for item in links if re.search(r'http://[a-z]+\.liebiao\.com/[a-z]+/\d+.html$', item) is not None]
        with open('links.txt', 'a') as f:
            for item in links:
                f.write("%s\n" % item)
        for link in links:
            yield response.follow(link, self.parse)