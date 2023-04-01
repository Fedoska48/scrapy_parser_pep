from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for row in response.css('#numerical-index tbody > tr'):
            pep_link = urljoin(
                self.start_urls[0],
                row.css('a::attr(href)').get()
            )
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, resposne):
        data = {
            'number': resposne.css(
                'h1.page-title::text'
            ).get().split('–')[0].strip(),
            'name': resposne.css(
                'h1.page-title::text'
            ).get().split('–')[1].strip(),
            'status': resposne.css('dd.field-even > abbr::text').get()
        }
        yield PepParseItem(data)
