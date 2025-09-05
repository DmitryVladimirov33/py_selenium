import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://google.com'


@pytest.fixture
def open_form(browser):
    browser.get(url)
    yield
    browser.quit()


def test_google_title(browser, open_form):
    try:
        title = browser.title
        print(f"Заголовок страницы: {title}")
        expected_title = "Google"
        assert title == expected_title, f"Заголовок не соответствует: ожидаемый '{expected_title}', полученный '{title}'"

        print("Тест пройден успешно!")

    except AssertionError as e:
        print(e)


def test_google_search(browser, open_form):
    try:
        elements = browser.find_elements(By.CSS_SELECTOR, "textarea[class='gLFyf']")
        for element in elements:
            element.send_keys('Погода в Москве')
        time.sleep(1)
        button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input.gNO89b")))
        button.click()
        time.sleep(2)
        print("Тест пройден успешно!")
    except AssertionError as e:
        print(e)
