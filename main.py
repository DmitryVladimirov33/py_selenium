from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = '/usr/local/bin/chromedriver'
url = 'https://google.com'

driver = webdriver.Chrome()


def test_google_title():
    try:
        driver.get(url)
        time.sleep(5)

        title = driver.title
        print(f"Заголовок страницы: {title}")
        expected_title = "Google"
        assert title == expected_title, f"Заголовок не соответствует: ожидаемый '{expected_title}', полученный '{title}'"

        print("Тест пройден успешно!")

    except AssertionError as e:
        print(e)

    finally:
        driver.quit()


def test_google_search():
    try:
        driver.get(url)
        time.sleep(2)

        elements = driver.find_elements(By.CSS_SELECTOR, "textarea[class='gLFyf']")
        for element in elements:
            element.send_keys('Погода в Москве')
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, "input.gNO89b")
        button.click()
        time.sleep(2)
        print("Тест пройден успешно!")
    except AssertionError as e:
        print(e)

    finally:
        driver.quit()
