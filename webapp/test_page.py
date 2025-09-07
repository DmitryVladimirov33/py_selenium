import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'http://127.0.0.1:8000/'


@pytest.fixture
def open_form(browser):
    browser.get(url)
    yield
    browser.quit()


def test_google_title(browser, open_form):
    title = browser.title
    print(f"Заголовок страницы: {title}")
    expected_title = "Приветствие"
    assert title == expected_title, f"Заголовок не соответствует: ожидаемый '{expected_title}', полученный '{title}'"
    print("Тест пройден успешно!")


def test_google_search(browser, open_form):
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type=text]")
    for element in elements:
        element.send_keys('Пользователь')
    time.sleep(1)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
    button.click()
    time.sleep(2)
    h1_element = browser.find_element(By.CSS_SELECTOR, "body > h1")
    assert h1_element.text == "Привет, Пользователь!"
    print("Тест пройден успешно!")
