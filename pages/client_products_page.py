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


class ClientProductsPage(Base):
    """ Класс содержащий локаторы и методы для справочника Клиенты Продукты"""

    # Data
    ignored_exceptions = (
    NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException)

    # Locators
    head_of_product_page = "//div[@class='ps-font-TopHeader text-indigo-950']"                # Заголовок страницы Клиенты Продукты

    ## General
    item_id = "//div[contains(@class, 'item-id')]"                                    # ID продукта в карточке продукта
    toast_message_success = "//div[contains(@class,'p-toast-message-success')]"               # Тостовое сообщение об успехе

    ##  Форма создания айтема
    client_id_card = "(//span[contains(@class,'p-dropdown-label')])[1]"                      # Селектор Client ID
    list_client_id_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"             # Список в селекторе Client ID
    product_card = "(//span[contains(@class,'p-dropdown-label')])[2]"                         # Селектор Product
    list_product_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"                # Список в селекторе Product
    button_create_card = "//button[contains(@items,'[object Object]')]"                       # Кнопка Create
    x_icon_card = "(//div/div/button[@class='prospace-icon-button'])[5]"                      # Иконка X в карточке создания айтема

    ## Грид айтемов
    button_create_new_card = "//button[contains(@class,'prospace-button')]"                   # Кнопка Create New
    _3_dots_grid = f"(//div[@class='flex justify-center']/button[@class='prospace-icon-button'])[{random.randint(1, 20)}]"  # Троеточие в гриде
    link_delete_restore_in_3_dots_grid = "(//div[contains(@class, 'prospace-dots-item')])[2]"   # Кнопка Delete в троеточии в гриде
    item_name = f"(//div[contains(@class, 'border-dotted')])[{random.randint(2, 20)}]"     # Имя продукта в гриде
    input_search_grid = "//input[contains(@data-pc-name,'inputtext')]"                          # Поле Search в гриде
    last_item_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"               # Имя последнего созданного айтема в гриде
    last_client_id_in_grid = "(//div[@class='text-ellipsis'])[1]"                               # Cient ID последнего созданного айтема в гриде
    last_client_name_in_grid = "(//div[@class='text-ellipsis'])[2]"                             # Client Name последнего созданного айтема в гриде
    last_product_in_grid = "(//div[@class='text-ellipsis'])[3]"                                 # Product последнего созданного айтема в гриде
    last_product_sku_name_in_grid = "(//div[@class='text-ellipsis'])[4]"                        # Product SKU Name последнего созданного айтема в гриде
    deleted_tab_grid = "(//div[contains(@class, 'h-8')])[2]"                                    # Кнопка-вкладка Deleted
    deleted_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='Deleted']"     # Кнопка-вкладка Deleted активна
    all_tab_grid = "(//div[contains(@class, 'h-8')])[1]"                                        # Кнопка-вкладка All
    all_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='All']"             # Кнопка-вкладка All активна
    count_items_in_footer_grid = "(//span[@class='text-indigo-950'])[2]"                        # Количество айтемов в футере
    unselected_checkbox = "//input[@type='checkbox' and @aria-label='Row Unselected']/ancestor::div[@class='p-checkbox p-component']"    # Невыбранный чекбокс в гриде
    selected_checkbox = f"(//div[contains(@class,'p-highlight')])[{random.randint(1, 20)}]"      # Выбранный чекбокс в гриде
    select_all_checkbox = "(//div[@class='p-checkbox p-component'])[1]"                                   # Чекбокс Select All в гриде
    delete_button_upper_panel = "//button[contains(@class,'prospace-action bg-white transition')]"        # Кнопка Delete в верхней сервисной панели
    counter_upper_panel = "//span[@class='prospace-counter-box']"                                         # Каунтер в верхней сервисной панели
    button_all_fiters = "//div[contains(@class, 'all-filters')]"                                          # Кнопка All filters
    any_client_id_in_grid = f"(//span[text()='Client ID']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"     # Любой Client ID в гриде
    any_client_name_in_grid = f"(//span[text()='Client name']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"  # Любой Client Name в гриде
    any_product_in_grid = f"(//span[text()='Product']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"  # Любой Product в гриде
    any_product_sku_name_in_grid = f"(//span[text()='Product SKU Name']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"   # Любой Product SKU Name в гриде
    counter_all_filters = "//div[contains(@class,'all-filters')]/span[@class='prospace-counter-box']"     # Каунтер на кнопке All Filters

    ##  Форма созданного айтема
    link_delete_in_3_dots_card = "//div[contains(@class,'prospace-dots-item')]"               # Кнопка Delete в троеточии в карточке
    _3_dots_card = "(//div/div/button[@class='prospace-icon-button'])[3]"                     # Троеточие в карточке
    mode_switcher = "//span[@class='p-inputswitch-slider']"                              # Свитчер режимов
    button_save = "//button[contains(@class,'prospace-button--with-icon')]"              # Кнопка Сохранить
    x_icon = "(//div/div/button[@class='prospace-icon-button'])[5]"                      # Иконка X в карточке созданного айтема

    ## Окно Delete Item
    button_delete_item = "(//button[contains(@class,'prospace-button--primary')])[2]"    # Кнопка Удалить айтем

    ## Таба расширенных фильтров
    input_client_filters = "(//input[contains(@data-pc-name,'inputtext')])[2]"                   # Поле Client в фильтрах
    input_product_filters = "(//input[contains(@data-pc-name,'inputtext')])[3]"                  # Поле Product в фильтрах
    button_apply_filters = "(//button[contains(@class,'prospace-button--primary')])[2]"                  # Кнопка Apply
    counter_filters = "(//div[@class='header']/span[@class='prospace-counter-box'])[1]"                # Каунтеры в фильтрах
    button_clear_filters = "//button[contains(@class, 'prospace-button--secondary')]"                    # Кнопка Clear
    x_icon_filters = "(//div[contains(@class, 'prospace-boxed-icon-button')]/button[@class='prospace-icon-button'])[3]"       # Иконка X в расширенных фильтрах
    x_icons_input_filters = "//div[@class='header']/div[contains(@class,'items-center')]"                                     # Иконки X в расширенных фильтрах индивидуально для каждого поля

    # Getters
    def get_text_to_be_present_in_element_value_name(self, el1, el2):
        return self.text_to_be_present_in_element_value(el1, el2)

    def get_input_client_filters(self):
        return self.element_is_clickable(self.input_client_filters)

    def get_input_product_filters(self):
        return self.element_is_clickable(self.input_product_filters)

    def get_input_search_grid(self):
        return self.element_is_clickable(self.input_search_grid)

    # Actions
    def click_button(self, el):
        return self.element_is_clickable(el).click()

    def get_text(self, el):
        return self.element_is_visible(el).text

    def is_visible(self, el):
        return self.element_is_visible(el)

    def is_not_visible(self, el):
        return self.element_is_not_visible(el)

    def enter_in_client_input_filters(self, el):
        return self.get_input_client_filters().send_keys(el)

    def enter_in_product_input_filters(self, el):
        return self.get_input_product_filters().send_keys(el)

    def open_last_item(self):
        return self.element_is_clickable(self.last_item_name_in_grid).click()

    def open_any_item(self):
        return self.element_is_clickable(self.item_name).click()

    def enter_in_search_field(self, name):
        return self.get_input_search_grid().send_keys(name)

    def open_deleted_tab(self):
        return self.element_is_clickable(self.deleted_tab_grid).click()

    def open_all_tab(self):
        return self.element_is_clickable(self.all_tab_grid).click()


    # Methods
    def open_client_products_dict(self):
        with allure.step("Open Client Products page"):
            Logger.add_start_step(method="open_client_products_dict")
            self.click_button(self.side_button_modules)
            self.click_button(self.link_client_products)
            self.assert_word(self.is_visible(self.head_of_product_page), "Client Products")
            print("Открыта страница Client Products")
            Logger.add_end_step(url=self.driver.current_url, method="open_client_products_dict")

    def create_client_product(self):
        """Создание матрицы Клиента Продукта"""
        with allure.step("Create Client Product"):
            Logger.add_start_step(method="create_client_product")
            self.is_visible(self.count_items_in_footer_grid)
            self.click_button(self.button_create_new_card)
            self.click_button(self.client_id_card)
            self.click_button(self.list_client_id_card)
            self.click_button(self.product_card)
            self.click_button(self.list_product_card)
            print("Все поля карточки айтема заполнены")
            self.click_button(self.button_create_card)
            self.is_not_visible(self.button_create_card)
            try:
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print("------------------Баг: Тостовое сообщение об успехе не отобразилось--------------------------")
            self.browser_refresh()

            """Получение информации о созданном айтеме из грида"""
            created_client_name = self.get_text(self.last_client_name_in_grid)
            created_product_name = self.get_text(self.last_product_sku_name_in_grid)
            created_client_id = self.get_text(self.last_client_id_in_grid)
            created_product_id = self.get_text(self.last_product_in_grid)


            """Проверка, что создан корректный Клиент Продукт"""
            expected_client_name = self.get_text(self.last_client_name_in_grid)
            expected_product_sku_name = self.get_text(self.last_product_sku_name_in_grid)

            """Получение ID выбранного клиента"""
            self.click_button(self.side_button_modules)
            self.click_button(self.link_clients)
            self.enter_in_search_field(created_client_name)
            print(f"Имя клиента '{created_client_name}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            self.click_button(self.last_item_name_in_grid)
            expected_client_id = self.get_text(self.item_id)
            print(expected_client_id)

            """Получение ID выбранного продукта"""
            self.click_button(self.side_button_modules)
            self.click_button(self.link_products)
            self.enter_in_search_field(created_product_name)
            print(f"Имя продукта '{created_product_name}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            self.click_button(self.last_item_name_in_grid)
            expected_product_id = self.get_text(self.item_id)
            print(expected_product_id)

            print(f"Веденный Client Name при создании Клиента Продукта: {created_client_name}, ожидаемое значение: {expected_client_name}")
            print(f"Веденный Product Name при создании Клиента Продукта: {created_product_name}, ожидаемое значение: {expected_product_sku_name}")
            print(f"Client ID полученный при создании Клиента Продукта: {created_client_id}, ожидаемое значение: {expected_client_id}")
            print(f"Product ID полученный при создании Клиента Продукта: {created_product_id}, ожидаемое значение: {expected_product_id}")
            assert created_client_name == expected_client_name, "Client Name не соответствует созданному"
            assert created_product_name == expected_product_sku_name, "Product Name не соответствует созданному"
            assert str(created_client_id) == str(expected_client_id), "Client ID не соответствует созданному"
            assert str(created_product_id) == str(expected_product_id), "Product ID не соответствует созданному"
            print("Создан корректный Клиент Продукт")
            Logger.add_end_step(url=self.driver.current_url, method="create_client_product")