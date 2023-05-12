import scrapy
from datetime import datetime

class BlogSpider(scrapy.Spider):
    name = 'northspider'
    start_urls = ['https://northcoders.com/']

    # limiters
    allowed_domains = ['northcoders.com']
    first_com = start_urls[0].find('.com')+4
    used_urls = []

    custom_settings = {
        'FEEDS': { './scraped_data/%(name)s/%(name)s_batch_%(batch_id)d.json': { 'format': 'json', 'batch_item_count': 50, 'overwrite': True}}
        }


        
    # methods

    def parse(self, response):
        
        # have we been to this page before? ew.
        if response.url in self.used_urls:
            return
        
        # hipster checklist
        self.used_urls.append(response.url)
        
        # find the thing, save the things
        elements = response.xpath("//*[contains(text(), 'SQL')]").getall()

        if len(elements) != 0:
            json_body = {}
            for i in range(len(elements)):
                json_body[str(i)] = elements[i]

            yield {'body': json_body, 'meta': {'url': response.url, 'time': f'{datetime.now()}'}}
        
        # be free, my child
        for next_page in response.css('a'):
            yield response.follow(next_page, self.parse)
        
        # to kill the crawler
        # raise scrapy.exceptions.CloseSpider('but why? :(')