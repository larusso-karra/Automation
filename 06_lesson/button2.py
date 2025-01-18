from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_rename_button():
    # Настраиваем драйвер для Google Chrome
    driver = webdriver.Chrome()
    
    try:
        # Открываем страницу
        driver.get("http://uitestingplayground.com/textinput")
        
        # Проверяем, что находимся на нужной странице
        assert driver.current_url == "http://uitestingplayground.com/textinput"
        
        # Находим поле ввода
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "newButtonName"))
        )
        
        # Вводим текст в поле
        input_field.send_keys("SkyPro")
        
        # Находим синюю кнопку
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "updatingButton"))
        )
        
        # Нажимаем на кнопку
        button.click()
        
        # Получаем новый текст кнопки
        new_button_text = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_value((By.ID, "updatingButton"), "SkyPro")
        )
        
        # Выводим текст кнопки в консоль
        print(new_button_text)
        
    finally:
        # Закрываем браузер после завершения теста
        driver.quit()

if __name__ == "__main__":
    test_rename_button()
