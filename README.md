# Snakey-Scrapy

## Running

This repo is running in poetry, and using a makefile so to run:

```
    make scrape
```

Note: the current scraper will take about 3-5 minutes to complete. Output goes to files in scraped_data.

## Glossary

start_urls = the list of websites to start on
allowed_domains = the websites that the spiders are able to visit (IMPORTANT!)
used_urls = disallow visiting same page twice
keywords = words to look for
