from selenium import webdriver
# pip install selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

# Configuración de Selenium
driver_path = '/path/to/chromedriver'  # Cambia esto a la ruta de tu WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# URL de la página de TripAdvisor
url = 'https://www.tripadvisor.com/Hotel_Review-g60763-d122005-Reviews-Hilton_Garden_Inn_Times_Square-New_York_City_New_York.html'  # Cambia esto a la URL de interés
# url = 'https://www.tripadvisor.es/Restaurant_Review-g187514-d2071743-Reviews-Pasteleria_La_Mallorquina_Puerta_Del_Sol-Madrid.html'
driver.get(url)

# Espera a que cargue la página
time.sleep(5)

# Archivo CSV para guardar los comentarios
with open('comentarios_tripadvisor.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Autor', 'Comentario', 'Fecha'])

    # Bucle para cargar más comentarios
    while True:
        # Seleccionar comentarios
        comentarios = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')

        for comentario in comentarios:
            try:
                autor = comentario.find_element(By.CSS_SELECTOR, 'span.ui_header_link').text
                texto = comentario.find_element(By.CSS_SELECTOR, 'q').text
                fecha = comentario.find_element(By.CSS_SELECTOR, 'span.ratingDate').text

                # Escribir en CSV
                writer.writerow([autor, texto, fecha])
            except:
                continue

        # Intentar hacer clic en el botón "Siguiente" para cargar más comentarios
        try:
            siguiente = driver.find_element(By.CSS_SELECTOR, 'a.ui_button.nav.next.primary')
            ActionChains(driver).move_to_element(siguiente).click().perform()
            time.sleep(3)
        except:
            print("No hay más comentarios.")
            break

# Cerrar el navegador
driver.quit()
