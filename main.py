# main.py

import scrapy
import psycopg2

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/en/search']

    def parse(self, response):
        items = response.xpath('//div[@class="text-content"]')
        
        for item in items[:500]:
            title = item.xpath('.//h2/a/text()').get()
            image_url = item.xpath('.//img/@src').get()
            
            # Save data to PostgreSQL database
            self.save_to_database(title, image_url)
            
            yield {
                'title': title,
                'image_url': image_url
            }
    
    def save_to_database(self, title, image_url):
        conn = psycopg2.connect(
            host='172.21.0.2',
            database='postgres',
            user='nico',
            password='Maradona1!'
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ads (title, image_url) VALUES (%s, %s)', (title, image_url))
        conn.commit()
        cursor.close()
        conn.close()
