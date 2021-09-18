import scrapy

from daily_wiki.items import Article

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org/']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    # Exporting web scraping results
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'file:///tmp/feaured-aticles-%(time)s.json'  # Output file name wil be generated at runtime
    }


    def parse(self, response):

        # host URL
        host = self.allowed_domains[0]

        for link in response.css(".featured_article_metadata > a"):

            # Generator syntax for yield.
            # Return a single Article object for each link
            yield Article(
                title = link.attrib.get("title"),
                link = f"https://{host}{link.attrib.get('href')}"
            )
        pass
