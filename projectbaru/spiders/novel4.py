import scrapy


class QuotesSpider(scrapy.Spider):
    name = "eternal"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-1-immortal-fate/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-2-mysterious-lady/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-3-supreme-demon-classic/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-4-tri-bovine-style/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-5-su-familys-misfortune/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-6-murder/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-7-connate-expert/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-8-su-hong/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-9-body-tempering-sutra/',
            'https://www.worldnovel.online/novel-eternal-sacred-king-id/chapter-10-attend-the-banquet-alone/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }