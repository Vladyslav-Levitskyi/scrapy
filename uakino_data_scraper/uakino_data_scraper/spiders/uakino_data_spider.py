from scrapy import Spider, Request
from loguru import logger

class UakinoSpider(Spider):
    name = 'uakino_data_spider'
    allowed_domains = ['uakino.me']
    start_urls = ['https://uakino.me/filmy/documentaries/']
    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter',
        'FEEDS': {
            'movie_links.json': {
                'format': 'json',
                'overwrite': True,
                'encoding': 'utf8'
            }
        },
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.add("spider_log.txt", rotation="500 MB", level="INFO")
        self.visited_urls = set()  # Множина для відстеження відвіданих URL

    def parse(self, response):
        # Збір посилань на фільми з поточної сторінки
        movie_links = response.css('.movie-item a.movie-title::attr(href)').getall()
        
        for link in movie_links:
            if link not in self.visited_urls:  # Перевіряємо чи не було вже такого посилання
                self.visited_urls.add(link)
                logger.info(f"Знайдено посилання на фільм: {link}")
                yield {
                    'movie_url': link
                }

        # Обробка пагінації
        current_page = response.css('.navigation span::text').get()
        logger.info(f"Поточна сторінка: {current_page}")
        
        next_pages = response.css('.navigation a::attr(href)').getall()
        if next_pages:
            logger.info(f"Знайдено {len(next_pages)} сторінок пагінації")
            for page_url in next_pages:
                if page_url not in self.visited_urls:  # Перевіряємо чи не відвідували цю сторінку
                    self.visited_urls.add(page_url)
                    logger.info(f"Переходимо на сторінку: {page_url}")
                    yield Request(
                        url=page_url,
                        callback=self.parse,
                        headers={
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'uk,en-US;q=0.7,en;q=0.3'
                        }
                    )
        else:
            logger.warning("Посилання на наступні сторінки не знайдені")