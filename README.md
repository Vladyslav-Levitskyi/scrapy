# scrapy

Scrapy Data Collection Project with UAKino

Description:
This project uses the Scrapy framework to collect information about documentaries from the UAKino.website. The project consists of two main spiders:
uakino_data_spider - collects links to movies.
detail_info_spider - collects detailed information about each movie.

This spider uses the links from movie_links.json and creates a result_data.json with detailed information about each movie.

The following information is collected for each film:
Title
Poster URL
Genres
Country
Year of release
Description
Source URL

Logging:
The project uses loguru for logging. Logs are stored in files:
spider_log.txt - for the first spider.
detail_spider_log.txt - for the second spider.

Notes:
The project is configured for correct processing of the Ukrainian language.
Implemented URL duplication avoidance mechanism.
A delay between requests is set to reduce the load on the server.

License MIT



Copyright (c) 11-2024 Vladyslav Levytskyi



