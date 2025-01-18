from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_element():
    # Настройка драйвера для Google Chrome
    driver = webdriver.Chrome()
    
    try:
        # Открытие страницы
        driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        
        # Поиск кнопки Add Element
        add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]")
        
        # Пять кликов по кнопке
        for _ in range(5):
            add_button.click()
            time.sleep(1)
            
        # Сбор всех элементов Delete
        delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")
        
        # Вывод размера списка
        print(f"Количество кнопок Delete: {len(delete_buttons)}")
        
    finally:
        # Закрываем браузер после завершения теста
        driver.quit()

if __name__ == "__main__":
    test_add_element()