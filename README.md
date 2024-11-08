# Scrapy Data Collection Project with UAKino

## Description

This project uses the Scrapy framework to collect information about documentaries from the [UAKino](https://uakino.website) website. The project includes two main spiders:

1. **uakino_data_spider**: Collects links to movies.
2. **detail_info_spider**: Collects detailed information about each movie using the collected links.

The `detail_info_spider` reads links from `movie_links.json` and outputs `result_data.json` with detailed information about each movie.

### Data Collected

For each movie, the following information is collected:

- **Title**
- **Poster URL**
- **Genres**
- **Country**
- **Year of release**
- **Description**
- **Source URL**

## Getting Started

To begin collecting data with this project, follow these steps:

1. **Run the `uakino_data_spider`** to gather movie links:
   - **Output**: `movie_links.json`, which contains the links to each movie.

2. **Run the `detail_info_spider`** to collect detailed movie information:
   - **Input**: `movie_links.json`
   - **Output**: `result_data.json`, a structured JSON file with details about each movie.

## Logging

The project uses `loguru` for detailed logging, with logs stored in separate files:

- `spider_log.txt`: Logs from the `uakino_data_spider`.
- `detail_spider_log.txt`: Logs from the `detail_info_spider`.

## Code Overview

- **uakino_data_spider**: Collects movie links from UAKino.
- **detail_info_spider**: Uses movie links to scrape additional information and store it in JSON format.

## Key Features

- Configured to handle Ukrainian language characters correctly.
- Mechanism to avoid duplicating URLs, ensuring unique data.
- Request delay settings to reduce server load and avoid being blocked.

## Libraries Used

- **Scrapy**: Framework for extracting data from websites.
- **Loguru**: For structured and easy-to-read logging.
- **JSON**: To store and structure collected data.

## Usage Notes

- Ensure that you have set up Scrapy and Loguru by installing the required packages.
- Set appropriate configurations in Scrapy’s settings for optimal performance.

## Requirements

- Python 3.x

Install dependencies with:

```bash
pip install -r requirements.txt
```

## License
MIT

## Copyright 
(c) 11-2024 Vladyslav Levytskyi



