# -*- coding: utf-8 -*-
import scrapy


class quotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
    	for quote in response.css('div.quote')
	        item = {
	        	'author_name': response.css('small.author::text').extract_first(),
	        	'text': response.css('span.text::text').extract_first(),
	        	'tags': response.css('a.tag::text').extract()
	        }
	        yield item
