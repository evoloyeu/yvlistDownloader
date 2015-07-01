import json, pickle
from scrapy.spider import Spider
from scrapy.selector import Selector

from sptube.items import SptubeItem

# not finish
class AutolistSpider(Spider):
	name = 'autolist'
	
	url_prefix = 'https://www.youtube.com'
	start_urls = [] #['https://www.youtube.com/playlist?list=PLRTwKflrxkQCrP1ZbbKpdP8xoQu2AXT74']

	def __init__(self, playlistURL=None, *args, **kwargs):
		super(AutolistSpider, self).__init__(*args, **kwargs)
		self.start_urls = [playlistURL]

	def parse(self, response):

		sel = Selector(response)
		sites = sel.xpath('//ol[@id="playlist-autoscroll-list"]')
		# sites = ol.xpath('//li')
		items = []

		print '........Len:', len(sites)
		print '=======response:', response
		# f=open('playlist.txt', 'w')
		for site in sites:

			# item = SptubeItem()
			# name = site.xpath('h4/text()').extract()[0].strip().encode('utf-8')
			# url = site.xpath('a/@href').extract()[0].encode('utf-8')

			# item['name'] = name
			# item['url'] = self.url_prefix+url
			# # print item
			# items.append(item)
			# f.write(name+'\n')
			# f.write(self.url_prefix+url+'\n')
			print '...................'

		# print '=========='
		# print items
		# print '=========='
		
		# f.write(items)
		# f.write(items)
		# pickle.dump(items, f)
		# f.close()

		return items





