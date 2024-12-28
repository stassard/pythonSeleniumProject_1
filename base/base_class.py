import datetime
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=self.ignored_exceptions)

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException)

    # Locators
    side_button_modules = "(//div[contains(@data-test,'prospace-sidebar-item')])[3]"
    link_products = "//a[text()='Products']"
    link_clients = "//a[text()='Clients']"

    # Actions
    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    #видно все эелементы
    def elements_are_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, locator)))

    #элемент существует в DOM дереве
    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    #элементы существуют в DOM дереве
    def elements_are_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))

    #элемент не видно
    def element_is_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))

    #элемент кликабельный
    def element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    # Текст присутствует в значении элемента
    def text_to_be_present_in_element_value(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element_value((By.XPATH, locator), text))

    def browser_refresh(self):
        return self.driver.refresh()

    def element_is_selected(self, locator):
        return self.wait.until(EC.element_located_selection_state_to_be((By.XPATH, locator), True))

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")


    def assert_word(self, word, result):
        """Проверка значения текста"""
        value_word = word.text
        assert value_word == result

