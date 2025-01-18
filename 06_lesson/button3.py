from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Указываем путь к драйверу
driver = webdriver.Chrome(executable_path='path_to_your_chromedriver')

# Переходим на страницу
url = 'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
driver.get(url)

# Ожидаем загрузки всех изображений
wait = WebDriverWait(driver, 10)
images = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'img')))

# Получаем src третьего изображения
third_image_src = images[2].get_attribute('src')
print("Атрибут src третьей картинки:", third_image_src)

# Закрываем браузер
driver.quit()