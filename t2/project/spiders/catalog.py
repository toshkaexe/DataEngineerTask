import scrapy

class Catalog1Spider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['urparts.com']
    start_urls = ['https://www.urparts.com/']
    pages_count = 500

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.urparts.com/index.cfm/page/catalogue?part={page}'
            yield scrapy.Request(url, callback=self.parse)

    def parse_pages(self, response, **kwargs):
        for href in response.css('#pageTitle:attr("href")').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        manufacturer = []
        for dpath in response.css('#path'):
            manufacturer = dpath.css('a::text').extract()

        description = response.css('.c_partDetail')

        category = description.css('h2::text').extract()
        # category another version
        # for item in response.css('.c_partDetail'):
        #   manufacturer1 = item.css("h2::text").get()

        titleString = response.css('#pageTitle::text').extract_first('').strip()
        model = titleString.split(" - ", 3)[1]
        part = titleString.split(" - ", 3)[2]
        part_category = titleString.split(" - ", 3)[3]

        # part anotjer version
        # part = description.css('#partNo::attr("value")').extract()


        item = {
            'manufacturer': manufacturer[2],
            'category': category[0].strip(),
            'model': model,
            'part': part,
            'part_category': part_category.strip(),
            'url': response.request.url,
            }
        yield item