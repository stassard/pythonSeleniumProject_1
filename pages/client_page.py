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
    list_of_affiliations_card = f"//li[@aria-posinset='{random.randint(1, 2)}']"  # Список Affiliations
    # button_upload_file = "//button[contains(@class,'prospace-button--secondary')]"  # Кнопка Upload File
    button_create_card = "//button[contains(@items,'[object Object]')]"  # Кнопка Create
    _3_dots_card = "(//div/div/button[@class='prospace-icon-button'])[4]"  # Троеточие в карточке продукта
    link_delete_in_3_dots_card = "//div[contains(@class,'prospace-dots-item')]"  # Кнопка Delete в троеточии в карточке
    x_icon_card = "(//div/div/button[@class='prospace-icon-button'])[5]"  # Иконка X в карточке создания продукта

    ## Грид продуктов
    _3_dots_grid = "//div[@class='flex justify-center']/button[@class='prospace-icon-button']"  # Троеточия в гриде
    link_delete_restore_in_3_dots_grid = "(//div[contains(@class, 'prospace-dots-item')])[2]"  # Кнопка Delete в троеточии в гриде
    client_name = "//div[contains(@class, 'border-dotted')]"  # Имя клиента в гриде
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
    checkbox = "//input[@type='checkbox' and @aria-label='Row Unselected']/ancestor::div[@class='p-checkbox p-component']"  # Чекбоксы в гриде
    select_all_checkbox = "(//div[@class='p-checkbox p-component'])[1]"  # Чекбокс Select All в гриде
    delete_button_upper_panel = "//button[contains(@class,'prospace-action bg-white transition')]"  # Кнопка Delete в верхней сервисной панели
    counter_upper_panel = "//span[@class='prospace-counter-box']"  # Каунтер в верхней сервисной панели
    button_all_fiters = "//div[contains(@class, 'all-filters')]"  # Кнопка All filters
    any_id_in_grid = "//span[text()='ID']/following-sibling::div[@class='text-ellipsis']"  # ID в гриде
    any_external_id_in_grid = "//span[text()='External ID']/following-sibling::div[@class='text-ellipsis']"  # External ID в гриде
    any_parent_in_grid = "//span[text()='Parent']/following-sibling::div[@class='text-ellipsis']"  # Parent измерения в гриде
    any_type_in_grid = "//span[text()='Type']/following-sibling::div[@class='text-ellipsis']"  # Type в гриде
    any_affiliation_in_grid = "//span[text()='Affiliation']/following-sibling::div[@class='text-ellipsis']"  # Affiliation в гриде
    counter_all_filters = "//div[contains(@class,'all-filters')]/span[@class='prospace-counter-box']"  # Каунтер на кнопке All Filters

    ##  Форма созданного продукта
    mode_switcher = "//span[@class='p-inputswitch-slider']"  # Свитчер режимов
    button_save = "//button[contains(@class,'prospace-button--with-icon')]"  # Кнопка Сохранить
    product_id = "//div[contains(@class, 'item-id')]"  # ID продукта в карточке продукта
    x_icon = "(//div/div/button[@class='prospace-icon-button'])[6]"  # Иконка X в карточке созданного продукта

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