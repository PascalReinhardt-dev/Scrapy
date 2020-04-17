import scrapy


 class FirstSpider(scrapy.Spider):
 	name = "Manfred"
 	allowed_domains = ["toscrape.com"]
    start_urls = [
        'http://quotes.toscrape.com/',
    ]


    def parse(self,response):
    	yield{
    		'author_name': response.css('small.author::text').extract_first(),
    		'text': response.css('span.text::text').extract_first(),
    		'tags': response.css('a.tag::text').extract()
    		}