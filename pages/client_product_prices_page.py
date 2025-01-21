import random
import time
import allure
from selenium.webdriver import Keys
from base.base_class import Base
from utilities.logger import Logger
from faker import Faker
import datetime



class ClientProductPricesPage(Base):
    """ Класс содержащий локаторы и методы для справочника Client Product Prices"""

    # Data
    faker_ru = Faker('ru_RU')
    create_date = faker_ru.date_between(start_date='today', end_date='+5y').strftime("%d.%m.%Y")
    update_date = faker_ru.date_between(start_date='today', end_date='+5y').strftime("%d.%m.%Y")
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    create_price = random.randint(1, 1000) / 10
    update_price = random.randint(1, 1000) / 10

    # Locators

    ##  Форма создания айтема
    selector_client_product_id_card = "(//span[contains(@class,'p-dropdown-label')])[1]"  # Селектор Client Product ID
    list_client_product_id_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"  # Список в селекторе Client Product ID
    input_price_card = "(//input[contains(@data-pc-name,'pcinput')])[1]"  # Поле Price
    input_start_date_card = "(//input[contains(@data-pc-name,'pcinput')])[2]"  # Поле Start Date
    input_end_date_card = "(//input[contains(@data-pc-name,'pcinput')])[3]"  # Поле End Date
    placeholders = "//span[contains(@class,'p-placeholder')]"        # Плейсхолдеры в селекторах

    ## Грид айтемов
    last_item_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"  # Имя последнего созданного айтема в гриде
    last_client_product_id_in_grid = "(//div[contains(@class,'text-ellipsis')])[1]"  # Cient Product ID последнего созданного айтема в гриде
    last_price_in_grid = "(//div[contains(@class,'text-ellipsis')])[2]"  # Price последнего созданного айтема в гриде
    last_start_date_in_grid = "(//div[contains(@class,'text-ellipsis')])[3]"  # Start Date последнего созданного айтема в гриде
    last_end_date_in_grid = "(//div[contains(@class,'text-ellipsis')])[4]"  # End Date последнего созданного айтема в гриде
    any_client_product_id_in_grid = f"(//span[text()='Client Product ID']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Client Product ID в гриде
    any_price_in_grid = f"(//span[text()='Price']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Price в гриде
    any_start_date_in_grid = f"(//span[text()='Start Date']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой Start Date в гриде
    any_end_date_in_grid = f"(//span[text()='End Date']/following-sibling::div[@class='text-ellipsis'])[{random.randint(2, 20)}]"  # Любой End Date в гриде

    ##  Форма созданного айтема
    icon_inside_start_date_input = "(//div[contains(@class,'absolute')]/div[contains(@class,'flex')])[1]"   # Иконка крестик/календарь в поле Start Date
    icon_inside_end_date_input = "(//div[contains(@class,'absolute')]/div[contains(@class,'flex')])[2]"     # Иконка крестик/календарь в поле End Date

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
    def enter_in_price_input(self, el):
        return self.get_input_price_card().send_keys(el)
    
    def enter_in_start_date_input(self, el):
        return self.get_input_start_date_card().send_keys(el)

    def enter_in_end_date_input(self, el):
        return self.get_input_end_date_card().send_keys(el)


    # Methods
    def open_client_product_prices_dict(self):
        with allure.step("Open Client Product Prices page"):
            Logger.add_start_step(method="open_client_product_prices_dict")
            self.click_button(self.side_button_modules)
            self.click_button(self.link_client_product_prices)
            self.assert_word(self.is_visible(self.head_of_page), "Client Product Prices")
            print("Открыта страница Client Product Prices")
            Logger.add_end_step(url=self.driver.current_url, method="open_client_product_prices_dict")

    def create_client_product_prices(self):
        """Создание элемента"""
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
            Logger.add_end_step(url=self.driver.current_url, method="create_client_product_prices")



    def read_client_product_prices(self):
        """Прочесть информацию об элементе и сравнить с данными из грида"""
        with allure.step("Read Client Product Prices"):
            Logger.add_start_step(method="read_client_product_prices")
            """Получить информацию об элементе из грида"""
            grid_name_id = self.get_text(self.last_item_name_in_grid)
            grid_client_product_id = self.get_text(self.last_client_product_id_in_grid)
            grid_price = self.get_text(self.last_price_in_grid)
            grid_start_date = self.get_text(self.last_start_date_in_grid)
            grid_end_date = self.get_text(self.last_end_date_in_grid)

            """Проверка, что информация в правой панели соответствует информации в гриде"""
            self.click_button(self.last_item_name_in_grid)
            card_id = self.get_text(self.item_id)
            try:
                self.invisibility_of_element_located(self.placeholders)
                card_client_product_id = self.is_visible(self.selector_client_product_id_card).get_attribute("aria-label")
            except self.ignored_exceptions:
                card_client_product_id = "Отображается плейсхолдер"

            card_price = self.is_visible(self.input_price_card).get_attribute("aria-valuenow")
            card_start_date = self.is_visible(self.input_start_date_card).get_attribute("value")
            card_end_date = self.is_visible(self.input_end_date_card).get_attribute("value")
            print(f"ID-имя в гриде: {grid_name_id}, в карточке: {card_id}")
            print(f"Client Product ID в гриде: {grid_client_product_id}, в карточке: {card_client_product_id}")
            print(f"Price в гриде: {grid_price}, в карточке: {card_price}")
            print(f"Start Date в гриде: {grid_start_date}, в карточке: {card_start_date}")
            print(f"End Date в гриде: {grid_end_date}, в карточке: {card_end_date}")
            assert grid_name_id == card_id, f"ID-имя не совпадает: {grid_name_id} - {card_id}"
            assert grid_client_product_id == card_client_product_id, f"Client Product ID не совпадает: {grid_client_product_id} - {card_client_product_id}"
            assert grid_price == card_price, f"Price не совпадает: {grid_price} - {card_price}"
            assert grid_start_date == card_start_date, f"Start Date не совпадает: {grid_start_date} - {card_start_date}"
            assert grid_end_date == card_end_date, f"End Date не совпадают: {grid_end_date} - {card_end_date}"
            print("Информация в карточке соответствует информации в гриде")
            Logger.add_end_step(url=self.driver.current_url, method="read_client_product_prices")



    def update_client_product_prices(self):
        with allure.step("Update Client Product Prices"):
            Logger.add_start_step(method="update_client_product_prices")
            """Информация о последнем созданном в гриде элементе до апдейта"""
            name_id_before = self.get_text(self.last_item_name_in_grid)
            client_product_id_before = self.get_text(self.last_client_product_id_in_grid)
            price_before = self.get_text(self.last_price_in_grid)
            start_date_before = self.get_text(self.last_start_date_in_grid)
            end_date_before = self.get_text(self.last_end_date_in_grid)

            """Открытие правой панели и редактирование информации"""
            self.click_button(self.last_item_name_in_grid)
            self.click_button(self.mode_switcher)
            self.get_input_price_card().clear()
            self.enter_in_price_input(self.update_price)
            self.click_button(self.icon_inside_start_date_input)
            self.enter_in_start_date_input(self.faker_ru.date_between(start_date='today', end_date='+5y').strftime("%d.%m.%Y"))
            self.get_input_start_date_card().send_keys(Keys.RETURN)
            self.click_button(self.icon_inside_end_date_input)
            self.enter_in_end_date_input(self.faker_ru.date_between(start_date='today', end_date='+5y').strftime("%d.%m.%Y"))
            self.get_input_end_date_card().send_keys(Keys.RETURN)
            self.click_button(self.button_save)
            try:
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print("------------------Баг: Тостовое сообщение об успехе не отобразилось--------------------------")
            time.sleep(3)
            self.click_button(self.x_icon)
            self.is_not_visible(self.x_icon)
            self.browser_refresh()

            """Информация о последнем созданном в гриде элементе после апдейта"""
            name_id_after = self.get_text(self.last_item_name_in_grid)
            client_product_id_after = self.get_text(self.last_client_product_id_in_grid)
            price_after = self.get_text(self.last_price_in_grid)
            start_date_after = self.get_text(self.last_start_date_in_grid)
            end_date_after = self.get_text(self.last_end_date_in_grid)

            """Проверка, что информация об элементе успешно отредактирована"""
            print(f"Имя-id до: {name_id_before}, после: {name_id_after} - не изменялся")
            print(f"Client Product ID до: {client_product_id_before}, после: {client_product_id_after} - не изменялся")
            print(f"Price до: {price_before}, после: {price_after}")
            print(f"Start Date до: {start_date_before}, после: {start_date_after}")
            print(f"End Date до: {end_date_before}, после: {end_date_after}")
            assert name_id_before == name_id_after, f"Имя-id изменилось: {name_id_before} - {name_id_after}"
            assert str(client_product_id_before) == str(client_product_id_after), f"Client Product ID изменился: {str(client_product_id_before)} - {str(client_product_id_after)}"
            assert str(price_before) != str(price_after), f"Price не обновился: {str(price_before)} - {str(price_after)}"
            assert start_date_before != start_date_after, f"Start Date не обновился: {start_date_before} - {start_date_after}"
            assert end_date_before != end_date_after, f"End Date не обновился: {end_date_before} - {end_date_after}"
            print("Элемент успешно отредактирован")
            Logger.add_end_step(url=self.driver.current_url, method="update_client_product_prices")


    def delete_client_product_prices_from_three_dots_grid(self):
        """Удаление элемента через троеточие в гриде"""
        with allure.step("Delete Client Product Prices using Dots In Grid"):
            Logger.add_start_step(method="delete_client_product_prices_from_three_dots_grid")
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
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_product_prices_from_three_dots_grid")


    def delete_client_product_prices_from_checkbox_grid(self):
        """Удаление элемента через чекбокс в гриде"""
        with allure.step("Delete Client Product Prices using Checkbox in Grid"):
            Logger.add_start_step(method="delete_client_product_prices_from_checkbox_grid")
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
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_product_prices_from_checkbox_grid")


    def delete_4_client_product_prices_from_checkbox_grid(self):
        with allure.step("Multiselection Deleted Client Product Prices using Checkboxes in Grid"):
            """Удаление четырех элементов через чекбоксы в гриде"""
            Logger.add_start_step(method="delete_4_client_product_prices_from_checkbox_grid")
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
                "Ошибка при удалении продуктов через чекбоксы"
            print("Элементы успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="delete_4_client_product_prices_from_checkbox_grid")


    def select_all_delete_client_product_prices(self):
        """Массовое удаление элементов через Select All в гриде"""
        with allure.step("Delete Client Product Prices using Select All"):
            Logger.add_start_step(method="select_all_delete_client_product_prices")
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
                "Ошибка при удалении элементов через Select All"
            print("Элементы успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="select_all_delete_client_product_prices")


    def delete_client_product_prices_from_card(self):
        """Удаление элемента через карточку продукта"""
        with allure.step("Delete Client Product Prices from Card"):
            Logger.add_start_step(method="delete_client_product_prices_from_card")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self.last_item_name_in_grid)
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
                "Ошибка при удалении элемента через карточку"
            print("Элемент успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_client_product_prices_from_card")


    def restore_client_product_prices_from_three_dots_grid(self):
        """Восстановление элемента из помеченных на удаление через троеточие в гриде"""
        with allure.step("Restore Client Product Prices using Dots in Grid"):
            Logger.add_start_step(method="restore_client_product_prices_from_three_dots_grid")
            self.is_visible(self.count_items_in_footer_grid)
            self.click_button(self.deleted_tab_grid)
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
            self.is_visible(self.count_items_in_footer_grid)
            self.click_button(self.deleted_tab_grid)
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
            Logger.add_end_step(url=self.driver.current_url, method="restore_client_product_prices_from_three_dots_grid")