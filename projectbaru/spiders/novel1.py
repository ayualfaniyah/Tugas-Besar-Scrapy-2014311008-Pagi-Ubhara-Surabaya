import scrapy


class QuotesSpider(scrapy.Spider):
    name = "first"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/the-first-order/chapter-1-a-sickness-in-the-head/',
            'https://www.worldnovel.online/the-first-order/chapter-2-this-world-has-never-trusted-tears/',
            'https://www.worldnovel.online/the-first-order/chapter-3-a-palace/',
            'https://www.worldnovel.online/the-first-order/chapter-4-luck-is-a-type-of-skill-too/',
            'https://www.worldnovel.online/the-first-order/chapter-5-the-school/',
            'https://www.worldnovel.online/the-first-order/chapter-6-walls-and-science/',
            'https://www.worldnovel.online/the-first-order/chapter-7-substitute-teacher/',
            'https://www.worldnovel.online/the-first-order/chapter-8-something-really-is-wrong-with-his-head/',
            'https://www.worldnovel.online/the-first-order/chapter-9-ask-me-if-theres-anything-you-dont-understand/',
            'https://www.worldnovel.online/the-first-order/chapter-10-side-quest/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }