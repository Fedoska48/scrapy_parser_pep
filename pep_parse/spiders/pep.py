from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for row in response.css(
                '#numerical-index tbody > tr a::attr(href)'
        ).getall():
            yield response.follow(
                urljoin(self.start_urls[0], row),
                callback=self.parse_pep
            )

    def parse_pep(self, resposne):
        number, name = resposne.css('h1.page-title::text').get().split(' – ')
        yield PepParseItem(
            dict(
                number=number,
                name=name,
                status=resposne.css('dd.field-even > abbr::text').get()
            )
        )
