import scrapy


class QuotesSpider(scrapy.Spider):
    name = "legend"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/chapter-1/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-2-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-3-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-4-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-5-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-6-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-7-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-8-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-9-indonesian/',
            'https://www.worldnovel.online/novel-the-legend-of-futian-bahasa-id/tlof-chapter-10-indonesian/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }