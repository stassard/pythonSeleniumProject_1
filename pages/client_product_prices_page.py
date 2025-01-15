import random
import time
import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from base.base_class import Base
from utilities.logger import Logger
from faker import Faker
import datetime



class ClientProductPricesPage(Base):
    """ Класс содержащий локаторы и методы для справочника Клиенты Продукты Цены"""

    # Data
    fake = Faker()
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    future_date = f"{random.randint(1, 20)}.{random.randint(1, 12)}.{random.randint(datetime.datetime.now().year + 1, 2030)} "
    ignored_exceptions = (
    NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException)
    create_price = random.randint(1, 1000) / 10

    # Locators
    head_of_product_page = "//div[@class='ps-font-TopHeader text-indigo-950']"                # Заголовок страницы Клиенты Продукты Цены

    ## General
    item_id = "//div[contains(@class, 'item-id')]"  # ID продукта в карточке продукта
    toast_message_success = "//div[contains(@class,'p-toast-message-success')]"  # Тостовое сообщение об успехе

    ##  Форма создания айтема
    selector_client_product_id_card = "(//span[contains(@class,'p-dropdown-label')])[1]"  # Селектор Client Product ID
    list_client_product_id_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"  # Список в селекторе Client Product ID
    input_price_card = "(//input[contains(@data-pc-name,'pcinput')])[1]"  # Поле Price
    input_start_date_card = "(//input[contains(@data-pc-name,'pcinput')])[2]"  # Поле Start Date
    input_end_date_card = "(//input[contains(@data-pc-name,'pcinput')])[3]"  # Поле End Date
    button_create_card = "//button[contains(@items,'[object Object]')]"  # Кнопка Create
    x_icon_card = "(//div/div/button[@class='prospace-icon-button'])[5]"  # Иконка X в карточке создания айтема
    placeholders = "//span[contains(@class,'p-placeholder')]"        # Плейсхолдеры в селекторах

    ## Грид айтемов
    button_create_new_card = "//button[contains(@class,'prospace-button')]"  # Кнопка Create New
    _3_dots_grid = f"(//div[@class='flex justify-center']/button[@class='prospace-icon-button'])[{random.randint(1, 20)}]"  # Троеточие в гриде
    link_delete_restore_in_3_dots_grid = "(//div[contains(@class, 'prospace-dots-item')])[2]"  # Кнопка Delete в троеточии в гриде
    any_item_name = f"(//div[contains(@class, 'border-dotted')])[{random.randint(2, 20)}]"  # Имя айтема в гриде
    input_search_grid = "//input[contains(@data-pc-name,'inputtext')]"  # Поле Search в гриде
    last_item_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"  # Имя последнего созданного айтема в гриде
    last_client_product_id_in_grid = "(//div[contains(@class,'text-ellipsis')])[1]"  # Cient Product ID последнего созданного айтема в гриде
    last_price_in_grid = "(//div[contains(@class,'text-ellipsis')])[2]"  # Price последнего созданного айтема в гриде
    last_start_date_in_grid = "(//div[contains(@class,'text-ellipsis')])[3]"  # Start Date последнего созданного айтема в гриде
    last_end_date_in_grid = "(//div[contains(@class,'text-ellipsis')])[4]"  # End Date последнего созданного айтема в гриде
    deleted_tab_grid = "(//div[contains(@class, 'h-8')])[2]"  # Кнопка-вкладка Deleted
    deleted_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='Deleted']"  # Кнопка-вкладка Deleted активна
    all_tab_grid = "(//div[contains(@class, 'h-8')])[1]"  # Кнопка-вкладка All
    all_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='All']"  # Кнопка-вкладка All активна
    count_items_in_footer_grid = "(//span[@class='text-indigo-950'])[2]"  # Количество айтемов в футере
    unselected_checkbox = "//input[@type='checkbox' and @aria-label='Row Unselected']/ancestor::div[@class='p-checkbox p-component']"  # Невыбранный чекбокс в гриде
    selected_checkbox = f"(//div[contains(@class,'p-highlight')])[{random.randint(1, 20)}]"  # Выбранный чекбокс в гриде
    select_all_checkbox = "(//div[@class='p-checkbox p-component'])[1]"  # Чекбокс Select All в гриде
    delete_button_upper_panel = "//button[contains(@class,'prospace-action bg-white transition')]"  # Кнопка Delete в верхней сервисной панели
    counter_upper_panel = "//span[@class='prospace-counter-box']"  # Каунтер в верхней сервисной панели
    button_all_fiters = "//div[contains(@class, 'all-filters')]"  # Кнопка All filters
    any_client_product_id_in_grid = f"(//span[text()='Client Product ID']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Client Product ID в гриде
    any_price_in_grid = f"(//span[text()='Price']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Price в гриде
    any_start_date_in_grid = f"(//span[text()='Start Date']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Start Date в гриде
    any_end_date_in_grid = f"(//span[text()='End Date']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой End Date в гриде
    counter_all_filters = "//div[contains(@class,'all-filters')]/span[@class='prospace-counter-box']"  # Каунтер на кнопке All Filters

    ##  Форма созданного айтема
    link_delete_in_3_dots_card = "//div[contains(@class,'prospace-dots-item')]"  # Кнопка Delete в троеточии в карточке
    _3_dots_card = "(//div/div/button[@class='prospace-icon-button'])[3]"  # Троеточие в карточке
    mode_switcher = "//span[@class='p-inputswitch-slider']"  # Свитчер режимов
    button_save = "//button[contains(@class,'prospace-button--with-icon')]"  # Кнопка Сохранить
    x_icon = "(//div/div/button[@class='prospace-icon-button'])[5]"  # Иконка X в карточке созданного айтема

    ## Окно Delete Item
    button_delete_item = "(//button[contains(@class,'prospace-button--primary')])[2]"  # Кнопка Удалить айтем

    ## Таба расширенных фильтров - пока не довезли

    # Getters
    def get_input_price_card(self):
        return self.element_is_clickable(self.input_price_card)

    def get_input_start_date_card(self):
        return self.element_is_clickable(self.input_start_date_card)

    def get_input_end_date_card(self):
        return self.element_is_clickable(self.input_end_date_card)

    def get_input_search_grid(self):
        return self.element_is_clickable(self.input_search_grid)

    # Actions
    def click_button(self, el):
        return self.element_is_clickable(el).click()

    def is_visible(self, el):
        return self.element_is_visible(el)

    def enter_in_price_input(self, el):
        return self.get_input_price_card().send_keys(el)
    
    def enter_in_start_date_input(self, el):
        return self.get_input_start_date_card().send_keys(el)

    def enter_in_end_date_input(self, el):
        return self.get_input_end_date_card().send_keys(el)

    def is_not_visible(self, el):
        return self.element_is_not_visible(el)

    def get_text(self, el):
        return self.element_is_visible(el).text

    def enter_in_search_field(self, name):
        return self.get_input_search_grid().send_keys(name)


    # Methods
    def open_client_product_prices_dict(self):
        with allure.step("Open Client Product Prices page"):
            Logger.add_start_step(method="open_client_product_prices_dict")
            self.click_button(self.side_button_modules)
            self.click_button(self.link_client_product_prices)
            self.assert_word(self.is_visible(self.head_of_product_page), "Client Product Prices")
            print("Открыта страница Client Product Prices")
            Logger.add_end_step(url=self.driver.current_url, method="open_client_product_prices_dict")

    def create_client_product_prices(self):
        """Создание цены"""
        with allure.step("Create Client Product Prices"):
            Logger.add_start_step(method="create_client_product_prices")
            self.is_visible(self.count_items_in_footer_grid)
            self.click_button(self.button_create_new_card)
            try:
                self.click_button(self.selector_client_product_id_card)
                self.click_button(self.list_client_product_id_card)
            except self.ignored_exceptions:
                self.click_button(self.selector_client_product_id_card)
                self.click_button(self.list_client_product_id_card)
            self.enter_in_price_input(self.create_price)
            self.enter_in_start_date_input(self.current_date)
            self.enter_in_end_date_input(self.future_date)
            print("Все поля карточки заполнены")

            """Получение информации о созданном айтеме из карточки"""
            created_client_product_id = self.is_visible(self.selector_client_product_id_card).get_attribute("aria-label")
            created_price = self.is_visible(self.input_price_card).get_attribute("aria-valuenow")
            created_start_date = self.is_visible(self.input_start_date_card).get_attribute("value")
            created_end_date = self.is_visible(self.input_end_date_card).get_attribute("value")

            self.click_button(self.button_create_card)
            self.is_not_visible(self.button_create_card)
            try:
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print("------------------Баг: Тостовое сообщение об успехе не отобразилось--------------------------")
            self.browser_refresh()

            """Проверка, что создана корректная цена"""
            grid_client_product_id = self.get_text(self.last_client_product_id_in_grid)
            grid_price = self.get_text(self.last_price_in_grid)
            grid_start_date = self.get_text(self.last_start_date_in_grid)
            grid_end_date = self.get_text(self.last_end_date_in_grid)
            print(
                f"Выбранный Client Product ID при создании: {created_client_product_id}, значение последнего созданного значения айтема в гриде: {grid_client_product_id}")
            print(
                f"Веденный Price при создании: {created_price}, значение последнего созданного значения айтема в гриде: {grid_price}")
            print(
                f"Веденный Start Date при создании: {created_start_date.replace(' ', '')}, значение последнего созданного продукта: {grid_start_date}")
            print(
                f"Веденный End Date при создании: {created_end_date.replace(' ', '')}, значение последнего созданного продукта: {grid_end_date}")
            assert created_client_product_id == grid_client_product_id, "Client Product ID не соответствует созданному"
            assert str(created_price) == str(grid_price), "Price не соответствует созданному"
            assert str(created_start_date.replace(' ', '')) == str(grid_start_date), "Start Date не соответствует созданному"
            assert str(created_end_date.replace(' ', '')) == str(grid_end_date), "End Date не соответствует созданному"
            print("Создана корректная цена")
            Logger.add_end_step(url=self.driver.current_url, method="create_client_product_prices")



    def read_client_product_prices(self):
        """Прочесть информацию о найденной цене и сравнить с данными из грида"""
        with allure.step("Read Client Product Prices"):
            """Найти цену"""
            Logger.add_start_step(method="read_client_product_prices")
            """Получить информацию о найденной цене из грида"""
            grid_name_id = self.get_text(self.last_item_name_in_grid)
            grid_client_product_id = self.get_text(self.last_client_product_id_in_grid)
            grid_price = self.get_text(self.last_price_in_grid)
            grid_start_date = self.get_text(self.last_start_date_in_grid)
            grid_end_date = self.get_text(self.last_end_date_in_grid)

            """Проверка, что информация в правой панели соответствует информации в гриде"""
            self.click_button(self.last_item_name_in_grid)
            self.click_button(self.mode_switcher)
            card_id = self.get_text(self.item_id)
            try:
                self.invisibility_of_element_located(self.placeholders)
                card_client_product_id = self.is_visible(self.selector_client_product_id_card).get_attribute("aria-label")
            except self.ignored_exceptions:
                card_client_product_id = "Отображается плейсхолдер"

            card_price = self.is_visible(self.input_price_card).get_attribute("aria-valuenow")
            card_start_date = self.get_text(self.input_start_date_card)
            card_end_date = self.get_text(self.input_start_date_card)
            print(f"ID-имя в гриде: {grid_name_id}, в карточке: {card_id}")
            print(f"Client Product ID в гриде: {grid_client_product_id}, в карточке: {card_client_product_id}")
            print(f"Price в гриде: {grid_price}, в карточке: {card_price}")
            print(f"Start Date в гриде: {grid_start_date}, в карточке: {card_start_date}")
            print(f"End Date в гриде: {grid_end_date}, в карточке: {card_end_date}")
            assert grid_name_id == card_id, "ID-имя не совпадает"
            assert grid_client_product_id == card_client_product_id, "Client Product ID не совпадает"
            assert grid_price == card_price, "Price не совпадает"
            assert grid_start_date == card_start_date, "Start Date не совпадает"
            assert grid_end_date == card_end_date, "End Date не совпадают"
            print("Информация в карточке соответствует информации в гриде")
            Logger.add_end_step(url=self.driver.current_url, method="read_client_product_prices")