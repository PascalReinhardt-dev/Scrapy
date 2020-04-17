# -*- coding: utf-8 -*-
import scrapy


class quotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['onvista.de']
    start_urls = ['https://www.onvista.de/rohstoffe/Oelpreis-Brent-26262975']

    def parse(self, response):
        yield{
        	'stocks_value': response.css('div.KURSDATEN_CONTAINER.span').extract_first(),
        }
