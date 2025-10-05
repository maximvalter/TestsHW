from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://passport.yandex.ru/auth/add/login"


def try_login(login: str, password: str) -> str:
    """Пробует авторизоваться с логином/паролем и возвращает текст ошибки."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(URL)

    # Вводим логин
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passp-field-login"))
    )
    login_input.send_keys(login)
    login_input.send_keys(Keys.RETURN)

    # Ждём текст ошибки под полем
    error_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".Textinput-Hint_state_error"))
    )
    error_text = error_elem.text

    driver.quit()
    return error_text
