from selenium import webdriver
import pytest

@pytest.fixture(scope="function", autouse=True)
def driver():
    """Настройка открытия и закрытия браузера"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    chrome_options.add_argument('--log-level=1')
    yield driver
    driver.quit()