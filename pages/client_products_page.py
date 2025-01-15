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
    selector_client_id_card = "(//span[contains(@class,'p-dropdown-label')])[1]"                      # Селектор Client ID
    list_client_id_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"             # Список в селекторе Client ID
    selector_product_card = "(//span[contains(@class,'p-dropdown-label')])[2]"                         # Селектор Product
    list_product_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"                # Список в селекторе Product
    button_create_card = "//button[contains(@items,'[object Object]')]"                       # Кнопка Create
    x_icon_card = "(//div/div/button[@class='prospace-icon-button'])[5]"                      # Иконка X в карточке создания айтема
    dropdown = "//li[contains(@class,'p-dropdown-item')]"                                     # Развернутый селектор

    ## Грид айтемов
    button_create_new_card = "//button[contains(@class,'prospace-button')]"                   # Кнопка Create New
    _3_dots_grid = f"(//div[@class='flex justify-center']/button[@class='prospace-icon-button'])[{random.randint(1, 10)}]"  # Троеточие в гриде
    link_delete_restore_in_3_dots_grid = "(//div[contains(@class, 'prospace-dots-item')])[2]"   # Кнопка Delete в троеточии в гриде
    any_item_name = f"(//div[contains(@class, 'border-dotted')])[{random.randint(2, 10)}]"     # Имя продукта в гриде
    input_search_grid = "//input[contains(@data-pc-name,'inputtext')]"                          # Поле Search в гриде
    last_item_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"               # Имя последнего созданного айтема в гриде
    last_client_id_in_grid = "(//div[contains(@class,'text-ellipsis')])[1]"                               # Cient ID последнего созданного айтема в гриде
    last_client_name_in_grid = "(//div[contains(@class,'text-ellipsis')])[2]"                             # Client Name последнего созданного айтема в гриде
    last_product_in_grid = "(//div[contains(@class,'text-ellipsis')])[3]"                                 # Product последнего созданного айтема в гриде
    last_product_sku_name_in_grid = "(//div[contains(@class,'text-ellipsis')])[4]"                        # Product SKU Name последнего созданного айтема в гриде
    deleted_tab_grid = "(//div[contains(@class, 'h-8')])[2]"                                    # Кнопка-вкладка Deleted
    deleted_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='Deleted']"     # Кнопка-вкладка Deleted активна
    all_tab_grid = "(//div[contains(@class, 'h-8')])[1]"                                        # Кнопка-вкладка All
    all_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='All']"             # Кнопка-вкладка All активна
    count_items_in_footer_grid = "(//span[@class='text-indigo-950'])[2]"                        # Количество айтемов в футере
    unselected_checkbox = "//input[@type='checkbox' and @aria-label='Row Unselected']/ancestor::div[@class='p-checkbox p-component']"    # Невыбранный чекбокс в гриде
    selected_checkbox = f"(//div[contains(@class,'p-highlight')])[{random.randint(1, 10)}]"      # Выбранный чекбокс в гриде
    select_all_checkbox = "(//div[@class='p-checkbox p-component'])[1]"                                   # Чекбокс Select All в гриде
    delete_button_upper_panel = "//button[contains(@class,'prospace-action bg-white transition')]"        # Кнопка Delete в верхней сервисной панели
    counter_upper_panel = "//span[@class='prospace-counter-box']"                                         # Каунтер в верхней сервисной панели
    button_all_fiters = "//div[contains(@class, 'all-filters')]"                                          # Кнопка All filters
    any_client_id_in_grid = f"(//span[text()='Client ID']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"     # Любой Client ID в гриде
    any_client_name_in_grid = f"(//span[text()='Client name']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"  # Любой Client Name в гриде
    any_product_in_grid = f"(//span[text()='Product']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"  # Любой Product в гриде
    any_product_sku_name_in_grid = f"(//span[text()='Product SKU Name']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"   # Любой Product SKU Name в гриде
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
        return self.element_is_clickable(self.any_item_name).click()

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
            try:
                self.click_button(self.selector_product_card)
                self.click_button(self.list_product_card)
            except self.ignored_exceptions:
                self.click_button(self.selector_product_card)
                self.click_button(self.list_product_card)
            try:
                self.click_button(self.selector_client_id_card)
                self.click_button(self.list_client_id_card)
            except self.ignored_exceptions:
                self.click_button(self.selector_client_id_card)
                self.click_button(self.list_client_id_card)
            print("Все поля карточки айтема заполнены")

            """Получение информации о созданном айтеме из карточки"""
            created_client_name = self.is_visible(self.selector_client_id_card).get_attribute("aria-label")
            created_product_name = self.is_visible(self.selector_product_card).get_attribute("aria-label")

            self.click_button(self.button_create_card)
            self.is_not_visible(self.button_create_card)
            try:
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print("------------------Баг: Тостовое сообщение об успехе не отобразилось--------------------------")
            self.browser_refresh()

            """Получение информации о созданном айтеме из грида"""
            created_client_id = self.get_text(self.last_client_id_in_grid)
            created_product_id = self.get_text(self.last_product_in_grid)

            """Проверка, что создан корректный Клиент Продукт"""
            expected_client_name = self.get_text(self.last_client_name_in_grid)
            expected_product_sku_name = self.get_text(self.last_product_sku_name_in_grid)

            """Получение ID выбранного клиента"""
            self.click_button(self.side_button_modules)
            self.click_button(self.link_clients)
            self.enter_in_search_field(created_client_name)
            print(f"Имя клиента '{created_client_name}' введено в поле поиска справочника Clients")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            self.click_button(self.last_item_name_in_grid)
            expected_client_id = self.get_text(self.item_id)
            print("ID клиента сохранен")

            """Получение ID выбранного продукта"""
            self.click_button(self.side_button_modules)
            self.click_button(self.link_products)
            self.enter_in_search_field(created_product_name)
            print(f"Имя продукта '{created_product_name}' введено в поле поиска справочника Products")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            item_name = "//div[contains(@class, 'border-dotted')]"
            for item in self.elements_are_present(item_name):
                el = item.text
                print(el)
                if el == created_client_name:
                    item.click()
                    break
            self.click_button(self.last_item_name_in_grid)
            expected_product_id = self.get_text(self.item_id)
            print("ID продукта сохранен")

            print(f"Выбранный Client Name при создании Клиента Продукта: {created_client_name}, значение в гриде: {expected_client_name}")
            print(f"Выбранный Product Name при создании Клиента Продукта: {created_product_name}, значение в гриде: {expected_product_sku_name}")
            print(f"Client ID полученный при создании Клиента Продукта: {created_client_id}, ожидаемое значение: {expected_client_id}")
            print(f"Product ID полученный при создании Клиента Продукта: {created_product_id}, ожидаемое значение: {expected_product_id}")
            assert created_client_name == expected_client_name, "Client Name не соответствует"
            assert created_product_name == expected_product_sku_name, "Product Name не соответствует"
            assert str(created_client_id) == str(expected_client_id), "Client ID не соответствует"
            assert str(created_product_id) == str(expected_product_id), "Product ID не соответствует"
            print("Создана корректная матрица Клиент Продукт")
            Logger.add_end_step(url=self.driver.current_url, method="create_client_product")

    def delete_client_product_from_three_dots_grid(self):
        """Удаление матрицы Клиента Продукта через троеточие в гриде"""
        with allure.step("Delete Client Product using Dots In Grid"):
            Logger.add_start_step(method="delete_client_product_from_three_dots_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self._3_dots_grid)
            self.click_button(self.link_delete_restore_in_3_dots_grid)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении через троеточие в гриде"
            print("Элемент успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_product_from_three_dots_grid")



    def delete_client_product_from_checkbox_grid(self):
        """Удаление матрицы Клиента Продукта через чекбокс в гриде"""
        with allure.step("Delete Client Product using Checkbox in Grid"):
            Logger.add_start_step(method="delete_client_product_from_checkbox_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.element_is_visible(self.unselected_checkbox)
            self.click_button(self.unselected_checkbox)
            count_deleted_items = self.get_text(self.counter_upper_panel)
            self.is_visible(self.delete_button_upper_panel)
            self.click_button(self.delete_button_upper_panel)
            self.invisibility_of_element_located(self.delete_button_upper_panel)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении через чекбокс"
            print("Элемент успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_product_from_checkbox_grid")



    def delete_4_client_product_from_checkbox_grid(self):
        with allure.step("Multiselection Deleted Client Product using Checkboxes in Grid"):
            """Удаление четырех матриц Клиент Продукт через чекбоксы в гриде"""
            Logger.add_start_step(method="delete_4_client_product_from_checkbox_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.element_is_visible(self.unselected_checkbox)
            self.click_button(self.unselected_checkbox)
            count = 0
            while self.get_text(self.counter_upper_panel) != "4":
                self.element_is_visible(self.unselected_checkbox)
                self.click_button(self.unselected_checkbox)
                count += 1
                if count == 10:
                    break
            print(f"Выбрано '{self.get_text(self.counter_upper_panel)}' чекбокса")
            self.is_visible(self.delete_button_upper_panel)
            self.click_button(self.delete_button_upper_panel)
            self.invisibility_of_element_located(self.delete_button_upper_panel)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элементы переместились во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 4, \
                "Ошибка при удалении через чекбоксы"
            print("Элементы успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="delete_4_client_product_from_checkbox_grid")



    def select_all_delete_client_product(self):
        """Массовое удаление матриц Клиент Продукт через Select All в гриде"""
        with allure.step("Delete Client Product using Select All"):
            Logger.add_start_step(method="select_all_delete_client_product")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.element_is_visible(self.select_all_checkbox)
            self.click_button(self.select_all_checkbox)
            count_deleted_items = self.get_text(self.counter_upper_panel)
            print(f"Количество выбранных элементов: {count_deleted_items}")
            self.is_visible(self.delete_button_upper_panel)
            self.click_button(self.delete_button_upper_panel)
            self.invisibility_of_element_located(self.delete_button_upper_panel)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элементы переместились во вкладку Deleted"""
            self.browser_refresh()
            self.element_is_visible(self.count_items_in_footer_grid)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении через Select All"
            print("Элементы успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="select_all_delete_client_product")

    def delete_client_product_from_card(self):
        """Удаление матрицы Клиент Продукт через карточку"""
        with allure.step("Delete Client Product from Card"):
            Logger.add_start_step(method="delete_client_product_from_card")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.open_last_item()
            print("Карточка элемента открыта")
            self.click_button(self._3_dots_card)
            print("Клик на троеточие")
            self.click_button(self.link_delete_in_3_dots_card)
            print("Клик на Delete")
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении через карточку"
            print("Элемент успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_product_from_card")



    def find_client_product_by_sku_name(self):
        """Поиск матрицы Клиент Продукт по Product SKU Name"""
        with allure.step("Find Client Product by Product SKU Name"):
            Logger.add_start_step(method="find_client_product_by_sku_name")
            any_name_in_grid = self.get_text(self.any_product_sku_name_in_grid)
            print(f"Выбранное для поиска имя продукта: {any_name_in_grid}")
            self.enter_in_search_field(any_name_in_grid)
            print(f"Имя продукта '{any_name_in_grid}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break

            """Проверка, что найдена корректная матрица"""
            first_name_in_grid = self.get_text(self.last_product_sku_name_in_grid)
            print(f"Имя первого отображаемого продукта в гриде: {first_name_in_grid}")
            assert str(any_name_in_grid) == str(first_name_in_grid), "Ошибка при поиске или имена продуктов не совпадают"
            print("Найдена корректная матрица")
            Logger.add_end_step(url=self.driver.current_url, method="find_client_product_by_sku_name")


    def find_client_product_by_id(self):
        """Поиск матрицы Клиент Продукт по ID"""
        with allure.step("Find Client Product by ID"):
            Logger.add_start_step(method="find_client_product_by_id")
            any_id = self.get_text(self.any_item_name)
            print(f"Выбранное для поиска ID элемента: {any_id}")
            self.enter_in_search_field(any_id)
            print(f"ID элемента '{any_id}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 60:
                    break

            """Проверка, что найден корректный элемент"""
            first_id = self.get_text(self.last_item_name_in_grid)
            print(f"ID первого отображаемого элемента в гриде: {first_id}")
            assert str(any_id) == str(first_id), "Ошибка при поиске или id не совпадают"
            print("Найден корректный элемент")
            Logger.add_end_step(url=self.driver.current_url, method="find_client_product_by_id")



    def read_client_product(self):
        """Прочесть информацию о найденной матрице Клиент Продукт и сравнить с данными из грида"""
        with allure.step("Read Client Product"):
            """Найти матрицу"""
            Logger.add_start_step(method="read_client_product")
            any_id = self.get_text(self.any_item_name)
            print(f"Выбранное для поиска ID элемента: {any_id}")
            self.enter_in_search_field(any_id)
            print(f"ID элемента '{any_id}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break

            """Получить информацию о найденной матрице Клиент Продукт из грида"""
            grid_client_name = self.get_text(self.last_client_name_in_grid)
            grid_product_sku_name = self.get_text(self.last_product_sku_name_in_grid)

            """Проверка, что информация в правой панели соответствует информации в гриде"""
            self.open_last_item()
            card_client_id = self.get_text(self.selector_client_id_card)
            card_product = self.get_text(self.selector_product_card)
            print(f"Имя клиента в гриде: {grid_client_name}, в карточке: {card_client_id}")
            print(f"Имя продукта в гриде: {grid_product_sku_name}, в карточке: {card_product}")
            assert grid_client_name == card_client_id, "Имена клиентов не совпадают"
            assert grid_product_sku_name == card_product, "Имена продуктов не совпадают"
            print("Информация о матрице Клиент Продукт в карточке соответствует информации о матрице Клиент Продукт в гриде")
            Logger.add_end_step(url=self.driver.current_url, method="read_client_product")



    def restore_client_product_from_three_dots_grid(self):
        """Восстановление матрицы Клиент Продукт из помеченных на удаление через троеточие в гриде"""
        with allure.step("Restore Client Product using Dots in Grid"):
            Logger.add_start_step(method="restore_client_product_from_three_dots_grid")
            self.is_visible(self.count_items_in_footer_grid)
            self.open_deleted_tab()
            self.is_visible(self.deleted_tab_grid_is_active)
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке Deleted до рестора: {count_of_items_before}")
            self.click_button(self._3_dots_grid)
            self.click_button(self.link_delete_restore_in_3_dots_grid)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку All"""
            self.browser_refresh()
            self.open_deleted_tab()
            self.is_visible(self.deleted_tab_grid_is_active)
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке Deleted после рестора: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при восстановлении элемента через троеточие в гриде"
            print("Элемент успешно восстановлен")
            Logger.add_end_step(url=self.driver.current_url, method="restore_client_product_from_three_dots_grid")



    def filters_client_product_by_client(self):
        """Фильтрация матриц Клиент Продукт по имени клиента"""
        with allure.step("Filter Client Products by Client using All Filters"):
            Logger.add_start_step(method="filters_client_product_by_client")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до фильтрации: {count_of_items_before}")
            any_client_name_in_grid = self.get_text(self.any_client_name_in_grid)
            print(f"Выбранное для фильтрации имя клиента: {any_client_name_in_grid}")
            self.click_button(self.button_all_fiters)
            self.enter_in_client_input_filters(any_client_name_in_grid)
            print("Имя клиента введено в поле Client")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            print("Клик Apply")

            """Проверка, что элементы отфильтровались по имени клиента"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All после фильтрации: {count_of_items_after}")
            if count_of_items_after < count_of_items_before:
                last_client_name_in_grid = self.get_text(self.last_client_name_in_grid)
                print(f"Имя первого отображаемого клиента в гриде: {last_client_name_in_grid}")
                counter_all_filters_is_visible = False
                try:
                    counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
                except self.ignored_exceptions:
                    pass
                assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
                assert str(any_client_name_in_grid) == str(last_client_name_in_grid), "Ошибка при фильтрации по имени или имена клиентов не совпадают"
            print("Фильтрация корректна")
            Logger.add_end_step(url=self.driver.current_url, method="filters_client_product_by_client")



    def filters_client_product_by_product(self):
        """Фильтрация матриц Клиент Продукт по имени продукта"""
        with allure.step("Filter Client Products by Product using All Filters"):
            Logger.add_start_step(method="filters_client_product_by_product")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до фильтрации: {count_of_items_before}")
            any_product_name_in_grid = self.get_text(self.any_product_sku_name_in_grid)
            print(f"Выбранное для фильтрации имя клиента: {any_product_name_in_grid}")
            self.click_button(self.button_all_fiters)
            self.enter_in_product_input_filters(any_product_name_in_grid)
            print("Имя клиента введено в поле Client")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            print("Клик Apply")

            """Проверка, что элементы отфильтровались по имени продукта"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All после фильтрации: {count_of_items_after}")
            if count_of_items_after < count_of_items_before:
                last_product_name_in_grid = self.get_text(self.last_product_sku_name_in_grid)
                print(f"Имя первого отображаемого клиента в гриде: {last_product_name_in_grid}")
                counter_all_filters_is_visible = False
                try:
                    counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
                except self.ignored_exceptions:
                    pass
                assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
                assert str(any_product_name_in_grid) == str(last_product_name_in_grid), "Ошибка при фильтрации по имени или имена продуктов не совпадают"
            print("Фильтрация корректна")
            Logger.add_end_step(url=self.driver.current_url, method="filters_client_product_by_product")


    def check_button_clear_filters_client_products(self):
        """Проверить работу кнопки Clear в расширенных фильтрах"""
        with allure.step("Check button Clear in All Filters"):
            Logger.add_start_step(method="check_button_clear_filters_client_products")
            self.click_button(self.button_all_fiters)
            self.enter_in_client_input_filters(random.randint(1, 10))
            self.enter_in_product_input_filters(random.randint(1, 10))
            self.click_button(self.button_clear_filters)
            counters_is_not_visible = False
            try:
                counters_is_not_visible = self.is_not_visible(self.counter_filters)
            except self.ignored_exceptions:
                pass
            if counters_is_not_visible is False:
                self.click_button(self.button_clear_filters)
                print("Повторное нажатие на Clear")
                counters_is_not_visible = True
            assert counters_is_not_visible, "Кнопка Clear расширенных фильтров не работает"
            print("Кнопка Clear расширенных фильтров работает")
            Logger.add_end_step(url=self.driver.current_url, method="check_button_clear_filters_client_products")


    def check_x_icon_filters_client_products(self):
        """Проверить работу кнопки закрытия расширенных фильтров"""
        with allure.step("Check button X in All Filters"):
            Logger.add_start_step(method="check_x_icon_filters_client_products")
            self.click_button(self.button_all_fiters)
            self.enter_in_client_input_filters(random.randint(1, 10))
            self.enter_in_product_input_filters(random.randint(1, 10))
            self.click_button(self.x_icon_filters)
            btn_apply_is_not_visible = False
            try:
                btn_apply_is_not_visible = self.is_not_visible(self.button_apply_filters)
            except self.ignored_exceptions:
                pass
            assert btn_apply_is_not_visible, "Кнопка закрытия расширенных фильтров не работает"
            print("Кнопка закрытия расширенных фильтров работает")
            Logger.add_end_step(url=self.driver.current_url, method="check_x_icon_filters_client_products")



    def check_x_icon_inside_filters_client_products(self):
        """Проверить работу индивидуальных кнопок очисток полей внутри расширенных фильтров"""
        with allure.step("Check individual buttons X in All Filters"):
            Logger.add_start_step(method="check_x_icon_inside_filters_client_products")
            self.click_button(self.button_all_fiters)
            self.enter_in_client_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            self.enter_in_product_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            x_icons_is_not_visible = False
            try:
                x_icons_is_not_visible = self.is_not_visible(self.x_icons_input_filters)
            except self.ignored_exceptions:
                pass
            assert x_icons_is_not_visible, "Индивидуальные кнопки очистки расширенных фильтров не работают"
            print("Индивидуальные кнопки очистки расширенных фильтров работают")
            Logger.add_end_step(url=self.driver.current_url, method="check_x_icon_inside_filters_client_products")