import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class JuritravailItem(scrapy.Item):
	url = scrapy.Field()
	title = scrapy.Field()
	# content = scrapy.Field()

class JuritravailSpider(CrawlSpider):
	name = 'juritravail'
	allowed_domains = ['www.juritravail.com']
	start_urls = ['https://www.juritravail.com/forum-juridique']
	custom_settings = {
		'DEPTH_LIMIT': 0,
	}

	rules = (
		Rule(LinkExtractor(allow=('loi-travail-2017', ), deny=('\.txt', '/wiki/.+:.+', '/index.+')), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		#self.logger.info('Hi, this is an item page! %s', response.url)
		item = JuritravailItem()
		item['url'] = response.url
		item['title'] = response.xpath('//h1//text()').extract_first()
		#item['content'] = ' '.join(response.xpath("//div[@id='bodyContent']//div[@id='mw-content-text']/*/child::p[not(@*)][1]//text()").extract())
		return item
