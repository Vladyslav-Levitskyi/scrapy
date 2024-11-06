import json
from scrapy import Spider, Request
from loguru import logger

class DetailInfoSpider(Spider):
    name = 'detail_info_spider'
    allowed_domains = ['uakino.me']
    custom_settings = {
        'FEEDS': {
            'result_data.json': {
                'format': 'json',
                'overwrite': True,
                'encoding': 'utf8'
            }
        },
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.add("detail_spider_log.txt", rotation="500 MB", level="INFO")
        
    def start_requests(self):
        # Читаємо URLs з JSON файлу
        with open('movie_links.json', 'r', encoding='utf-8') as f:
            movie_urls = json.load(f)
            
        for item in movie_urls:
            url = item['movie_url']
            logger.info(f"Обробка URL: {url}")
            yield Request(
                url=url,
                callback=self.parse,
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'uk,en-US;q=0.7,en;q=0.3'
                }
            )

    def parse(self, response):
        try:
            # Отримуємо назву фільму
            title = response.css('span.solototle::text').get().strip()
            
            # Отримуємо посилання на зображення
            image_url = response.css('a[data-fancybox="gallery"] img::attr(src)').get()
            full_image_url = response.css('a[data-fancybox="gallery"]::attr(href)').get()
            
            # Отримуємо жанри
            genres = response.css('.fi-desc[itemprop="genre"] a::text').getall()
            
            # Отримуємо країну
            country = response.css('.fi-item:contains("Країна") .fi-desc a::text').get()
            
            # Отримуємо рік
            year = response.css('.fi-item:contains("Рік") .fi-desc a::text').get()
            
            # Отримуємо опис
            description = response.css('.full-text.clearfix::text').get()
            if description:
                description = description.strip()
            
            logger.info(f"Зібрано інформацію про фільм: {title}")
            
            yield {
                'title': title,
                'poster_preview': image_url,
                'poster_full': full_image_url,
                'genres': genres,
                'country': country,
                'year': year,
                'description': description,
                'source_url': response.url
            }
            
        except Exception as e:
            logger.error(f"Помилка при обробці {response.url}: {str(e)}")