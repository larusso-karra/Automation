from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_click_without_id():
    # Настройка драйвера для Google Chrome
    driver = webdriver.Chrome()
    
    try:
        # Открытие страницы
        driver.get("http://uitestingplayground.com/dynamicid")
        
        # Нахождение синей кнопки
        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
        
        # Кликаем по кнопке
        blue_button.click()
        
    finally:
        # Закрываем браузер после завершения теста
        driver.quit()

if __name__ == "__main__":
    test_click_without_id()