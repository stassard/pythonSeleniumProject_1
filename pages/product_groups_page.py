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



class ProductGroupsPage(Base):
    """ Класс содержащий локаторы и методы для справочника Product Groups"""

    # Locators

    # Окно инициации создания продутковой группы
    input_name_of_element = "(//input[contains(@data-pc-name,'inputtext')])[2]"  # Поле Name
    button_manual = "//div[contains(@aria-label, 'Manual')]"  # Кнопка Manual в окне инициации продуктовой группы
    button_auto = "//div[contains(@aria-label, 'Auto')]"  # Кнопка Auto в окне инициации продуктовой группы
    button_create_in_window = "(//button[contains(@class,'prospace-button--primary')])[2]"  # Кнопка Create в окне инициации создания продуктовой группы
    button_cancel_in_window = "//button[contains(@class,'prospace-button--secondary')]"  # Кнопка Cancel в окне инициации создания продуктовой группы

    ##  Форма создания айтема
    button_add_new_condition_card = "(//button[contains(@class,'prospace-button--secondary')])[2]"   # Кнопка Add new condition
    text_area_card = "//textarea[contains(@class,'p-inputtextarea')]"  # Многострочное текстовое поле
    first_selector_option_card = "(//div[contains(@class,'p-treeselect-trigger')])[1]"   # Первый селектор Option
    second_selector_option_card = "(//div[contains(@class,'p-treeselect-trigger')])[2]"   # Второй селектор Option
    list_option_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"  # Список в селекторе Option
    input_first_value_card = "(//input[contains(@data-pc-name,'inputtext')])[3]"  # Первое поле Value
    input_second_value_card = "(//input[contains(@data-pc-name,'inputtext')])[4]"  # Второе поле Value
    button_first_trashcan_card = "(//div[contains(@class,'mt-[1.6rem]')]/button[contains(@class,'prospace-icon-button')])[1]"   # Первая иконка мусорного бака
    button_second_trashcan_card = "(//div[contains(@class,'mt-[1.6rem]')]/button[contains(@class,'prospace-icon-button')])[2]"   # Вторая иконка мусорного бака

    ## Грид айтемов
    last_item_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"  # Имя последнего созданного айтема в гриде
    last_type_in_grid = "(//div[contains(@class,'text-ellipsis')])[1]"  # Type последнего созданного айтема в гриде
    last_description_in_grid = "(//div[contains(@class,'text-ellipsis')])[2]"  # Description последнего созданного айтема в гриде
    last_counter_products_in_grid = "(//span[contains(@class,'prospace-counter-box')])[2]"  # Каунтер последнего созданного айтема в гриде

    # ------------------------------------------------------------------------------------------
    manual_tab_grid = "(//div[contains(@class, 'h-8')])[3]"  # Кнопка-вкладка Manual
    auto_tab_grid = "(//div[contains(@class, 'h-8')])[2]"  # Кнопка-вкладка Auto
    manual_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='Manual']"  # Кнопка-вкладка Manual активна
    auto_tab_grid_is_active = "//div[contains(@class, 'active')]/span[text()='Auto']"  # Кнопка-вкладка Auto активна
    any_client_product_id_in_grid = f"(//span[text()='Client Product ID']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Client Product ID в гриде
    any_price_in_grid = f"(//span[text()='Price']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Price в гриде
    any_start_date_in_grid = f"(//span[text()='Start Date']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Start Date в гриде
    any_end_date_in_grid = f"(//span[text()='End Date']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой End Date в гриде

    ##  Форма созданного айтема
    icon_inside_start_date_input = "(//span/following-sibling::button[contains(@class,'prospace-icon-button')])[1]"   # Иконка крестик/календарь в поле Start Date
    icon_inside_end_date_input = "(//span/following-sibling::button[contains(@class,'prospace-icon-button')])[2]"     # Иконка крестик/календарь в поле End Date

    ## Таба расширенных фильтров - пока не довезли




    # Actions




    # Methods
    def open_product_groups_dict(self):
        with allure.step("Open Product Groups page"):
            Logger.add_start_step(method="open_product_groups_dict")
            self.click_button(self.side_button_modules)
            self.click_button(self.link_client_product_prices)
            self.assert_word(self.is_visible(self.head_of_page), "Product groups")
            print("Открыта страница Product Groups")
            Logger.add_end_step(url=self.driver.current_url, method="open_product_groups_dict")


    def create_product_groups(self):
        """Создание элемента"""
        with allure.step("Create Product Groups"):
            Logger.add_start_step(method="create_product_groups")
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
            self.enter_in_end_date_input(self.create_date)
            print("Все поля карточки заполнены")

            """Получение информации о созданном элементе из карточки"""
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

            """Проверка, что создан корректный элемент"""
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
            assert created_client_product_id == grid_client_product_id, f"Client Product ID не соответствует созданному: {created_client_product_id} - {grid_client_product_id}"
            assert str(created_price) == str(grid_price), f"Price не соответствует созданному: {str(created_price)} - {str(grid_price)}"
            assert str(created_start_date.replace(' ', '')) == str(grid_start_date), f"Start Date не соответствует созданному: {str(created_start_date.replace(' ', ''))} - {str(grid_start_date)}"
            assert str(created_end_date.replace(' ', '')) == str(grid_end_date), f"End Date не соответствует созданному: {str(created_end_date.replace(' ', ''))} - {str(grid_end_date)}"
            print("Создан корректный элемент")
            Logger.add_end_step(url=self.driver.current_url, method="create_product_groups")