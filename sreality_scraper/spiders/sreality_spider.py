
import scrapy
import psycopg2
from scrapy.http import Request

   

class SrealitySpider(scrapy.Spider):
    name = "sreality_spider"
    start_urls = ['https://www.sreality.cz/en/search']

    def parse(self, response):
        # Extrae los datos que deseas
        items = response.xpath('//div[@class="info"]')
        for item in items[:500]:
            title = item.xpath('.//h2/a/text()').get()
            image_url = item.xpath('.//img/@src').get()

            # Guarda los datos en la base de datos
            connection = psycopg2.connect(**settings.DATABASE)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO table (title, image_url) VALUES (%s, %s)", (title, image_url))
            connection.commit()
            cursor.close()
            connection.close()

            yield {
                'title': title,
                'image_url': image_url
            }
            pass 
           
