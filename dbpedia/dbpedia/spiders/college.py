# -*- coding: utf-8 -*-
import scrapy


class CollegeSpider(scrapy.Spider):
    name = 'college'
    allowed_domains = ['http://dbpedia.org/page/Rensselaer_Polytechnic_Institute']
    start_urls = ['http://http://dbpedia.org/page/Rensselaer_Polytechnic_Institute/']

    def parse(self, response):
        pass
