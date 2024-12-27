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


class ClientPage(Base):
    """ Класс содержащий локаторы и методы для справочника Клиенты"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Data
    ignored_exceptions = (
    NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException)
    create_path_upload = "D:\\PythonEducation\\autoProjectOnlineStore\\files_upload\\магнит.jpg"
    update_path_upload = "D:\\PythonEducation\\autoProjectOnlineStore\\files_upload\\спар.png"
    create_name = f"Test {random.randint(11234, 987659)}"
    update_name = f"Test {random.randint(11234, 987659)}"
    create_external_id = f"Test {random.randint(11234, 987659)}"
    create_parent = f"Parent {random.randint(11234, 987659)}"
    update_parent = f"UPD Parent {random.randint(11234, 987659)}"
    create_type = f"Type {random.randint(11234, 987659)}"
    update_type = f"UPD Type {random.randint(11234, 987659)}"
    create_dispatch_start = random.randint(1, 20)
    update_dispatch_start = random.randint(1, 20)
    create_dispatch_end = random.randint(1, 20)
    update_dispatch_end = random.randint(1, 20)

    # Locators
    head_of_client_page = "//div[@class='ps-font-TopHeader text-indigo-950']"  # Заголовок страницы Клиенты

    ##  Форма создания клиента
    button_create_new_card = "//button[contains(@class,'prospace-button')]"  # Кнопка Create New
    input_name_card = "(//input[contains(@data-pc-name,'inputtext')])[3]"  # Поле Имя клиента
    input_external_id_card = "(//input[contains(@data-pc-name,'inputtext')])[4]"  # Поле External ID
    input_parent_card = "(//input[contains(@data-pc-name,'inputtext')])[5]"  # Поле Parent
    input_type_card = "(//input[contains(@data-pc-name,'inputtext')])[6]"  # Поле Type
    selector_invoice_type_card = "(//span[contains(@class,'p-dropdown-label')])[1]"  # Селектор Invoice Type
    selector_affiliation_card = "(//span[contains(@class,'p-dropdown-label')])[2]"  # Селектор Affiliation
    input_dispatch_start_before_day = "(//input[contains(@data-pc-name,'pcinput')])[1]"  # Поле Dispatch Start Before Day
    input_dispatch_end_before_day = "(//input[contains(@data-pc-name,'pcinput')])[2]"  # Поле Dispatch End Before Day
    list_of_invoice_types_card = f"//li[@aria-posinset='{random.randint(1, 2)}']"  # Список Invoice Types
    on_invoice_type_card = "//li[@aria-posinset='1']"  # Тип Invoice Types - On invoice
    off_invoice_type_card = "//li[@aria-posinset='2']"  # Тип Invoice Types - Off invoice
    list_of_affiliations_card = f"//li[@aria-posinset='{random.randint(1, 2)}']"  # Список Affiliations
    international_affiliation_card = "//li[@aria-posinset='1']"  # Тип Affiliation - International
    local_affiliation_card = "//li[@aria-posinset='2']"  # Тип Affiliation - Local
    button_upload_file = "//input[@type='file']"  # Кнопка Upload File
    button_create_card = "//button[contains(@items,'[object Object]')]"  # Кнопка Create
    _3_dots_card = "(//div/div/button[@class='prospace-icon-button'])[3]"  # Троеточие в карточке продукта
    link_delete_in_3_dots_card = "//div[contains(@class,'prospace-dots-item')]"  # Кнопка Delete в троеточии в карточке
    x_icon_card = "(//div/div/button[@class='prospace-icon-button'])[5]"  # Иконка X в карточке создания продукта
    name_of_added_file = "//span[contains(@class,'text-purple-800')]"     # Имя прикрепленного файла

    ## Грид клиентов
    _3_dots_grid = "//div[@class='flex justify-center']/button[@class='prospace-icon-button']"  # Троеточия в гриде
    link_delete_restore_in_3_dots_grid = "(//div[contains(@class, 'prospace-dots-item')])[2]"  # Кнопка Delete в троеточии в гриде
    client_name = f"(//div[contains(@class, 'border-dotted')])[{random.randint(1, 20)}]"  # Имя клиента в гриде
    input_search_grid = "//input[contains(@data-pc-name,'inputtext')]"  # Поле Search в гриде
    last_client_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"  # Имя последнего созданного клиента в гриде
    last_id_in_grid = "(//div[@class='text-ellipsis'])[1]"  # ID последнего созданного клиента в гриде
    last_external_id_in_grid = "(//div[@class='text-ellipsis'])[2]"  # External ID последнего созданного клиента в гриде
    last_parent_in_grid = "(//div[@class='text-ellipsis'])[3]"  # Parent последнего созданного клиента в гриде
    last_type_in_grid = "(//div[@class='text-ellipsis'])[4]"  # Type последнего созданного клиента в гриде
    last_affiliation_in_grid = "(//div[@class='text-ellipsis'])[5]"  # Affiliation последнего созданного клиента в гриде
    last_invoice_type_in_grid = "(//div[@class='text-ellipsis'])[6]"  # Invoice Type последнего созданного клиента в гриде
    deleted_tab_grid = "(//div[contains(@class, 'h-8')])[2]"  # Кнопка-вкладка Deleted
    deleted_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='Deleted']"  # Кнопка-вкладка Deleted активна
    all_tab_grid = "(//div[contains(@class, 'h-8')])[1]"  # Кнопка-вкладка All
    all_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='All']"  # Кнопка-вкладка All активна
    count_items_in_footer_grid = "(//span[@class='text-indigo-950'])[2]"  # Количество айтемов в футере
    unselected_checkbox = f"(//input[@type='checkbox' and @aria-label='Row Unselected']/ancestor::div[@class='p-checkbox p-component'])[{random.randint(1, 20)}]"  # Чекбоксы в гриде
    selected_checkbox = f"(//div[contains(@class,'p-highlight')])[{random.randint(1, 20)}]"      # Выбранный чекбокс в гриде
    select_all_checkbox = "(//div[@class='p-checkbox p-component'])[1]"  # Чекбокс Select All в гриде
    delete_button_upper_panel = "//button[contains(@class,'prospace-action bg-white transition')]"  # Кнопка Delete в верхней сервисной панели
    counter_upper_panel = "//span[@class='prospace-counter-box']"  # Каунтер в верхней сервисной панели
    button_all_fiters = "//div[contains(@class, 'all-filters')]"  # Кнопка All filters
    any_id_in_grid = f"(//span[text()='ID']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"  # ID в гриде
    any_external_id_in_grid = f"(//span[text()='External ID']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"  # External ID в гриде
    any_parent_in_grid = f"(//span[text()='Parent']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"  # Parent измерения в гриде
    any_type_in_grid = f"(//span[text()='Type']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"  # Type в гриде
    any_affiliation_in_grid = f"(//span[text()='Affiliation']/following-sibling::div[@class='text-ellipsis'])[{random.randint(1, 20)}]"  # Affiliation в гриде
    counter_all_filters = "//div[contains(@class,'all-filters')]/span[@class='prospace-counter-box']"  # Каунтер на кнопке All Filters

    ##  Форма созданного клиента
    mode_switcher = "//span[@class='p-inputswitch-slider']"  # Свитчер режимов
    button_save = "//button[contains(@class,'prospace-button--with-icon')]"  # Кнопка Сохранить
    product_id = "//div[contains(@class, 'item-id')]"  # ID продукта в карточке продукта
    x_icon = "(//div/div/button[@class='prospace-icon-button'])[6]"  # Иконка X в карточке созданного продукта
    value_of_invoice_type_card = "(//span[contains(@class,'p-dropdown-label')]/span)[1]"   # Значение поля Invoice Type
    value_of_affiliation_card = "(//span[contains(@class,'p-dropdown-label')]/span)[2]"   # Значение поля Affiliation

    ## Окно Delete Item
    button_delete_item = "(//button[contains(@class,'prospace-button--primary')])[2]"  # Кнопка Удалить айтем

    ## Таба расширенных фильтров
    input_name_filters = "(//input[contains(@data-pc-name,'inputtext')])[2]"  # Поле Name
    input_type_filters = "(//input[contains(@data-pc-name,'inputtext')])[3]"  # Поле Type
    selector_invoice_type_filters = "(//span[contains(@class,'p-dropdown-label')])[1]"  # Селектор Invoice Type
    selector_affiliation_filters = "(//span[contains(@class,'p-dropdown-label')])[2]"  # Селектор Affiliation
    list_of_invoice_types_filters = f"//li[@aria-posinset='{random.randint(1, 2)}']"  # Список Invoice Types
    list_of_affiliations_filters = f"//li[@aria-posinset='{random.randint(1, 2)}']"  # Список Affiliations
    input_dispatch_start_before_day_from_filters = "(//input[@data-pc-name='pcinput'])[1]"  # Поле Dispatch Start Before Day(From)
    input_dispatch_start_before_day_to_filters = "(//input[@data-pc-name='pcinput'])[2]"  # Поле Dispatch Start Before Day(To)
    input_dispatch_end_before_day_from_filters = "(//input[@data-pc-name='pcinput'])[3]"  # Поле Dispatch End Before Day(From)
    input_dispatch_end_before_day_to_filters = "(//input[@data-pc-name='pcinput'])[4]"  # Поле Dispatch End Before Day(To)
    button_apply_filters = "(//button[contains(@class,'prospace-button--primary')])[2]"  # Кнопка Apply
    counter_filters = "//div[@class='header']/span[@class='prospace-counter-box']"  # Каунтеры в фильтрах
    button_clear_filters = "//button[contains(@class, 'prospace-button--secondary')]"  # Кнопка Clear
    x_icon_filters = "(//div[contains(@class, 'prospace-boxed-icon-button')]/button[@class='prospace-icon-button'])[3]"  # Иконка X в расширенных фильтрах
    x_icons_input_filters = "//div[@class='header']/div[contains(@class,'items-center')]"  # Иконки X в расширенных фильтрах индивидуально для каждого поля

    # Getters
    def upload_file(self, file):
        return self.element_is_present(self.button_upload_file).send_keys(file)

    def get_text_to_be_present_in_element_value_name(self, el1, el2):
        return self.text_to_be_present_in_element_value(el1, el2)

    def get_input_name_card(self):
        return self.element_is_clickable(self.input_name_card)

    def get_input_external_id_card(self):
        return self.element_is_clickable(self.input_external_id_card)

    def get_input_parent_card(self):
        return self.element_is_clickable(self.input_parent_card)

    def get_input_type_card(self):
        return self.element_is_clickable(self.input_type_card)

    def get_input_dispatch_start_before_day(self):
        return self.element_is_clickable(self.input_dispatch_start_before_day)

    def get_input_dispatch_end_before_day(self):
        return self.element_is_clickable(self.input_dispatch_end_before_day)

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


    def enter_in_name_input(self, el):
        return self.get_input_name_card().send_keys(el)

    def enter_in_external_id_input(self, el):
        return self.get_input_external_id_card().send_keys(el)

    def enter_in_parent_input(self, el):
        return self.element_is_clickable(self.input_parent_card).send_keys(el)

    def enter_in_type_input(self, el):
        return self.get_input_type_card().send_keys(el)

    def enter_in_dispatch_start_before_day(self, el):
        return self.get_input_dispatch_start_before_day().send_keys(el)

    def enter_in_dispatch_end_before_day(self, el):
        return self.get_input_dispatch_end_before_day().send_keys(el)

    def open_last_client(self):
        return self.element_is_clickable(self.last_client_name_in_grid).click()

    def open_any_client(self):
        return self.element_is_clickable(self.client_name).click()

    def enter_in_search_field(self, name):
        return self.get_input_search_grid().send_keys(name)

    def open_deleted_tab(self):
        return self.element_is_clickable(self.deleted_tab_grid).click()

    def open_all_tab(self):
        return self.element_is_clickable(self.all_tab_grid).click()

    def enter_in_name_input_filters(self, el):
        return self.element_is_clickable(self.input_name_filters).send_keys(el)

    def enter_in_type_input_filters(self, el):
        return self.element_is_clickable(self.input_type_filters).send_keys(el)

    def enter_in_dispatch_start_before_day_from_input_filters(self, el):
        return self.element_is_clickable(self.input_dispatch_start_before_day_from_filters).send_keys(el)

    def enter_in_dispatch_start_before_day_to_input_filters(self, el):
        return self.element_is_clickable(self.input_dispatch_start_before_day_to_filters).send_keys(el)

    def enter_in_dispatch_end_before_day_from_input_filters(self, el):
        return self.element_is_clickable(self.input_dispatch_end_before_day_from_filters).send_keys(el)

    def enter_in_dispatch_end_before_day_to_input_filters(self, el):
        return self.element_is_clickable(self.input_dispatch_end_before_day_to_filters).send_keys(el)


    # Methods
    def open_clients_dict(self):
        with allure.step("Open Clients page"):
            Logger.add_start_step(method="open_clients_dict")
            self.click_button(self.side_button_modules)
            self.click_button(self.link_clients)
            self.assert_word(self.is_visible(self.head_of_client_page), "Clients")
            print("Открыта страница Clients")
            Logger.add_end_step(url=self.driver.current_url, method="open_clients_dict")

    def create_client(self):
        """Создание клиента"""
        with allure.step("Create Client"):
            Logger.add_start_step(method="create_client")
            self.click_button(self.button_create_new_card)
            self.enter_in_name_input(self.create_name)
            self.enter_in_external_id_input(self.create_external_id)
            self.enter_in_parent_input(self.create_parent)
            self.enter_in_type_input(self.create_type)
            self.click_button(self.selector_invoice_type_card)
            self.click_button(self.list_of_invoice_types_card)
            self.click_button(self.selector_affiliation_card)
            self.click_button(self.list_of_affiliations_card)
            self.get_input_dispatch_start_before_day().clear()
            self.get_input_dispatch_start_before_day().send_keys(random.randint(1, 10))
            self.get_input_dispatch_end_before_day().clear()
            self.get_input_dispatch_end_before_day().send_keys(random.randint(1, 10))
            self.upload_file(self.create_path_upload)
            name_of_added_file = self.get_text(self.name_of_added_file)
            print("Все поля карточки клиента заполнены")
            self.click_button(self.button_create_card)
            self.is_not_visible(self.button_create_card)
            self.browser_refresh()

            """Проверка, что создан корректный клиент"""
            fact_name = self.get_text(self.last_client_name_in_grid)
            fact_external_id = self.get_text(self.last_external_id_in_grid)
            fact_parent = self.get_text(self.last_parent_in_grid)
            fact_type = self.get_text(self.last_type_in_grid)
            print(f"Ожидаемое имя клиента: {self.create_name}, фактическое: {fact_name}")
            print(f"Ожидаемый External ID клиента: {self.create_external_id}, фактический: {fact_external_id}")
            print(f"Ожидаемый Parent клиента: {self.create_parent}, фактический: {fact_parent}")
            print(f"Ожидаемый Type клиента: {self.create_type}, фактический: {fact_type}")
            print(f"Ожидаемое имя загруженного логотипа клиента: магнит.jpg, фактическое: {name_of_added_file}")
            assert self.create_name == fact_name, "Имя клиента не соответствует созданному"
            assert str(self.create_external_id) == str(fact_external_id), "External ID клиента не соответствует созданному"
            assert str(self.create_parent) == str(fact_parent), "Parent клиента не соответствует созданному"
            assert self.create_type == fact_type, "Type клиента не соответствует созданной"
            assert "магнит.jpg" == name_of_added_file, "Имя добавленного файла отображается некорректно"
            print("Создан корректный клиент")
            Logger.add_end_step(url=self.driver.current_url, method="create_client")


    def delete_client_from_three_dots_grid(self):
        """Удаление клиента через троеточие в гриде"""
        with allure.step("Delete Client using Dots In Grid"):
            Logger.add_start_step(method="delete_client_from_three_dots_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self._3_dots_grid)
            self.click_button(self.link_delete_restore_in_3_dots_grid)
            try:
                self.click_button(self.button_delete_item)
            except self.ignored_exceptions:
                print("Баг: Окно подтверждения не отобразилось")

            """Проверка, что клиент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении через троеточие в гриде"
            print("Клиент успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_from_three_dots_grid")



    def delete_client_from_checkbox_grid(self):
        """Удаление клиента через чекбокс в гриде"""
        with allure.step("Delete Client using Checkbox in Grid"):
            Logger.add_start_step(method="delete_client_from_checkbox_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self.unselected_checkbox)
            count_deleted_items = self.get_text(self.counter_upper_panel)
            self.click_button(self.delete_button_upper_panel)
            try:
                self.click_button(self.button_delete_item)
            except self.ignored_exceptions:
                print("Баг: Окно подтверждения не отобразилось")


            """Проверка, что клиент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении клиента через чекбокс"
            print("Клиент успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_from_checkbox_grid")



    def delete_4_clients_from_checkbox_grid(self):
        """Удаление четырех клиентов через чекбоксы в гриде"""
        with allure.step("Multiselection Deleted Clients using Checkboxes in Grid"):
            Logger.add_start_step(method="delete_4_clients_from_checkbox_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All до удаления: {count_of_items_before}")
            self.element_is_visible(self.unselected_checkbox)
            self.click_button(self.unselected_checkbox)
            while self.get_text(self.counter_upper_panel) != "4":
                self.element_is_visible(self.unselected_checkbox)
                self.click_button(self.unselected_checkbox)
            print(f"Выбрано '{self.get_text(self.counter_upper_panel)}' чекбокса")
            self.click_button(self.delete_button_upper_panel)
            try:
                self.element_is_visible(self.button_delete_item)
                self.click_button(self.button_delete_item)
            except self.ignored_exceptions:
                print("Баг: Окно подтверждения не отобразилось")


            """Проверка, что клиенты переместились во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 4, \
                "Ошибка при удалении клиентов через чекбоксы"
            print("Клиенты успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="delete_4_clients_from_checkbox_grid")


    def select_all_delete_client(self):
        """Массовое удаление клиентов через Select All в гриде"""
        with allure.step("Delete Client using Select All"):
            Logger.add_start_step(method="select_all_delete_client")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self.select_all_checkbox)
            count_deleted_items = self.get_text(self.counter_upper_panel)
            print(f"Количество выбранных элементов: {count_deleted_items}")
            self.click_button(self.delete_button_upper_panel)
            try:
                self.click_button(self.button_delete_item)
            except self.ignored_exceptions:
                print("Баг: Окно подтверждения не отобразилось")

            """Проверка, что клиенты переместились во вкладку Deleted"""
            self.browser_refresh()
            self.element_is_visible(self.count_items_in_footer_grid)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении клиентов через Select All"
            print("Клиенты успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="select_all_delete_client")

    def delete_client_from_card(self):
        """Удаление клиента через карточку продукта"""
        with allure.step("Delete Client from Card"):
            Logger.add_start_step(method="delete_client_from_card")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All до удаления: {count_of_items_before}")
            self.open_last_client()
            print("Карточка Клиента открыта")
            self.click_button(self._3_dots_card)
            print("Клик на троеточие")
            self.click_button(self.link_delete_in_3_dots_card)
            print("Клик на Delete")
            try:
                self.click_button(self.button_delete_item)
            except self.ignored_exceptions:
                print("Баг: Окно подтверждения не отобразилось")

            """Проверка, что клиент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество клиентов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении клиента через карточку"
            print("Клиент успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_from_card")


    def find_client_by_name(self):
        """Поиск клиента по имени продукта"""
        with allure.step("Find Client by Name"):
            Logger.add_start_step(method="find_client_by_name")
            any_name_in_grid = self.get_text(self.client_name)
            print(f"Выбранное для поиска имя клиента: {any_name_in_grid}")
            self.enter_in_search_field(any_name_in_grid)
            print(f"Имя клиента '{any_name_in_grid}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")

            """Проверка, что найден корректный клиент"""
            first_name_in_grid = self.get_text(self.client_name)
            print(f"Имя первого отображаемого клиента в гриде: {str(first_name_in_grid)}")
            assert str(any_name_in_grid) == str(
                first_name_in_grid), "Ошибка при поиске или имена клиентов не совпадают"
            print("Найден корректный клиент")
            Logger.add_end_step(url=self.driver.current_url, method="find_client_by_name")


    def find_client_by_id(self):
        """Поиск созданного клиента по ID"""
        with allure.step("Find Client by ID"):
            Logger.add_start_step(method="find_client_by_id")
            any_id = self.get_text(self.any_id_in_grid)
            print(f"Выбранное для поиска ID клиента: {any_id}")
            self.enter_in_search_field(any_id)
            print(f"ID клиента '{any_id}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")

            """Проверка, что найден корректный клиент"""
            first_id = self.get_text(self.any_id_in_grid)
            print(f"ID первого отображаемого клиента в гриде: {first_id}")
            assert str(any_id) == str(first_id), "Ошибка при поиске или id клиентов не совпадают"
            print("Найден корректный клиент")
            Logger.add_end_step(url=self.driver.current_url, method="find_client_by_id")


    """TODO: Продумать изменения в селекторах Affiliation и Invoice Type"""
    def update_client(self):
        with allure.step("Update Client"):
            Logger.add_start_step(method="update_client")
            """Информация о последнем созданном в гриде клиенте до апдейта"""
            id_before = self.is_visible(self.last_id_in_grid).get_attribute("title")
            external_id_before = self.is_visible(self.last_external_id_in_grid).get_attribute("title")
            name_before = self.get_text(self.last_client_name_in_grid)
            parent_before = self.element_is_present(self.last_parent_in_grid).get_attribute("title")
            type_before = self.is_visible(self.last_type_in_grid).get_attribute("title")
            affiliation_before = self.is_visible(self.last_affiliation_in_grid).get_attribute("title")
            invoice_type_before = self.is_visible(self.last_invoice_type_in_grid).get_attribute("title")

            """Открытие правой панели и редактирование информации"""
            self.open_last_client()
            self.click_button(self.mode_switcher)
            self.get_input_name_card().clear()
            self.enter_in_name_input(self.update_name)
            self.get_input_parent_card().clear()
            self.enter_in_parent_input(self.update_parent)
            self.get_input_type_card().clear()
            self.enter_in_type_input(self.update_type)
            if self.get_text(self.value_of_invoice_type_card) == "On Invoice":
                self.click_button(self.selector_invoice_type_card)
                self.click_button(self.off_invoice_type_card)
            else:
                self.click_button(self.selector_invoice_type_card)
                self.click_button(self.on_invoice_type_card)

            if self.get_text(self.value_of_affiliation_card) == "Local":
                self.click_button(self.selector_affiliation_card)
                self.click_button(self.international_affiliation_card)
            else:
                self.click_button(self.selector_affiliation_card)
                self.click_button(self.local_affiliation_card)
            self.get_input_dispatch_start_before_day().clear()
            self.enter_in_dispatch_start_before_day(self.update_dispatch_start)
            self.get_input_dispatch_end_before_day().clear()
            self.enter_in_dispatch_end_before_day(self.update_dispatch_end)
            self.click_button(self.button_save)
            self.click_button(self.x_icon)
            self.is_not_visible(self.x_icon)
            self.browser_refresh()

            """Информация о последнем созданном в гриде клиенте после апдейта"""
            name_after = self.get_text(self.last_client_name_in_grid)
            parent_after = self.element_is_present(self.last_parent_in_grid).get_attribute("title")
            type_after = self.is_visible(self.last_type_in_grid).get_attribute("title")
            affiliation_after = self.is_visible(self.last_affiliation_in_grid).get_attribute("title")
            invoice_type_after = self.is_visible(self.last_invoice_type_in_grid).get_attribute("title")
            id_after = self.is_visible(self.last_id_in_grid).get_attribute("title")
            external_id_after = self.is_visible(self.last_external_id_in_grid).get_attribute("title")

            """Проверка, что информация о продукте успешно отредактирована"""
            print(f"ID клиента до: {id_before}, после: {id_after} - не изменялся")
            print(f"Имя клиента до: {name_before}, после: {name_after}")
            print(f"External ID клиента до: {external_id_before}, после: {external_id_after} - не изменялся")
            print(f"Parent клиента до: {parent_before}, после: {parent_after}")
            print(f"Type клиента до: {type_before}, после: {type_after}")
            print(f"Affiliation клиента до: {affiliation_before}, после: {affiliation_after}")
            print(f"Invoice Type клиента до: {invoice_type_before}, после: {invoice_type_after}")
            assert id_before == id_after, "ID клиента изменился"
            assert name_before != name_after, "Имя клиента не обновилось"
            assert str(external_id_before) == str(external_id_after), "External ID клиента изменился"
            assert parent_before != parent_after, "Parent клиента не обновился"
            assert type_before != type_after, "Type клиента не обновился"
            assert affiliation_before != affiliation_after, "Affiliation клиента не обновился"
            assert invoice_type_before != invoice_type_after, "Invoice Type клиента нне обновился"
            print("Продукт успешно отредактирован")
            Logger.add_end_step(url=self.driver.current_url, method="update_client")