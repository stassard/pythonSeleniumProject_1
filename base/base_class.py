import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import random


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=30, poll_frequency=1, ignored_exceptions=self.ignored_exceptions)

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException)

    # Locators

    ## General
    toast_message_success = "//div[contains(@class,'p-toast-message-success')]"  # Тостовое сообщение об успехе
    head_of_page = "//div[@class='ps-font-TopHeader text-indigo-950']"  # Заголовок страницы

    ## Menu
    side_button_modules = "(//div[contains(@data-test,'prospace-sidebar-item')])[3]"
    link_products = "//a[text()='Products']"
    link_clients = "//a[text()='Clients']"
    link_client_products = "//a[text()='Client Products']"
    link_client_product_prices = "//a[text()='Client Product Prices']"

    ## Creation Cards
    button_create_new_card = " //button[@aria-label='Create new']"  # Кнопка Create New
    button_create_card = "//button[@aria-label='Create']"  # Кнопка Create
    link_delete_in_3_dots_card = "//div[contains(@class,'prospace-dots-item')]"  # Кнопка Delete в троеточии в карточке
    x_icon_card = "(//div/div/button[@type='icon-secondary'])[5]"  # Иконка X в карточке создания продукта
    dropdown = "//li[contains(@class,'p-dropdown-item')]"   # Выпадающий список

    ## Created Cards
    mode_switcher = "//span[@class='p-inputswitch-slider']"  # Свитчер режимов
    button_save = "//button[@aria-label='Save']"  # Кнопка Сохранить
    _3_dots_card = "(//div/div/button[@type='icon-secondary'])[3]"  # Троеточие в карточке элемента
    item_id = "//div[contains(@class, 'item-id')]"  # ID продукта в карточке элемента
    x_icon = "(//div/div/button[@type='icon-secondary'])[6]"  # Иконка X в карточке созданного элемента
    input_search_grid = "//input[contains(@data-pc-name,'inputtext')]"  # Поле Search в гриде
    deleted_tab_grid = "(//div[contains(@class, 'h-8')])[2]"  # Кнопка-вкладка Deleted
    deleted_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='Deleted']"  # Кнопка-вкладка Deleted активна
    all_tab_grid = "(//div[contains(@class, 'h-8')])[1]"  # Кнопка-вкладка All
    all_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='All']"  # Кнопка-вкладка All активна
    count_items_in_footer_grid = "(//span[@class='text-indigo-950'])[2]"  # Количество айтемов в футере
    unselected_checkbox = "//input[@type='checkbox' and @aria-label='Row Unselected']/ancestor::div[@class='p-checkbox p-component']"  # Невыбранный чекбокс в гриде
    selected_checkbox = f"(//div[contains(@class,'p-highlight')])[{random.randint(1, 10)}]"  # Выбранный чекбокс в гриде
    select_all_checkbox = "(//div[@class='p-checkbox p-component'])[1]"  # Чекбокс Select All в гриде
    delete_button_upper_panel = "//button[@aria-label='Delete']"  # Кнопка Delete в верхней сервисной панели
    counter_upper_panel = "//span[@class='prospace-counter-box']"  # Каунтер в верхней сервисной панели
    button_all_fiters = "//div[contains(@class, 'all-filters')]"  # Кнопка All filters
    counter_all_filters = "//div[contains(@class,'all-filters')]/span[@class='prospace-counter-box']"  # Каунтер на кнопке All Filters

    ## Grid
    button_delete_item = "//button[contains(@aria-label,'Delete item')]"  # Кнопка Удалить элемент
    _3_dots_grid = f"(//div[contains(@class,'flex justify-center')]/div[contains(@class,'flex')])[{random.randint(1, 10)}]"  # Троеточие в гриде
    link_delete_restore_in_3_dots_grid = "(//div[contains(@class, 'prospace-dots-item')])[2]"  # Кнопка Delete в троеточии в гриде
    any_item_name = f"(//div[contains(@class, 'border-dotted')])[{random.randint(2, 10)}]"  # Имя элемента в гриде

    ## Filters
    button_apply_filters = "//button[contains(@aria-label,'Apply')]"  # Кнопка Apply
    counter_filters = "(//div[@class='header']/span[@class='prospace-counter-box'])[1]"  # Каунтеры в фильтрах
    button_clear_filters = "//button[contains(@aria-label, 'Clear')]"  # Кнопка Clear
    x_icon_filters = "(//button[@type='icon-secondary'])[3]"  # Иконка X в расширенных фильтрах
    x_icons_input_filters = "//div[@class='header']/div[contains(@class,'items-center')]"  # Иконки X в расширенных фильтрах индивидуально для каждого поля

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

    def invisibility_of_element_located(self, locator):
        return self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"screens/{name_screenshot}")
        print("Скриншот выполнен")


    def assert_word(self, word, result):
        """Проверка значения текста"""
        value_word = word.text
        assert value_word == result

    def click_button(self, el):
        return self.element_is_clickable(el).click()

    def get_text(self, el):
        return self.element_is_visible(el).text

    def is_visible(self, el):
        return self.element_is_visible(el)

    def is_not_visible(self, el):
        return self.element_is_not_visible(el)

