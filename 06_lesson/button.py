from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ajax_button_click():
    # Настраиваем драйвер для Google Chrome
    driver = webdriver.Chrome()
    
    try:
        # Открываем страницу
        driver.get("http://uitestingplayground.com/ajax")
        
        # Проверяем, что находимся на нужной странице
        assert driver.title == "Ajax"
        
        # Находим синюю кнопку
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ajaxButton"))
        )
        
        # Нажимаем на кнопку
        button.click()
        
        # Получаем текст из зелёной плашки
        green_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
        ).text
        
        # Выводим текст в консоль
        print(green_text)
        
    finally:
        # Закрываем браузер после завершения теста
        driver.quit()

if __name__ == "__main__":
    test_ajax_button_click()
