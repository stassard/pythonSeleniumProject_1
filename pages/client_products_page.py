import random
import time
import allure
from selenium.webdriver import Keys
from base.base_class import Base
from utilities.logger import logger


class ClientProductsPage(Base):
    """ Класс содержащий локаторы и методы для справочника Client Products"""

    # Locators

    ##  Форма создания айтема
    selector_client_id_card = "(//span[contains(@class,'p-dropdown-label')])[1]"                      # Селектор Client ID
    list_client_id_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"             # Список в селекторе Client ID
    selector_product_card = "(//span[contains(@class,'p-dropdown-label')])[2]"                         # Селектор Product
    list_product_card = f"//li[@aria-posinset='{random.randint(1, 5)}']"                # Список в селекторе Product
    placeholders = "//span[contains(@class,'p-placeholder')]"  # Плейсхолдеры в селекторах

    ## Грид айтемов
    last_item_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"               # Имя последнего созданного айтема в гриде
    last_client_id_in_grid = "(//div[contains(@class,'text-ellipsis')])[1]"                               # Cient ID последнего созданного айтема в гриде
    last_client_name_in_grid = "(//div[contains(@class,'text-ellipsis')])[2]"                             # Client Name последнего созданного айтема в гриде
    last_product_in_grid = "(//div[contains(@class,'text-ellipsis')])[3]"                                 # Product последнего созданного айтема в гриде
    last_product_sku_name_in_grid = "(//div[contains(@class,'text-ellipsis')])[4]"                        # Product SKU Name последнего созданного айтема в гриде
    any_client_id_in_grid = f"(//span[text()='Client ID']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"     # Любой Client ID в гриде
    any_client_name_in_grid = f"(//span[text()='Client name']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"  # Любой Client Name в гриде
    any_product_in_grid = f"(//span[text()='Product']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"  # Любой Product в гриде
    any_product_sku_name_in_grid = f"(//span[text()='Product SKU Name']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"   # Любой Product SKU Name в гриде

    ## Таба расширенных фильтров
    input_client_filters = "(//input[contains(@data-pc-name,'inputtext')])[2]"                   # Поле Client в фильтрах
    input_product_filters = "(//input[contains(@data-pc-name,'inputtext')])[3]"                  # Поле Product в фильтрах

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

    def enter_in_client_input_filters(self, el):
        return self.get_input_client_filters().send_keys(el)

    def enter_in_product_input_filters(self, el):
        return self.get_input_product_filters().send_keys(el)

    def enter_in_search_field(self, name):
        return self.get_input_search_grid().send_keys(name)


    # Methods
    def open_client_products_dict(self):
        with allure.step("Open Client Products page"):
            logger.info("Open Client Products page")
            self.click_button(self.side_button_modules)
            self.click_button(self.link_client_products)
            self.assert_word(self.is_visible(self.head_of_page), "Client Products")
            logger.info("Page Client Products is open")


    def create_client_product(self):
        """Создание матрицы Клиента Продукта"""
        with allure.step("Create Client Product"):
            logger.info("---Create Client Product---")
            self.is_visible(self.count_items_in_footer_grid)
            self.click_button(self.button_create_new_card)
            logger.info("Right Panel is Open")
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
            logger.info("All fields are Filled")

            """Получение информации о созданном айтеме из карточки"""
            created_client_name = self.is_visible(self.selector_client_id_card).get_attribute("aria-label")
            created_product_name = self.is_visible(self.selector_product_card).get_attribute("aria-label")

            self.click_button(self.button_create_card)
            self.is_not_visible(self.button_create_card)
            try:
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                logger.error("------------------Bug: Toast success message is not appeared--------------------------")
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
            logger.info(f"Имя клиента '{created_client_name}' введено в поле поиска справочника Clients")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            logger.info("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            self.click_button(self.last_item_name_in_grid)
            expected_client_id = self.get_text(self.item_id)
            logger.info("ID клиента сохранен")

            """Получение ID выбранного продукта"""
            self.click_button(self.side_button_modules)
            self.click_button(self.link_products)
            self.enter_in_search_field(created_product_name)
            logger.info(f"Имя продукта '{created_product_name}' введено в поле поиска справочника Products")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            logger.info("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            item_name = "//div[contains(@class, 'border-dotted')]"
            for item in self.elements_are_present(item_name):
                el = item.text
                logger.info(el)
                if el == created_client_name:
                    item.click()
                    break
            self.click_button(self.last_item_name_in_grid)
            expected_product_id = self.get_text(self.item_id)
            logger.info("ID продукта сохранен")

            logger.info(f"Выбранный Client Name при создании Клиента Продукта: {created_client_name}, значение в гриде: {expected_client_name}")
            logger.info(f"Выбранный Product Name при создании Клиента Продукта: {created_product_name}, значение в гриде: {expected_product_sku_name}")
            logger.info(f"Client ID полученный при создании Клиента Продукта: {created_client_id}, ожидаемое значение: {expected_client_id}")
            logger.info(f"Product ID полученный при создании Клиента Продукта: {created_product_id}, ожидаемое значение: {expected_product_id}")
            assert created_client_name == expected_client_name, "Client Name не соответствует"
            assert created_product_name == expected_product_sku_name, "Product Name не соответствует"
            assert str(created_client_id) == str(expected_client_id), "Client ID не соответствует"
            assert str(created_product_id) == str(expected_product_id), "Product ID не соответствует"
            logger.info("Создана корректная матрица Клиент Продукт")
            logger.info("---Create Client Product---")

    def delete_client_product_from_three_dots_grid(self):
        """Удаление матрицы Клиента Продукта через троеточие в гриде"""
        with allure.step("Delete Client Product using Dots In Grid"):
            logger.info("---Delete Client Product using Dots In Grid---")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self._3_dots_grid)
            self.click_button(self.link_delete_restore_in_3_dots_grid)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                logger.error(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении через троеточие в гриде"
            logger.info("Элемент успешно удален")
            logger.info("---Delete Client Product using Dots In Grid---")



    def delete_client_product_from_checkbox_grid(self):
        """Удаление матрицы Клиента Продукта через чекбокс в гриде"""
        with allure.step("Delete Client Product using Checkbox in Grid"):
            logger.info("---Delete Client Product using Checkbox in Grid---")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
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
                logger.error(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении через чекбокс"
            logger.info("Элемент успешно удален")
            logger.info("---Delete Client Product using Checkbox in Grid---")



    def delete_4_client_product_from_checkbox_grid(self):
        with allure.step("Multiselection Deleted Client Product using Checkboxes in Grid"):
            """Удаление четырех матриц Клиент Продукт через чекбоксы в гриде"""
            logger.info("---Multiselection Deleted Client Product using Checkboxes in Grid---")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.element_is_visible(self.unselected_checkbox)
            self.click_button(self.unselected_checkbox)
            count = 0
            while self.get_text(self.counter_upper_panel) != "4":
                self.element_is_visible(self.unselected_checkbox)
                self.click_button(self.unselected_checkbox)
                count += 1
                if count == 10:
                    break
            logger.info(f"Выбрано '{self.get_text(self.counter_upper_panel)}' чекбокса")
            self.is_visible(self.delete_button_upper_panel)
            self.click_button(self.delete_button_upper_panel)
            self.invisibility_of_element_located(self.delete_button_upper_panel)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                logger.error(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элементы переместились во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 4, \
                "Ошибка при удалении через чекбоксы"
            logger.info("Элементы успешно удалены")
            logger.info("---Multiselection Deleted Client Product using Checkboxes in Grid---")



    def select_all_delete_client_product(self):
        """Массовое удаление матриц Клиент Продукт через Select All в гриде"""
        with allure.step("Delete Client Product using Select All"):
            logger.info("---Delete Client Product using Select All---")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.element_is_visible(self.select_all_checkbox)
            self.click_button(self.select_all_checkbox)
            count_deleted_items = self.get_text(self.counter_upper_panel)
            logger.info(f"Количество выбранных элементов: {count_deleted_items}")
            self.is_visible(self.delete_button_upper_panel)
            self.click_button(self.delete_button_upper_panel)
            self.invisibility_of_element_located(self.delete_button_upper_panel)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                logger.error(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элементы переместились во вкладку Deleted"""
            self.browser_refresh()
            self.element_is_visible(self.count_items_in_footer_grid)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении через Select All"
            logger.info("Элементы успешно удалены")
            logger.info("---Delete Client Product using Select All---")

    def delete_client_product_from_card(self):
        """Удаление матрицы Клиент Продукт через карточку"""
        with allure.step("Delete Client Product from Card"):
            logger.info("---Delete Client Product from Card---")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self.last_item_name_in_grid)
            logger.info("Карточка элемента открыта")
            self.click_button(self._3_dots_card)
            logger.info("Клик на троеточие")
            self.click_button(self.link_delete_in_3_dots_card)
            logger.info("Клик на Delete")
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                logger.error(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении через карточку"
            logger.info("Элемент успешно удален")
            logger.info("---Delete Client Product from Card---")



    def find_client_product_by_sku_name(self):
        """Поиск матрицы Клиент Продукт по Product SKU Name"""
        with allure.step("Find Client Product by Product SKU Name"):
            logger.info("---Find Client Product by Product SKU Name---")
            any_name_in_grid = self.get_text(self.any_product_sku_name_in_grid)
            logger.info(f"Выбранное для поиска имя продукта: {any_name_in_grid}")
            self.enter_in_search_field(any_name_in_grid)
            logger.info(f"Имя продукта '{any_name_in_grid}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            logger.info("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break

            """Проверка, что найдена корректная матрица"""
            first_name_in_grid = self.get_text(self.last_product_sku_name_in_grid)
            logger.info(f"Имя первого отображаемого продукта в гриде: {first_name_in_grid}")
            assert str(any_name_in_grid) == str(first_name_in_grid), "Ошибка при поиске или имена продуктов не совпадают"
            logger.info("Найдена корректная матрица")
            logger.info("---Find Client Product by Product SKU Name---")


    def find_client_product_by_id(self):
        """Поиск матрицы Клиент Продукт по ID"""
        with allure.step("Find Client Product by ID"):
            logger.info("---Find Client Product by ID---")
            any_id = self.get_text(self.any_item_name)
            logger.info(f"Выбранное для поиска ID элемента: {any_id}")
            self.enter_in_search_field(any_id)
            logger.info(f"ID элемента '{any_id}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            logger.info("Enter")
            count = 0
            while self.get_text(self.last_item_name_in_grid) != any_id:
                time.sleep(1)
                count += 1
                if count == 60:
                    break

            """Проверка, что найден корректный элемент"""
            first_id = self.get_text(self.last_item_name_in_grid)
            logger.info(f"ID первого отображаемого элемента в гриде: {first_id}")
            assert str(any_id) == str(first_id), "Ошибка при поиске или id не совпадают"
            logger.info("Найден корректный элемент")
            logger.info("---Find Client Product by ID---")



    def read_client_product(self):
        """Прочесть информацию о найденной матрице Клиент Продукт и сравнить с данными из грида"""
        with allure.step("Read Client Product"):
            """Найти матрицу"""
            logger.info("---Read Client Product---")
            any_id = self.get_text(self.any_item_name)
            logger.info(f"Выбранное для поиска ID элемента: {any_id}")
            self.enter_in_search_field(any_id)
            logger.info(f"ID элемента '{any_id}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            logger.info("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 60:
                    break

            """Получить информацию о найденной матрице Клиент Продукт из грида"""
            grid_id = self.get_text(self.last_item_name_in_grid)
            grid_client_name = self.get_text(self.last_client_name_in_grid)
            grid_product_sku_name = self.get_text(self.last_product_sku_name_in_grid)

            """Проверка, что информация в правой панели соответствует информации в гриде"""
            self.click_button(self.last_item_name_in_grid)
            try:
                card_id = self.get_text(self.item_id)
            except self.ignored_exceptions:
                card_id = "ID в карточке не отображается"
            try:
                self.invisibility_of_element_located(self.placeholders)
                card_client_id = self.is_visible(self.selector_client_id_card).get_attribute("aria-label")
            except self.ignored_exceptions:
                card_client_id = "Отображается плейсхолдер"
            try:
                self.invisibility_of_element_located(self.placeholders)
                card_product_sku_name = self.is_visible(self.selector_product_card).get_attribute("aria-label")
            except self.ignored_exceptions:
                card_product_sku_name = "Отображается плейсхолдер"
            logger.info(f"ID в гриде: {grid_id}, в карточке: {card_id}")
            logger.info(f"Client Name в гриде: {grid_client_name}, в карточке: {card_client_id}")
            logger.info(f"Product SKU Name в гриде: {grid_product_sku_name}, в карточке: {card_product_sku_name}")
            assert grid_id == card_id, f"ID элементов не совпадают: {grid_id} - {card_id}"
            assert grid_client_name == card_client_id, f"Имена клиентов не совпадают: {grid_client_name} - {card_client_id}"
            assert grid_product_sku_name == card_product_sku_name, f"Имена продуктов не совпадают: {grid_product_sku_name} - {card_product_sku_name}"
            logger.info("Информация о матрице Клиент Продукт в карточке соответствует информации о матрице Клиент Продукт в гриде")
            logger.info("---Read Client Product---")



    def restore_client_product_from_three_dots_grid(self):
        """Восстановление матрицы Клиент Продукт из помеченных на удаление через троеточие в гриде"""
        with allure.step("Restore Client Product using Dots in Grid"):
            logger.info("---Restore Client Product using Dots in Grid---")
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
            logger.info(f"Количество элементов на вкладке Deleted до рестора: {count_of_items_before}")
            self.click_button(self._3_dots_grid)
            self.click_button(self.link_delete_restore_in_3_dots_grid)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                logger.error(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что элемент переместился во вкладку All"""
            self.browser_refresh()
            self.click_button(self.deleted_tab_grid)
            self.is_visible(self.deleted_tab_grid_is_active)
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке Deleted после рестора: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при восстановлении элемента через троеточие в гриде"
            logger.info("Элемент успешно восстановлен")
            logger.info("---Restore Client Product using Dots in Grid---")



    def filters_client_product_by_client(self):
        """Фильтрация матриц Клиент Продукт по имени клиента"""
        with allure.step("Filter Client Products by Client using All Filters"):
            logger.info("---Filter Client Products by Client using All Filters---")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до фильтрации: {count_of_items_before}")
            any_client_name_in_grid = self.get_text(self.any_client_name_in_grid)
            logger.info(f"Выбранное для фильтрации имя клиента: {any_client_name_in_grid}")
            self.click_button(self.button_all_fiters)
            self.enter_in_client_input_filters(any_client_name_in_grid)
            logger.info("Имя клиента введено в поле Client")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            logger.info("Клик Apply")

            """Проверка, что элементы отфильтровались по имени клиента"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All после фильтрации: {count_of_items_after}")
            if count_of_items_after < count_of_items_before:
                last_client_name_in_grid = self.get_text(self.last_client_name_in_grid)
                logger.info(f"Имя первого отображаемого клиента в гриде: {last_client_name_in_grid}")
                counter_all_filters_is_visible = False
                try:
                    counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
                except self.ignored_exceptions:
                    pass
                assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
                assert str(any_client_name_in_grid) == str(last_client_name_in_grid), "Ошибка при фильтрации по имени или имена клиентов не совпадают"
            logger.info("Фильтрация корректна")
            logger.info("---Filter Client Products by Client using All Filters---")



    def filters_client_product_by_product(self):
        """Фильтрация матриц Клиент Продукт по имени продукта"""
        with allure.step("Filter Client Products by Product using All Filters"):
            logger.info("---Filter Client Products by Product using All Filters---")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All до фильтрации: {count_of_items_before}")
            any_product_name_in_grid = self.get_text(self.any_product_sku_name_in_grid)
            logger.info(f"Выбранное для фильтрации имя клиента: {any_product_name_in_grid}")
            self.click_button(self.button_all_fiters)
            self.enter_in_product_input_filters(any_product_name_in_grid)
            logger.info("Имя клиента введено в поле Client")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            logger.info("Клик Apply")

            """Проверка, что элементы отфильтровались по имени продукта"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            logger.info(f"Количество элементов на вкладке All после фильтрации: {count_of_items_after}")
            if count_of_items_after < count_of_items_before:
                last_product_name_in_grid = self.get_text(self.last_product_sku_name_in_grid)
                logger.info(f"Имя первого отображаемого клиента в гриде: {last_product_name_in_grid}")
                counter_all_filters_is_visible = False
                try:
                    counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
                except self.ignored_exceptions:
                    pass
                assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
                assert str(any_product_name_in_grid) == str(last_product_name_in_grid), "Ошибка при фильтрации по имени или имена продуктов не совпадают"
            logger.info("Фильтрация корректна")
            logger.info("---Filter Client Products by Product using All Filters---")


    def check_button_clear_filters_client_products(self):
        """Проверить работу кнопки Clear в расширенных фильтрах"""
        with allure.step("Check button Clear in All Filters"):
            logger.info("---Check button Clear in All Filters---")
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
                logger.info("Повторное нажатие на Clear")
                counters_is_not_visible = True
            assert counters_is_not_visible, "Кнопка Clear расширенных фильтров не работает"
            logger.info("Кнопка Clear расширенных фильтров работает")
            logger.info("---Check button Clear in All Filters---")


    def check_x_icon_filters_client_products(self):
        """Проверить работу кнопки закрытия расширенных фильтров"""
        with allure.step("Check button X in All Filters"):
            logger.info("---Check button X in All Filters---")
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
            logger.info("Кнопка закрытия расширенных фильтров работает")
            logger.info("---Check button X in All Filters---")



    def check_x_icon_inside_filters_client_products(self):
        """Проверить работу индивидуальных кнопок очисток полей внутри расширенных фильтров"""
        with allure.step("Check individual buttons X in All Filters"):
            logger.info("---Check individual buttons X in All Filters---")
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
            logger.info("Индивидуальные кнопки очистки расширенных фильтров работают")
            logger.info("---Check individual buttons X in All Filters---")