import scrapy
# pip install scrapy


class TripAdvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    start_urls = [
        #'https://www.tripadvisor.es/Restaurant_Review-g187514-d2071743-Reviews-Pasteleria_La_Mallorquina_Puerta_Del_Sol-Madrid.html'  # Cambia esto a la URL de interés
        'https://pastelerialamallorquina.es/'
    ]

    def parse(self, response):
        for comentario in response.css('div.review-container'):
            yield {
                'autor': comentario.css('span.ui_header_link::text').get(),
                'comentario': comentario.css('q::text').get(),
                'fecha': comentario.css('span.ratingDate::text').get(),
            }

        # Link a la siguiente página
        siguiente_pagina = response.css('a.ui_button.nav.next.primary::attr(href)').get()
        if siguiente_pagina:
            yield response.follow(siguiente_pagina, callback=self.parse)
