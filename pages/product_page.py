import random
import time
import allure
from selenium.webdriver import Keys
from base.base_class import Base
from utilities.logger import Logger


class ProductPage(Base):
    """ Класс содержащий локаторы и методы для справочника Продукты"""

    # Data
    create_name = f"Test {random.randint(11234, 98765)}"
    update_name = f"UPD Test {random.randint(11234, 98765)}"
    create_eanc = random.randint(11234, 98765)
    update_eanc = random.randint(11234, 98765)
    create_eanp = random.randint(11234, 98765)
    update_eanp = random.randint(11234, 98765)
    create_category = f"Category {random.randint(11234, 98765)}"
    update_category = f"UPD Category {random.randint(11234, 98765)}"
    create_technology = f"Technology {random.randint(11234, 98765)}"
    update_technology = f"UPD Technology {random.randint(11234, 98765)}"
    create_brand = f"Brand {random.randint(11234, 98765)}"
    update_brand = f"UPD Brand {random.randint(11234, 98765)}"
    create_unit = random.randint(1, 100) / 10
    update_unit = random.randint(1, 100) / 10

    # Locators

    ##  Форма создания продукта
    input_name_card = "(//input[contains(@data-pc-name,'inputtext')])[3]"                     # Поле Имя продукта
    input_EANC_card = "(//input[contains(@data-pc-name,'inputtext')])[4]"                     # Поле EANC
    input_EANP_card = "(//input[contains(@data-pc-name,'inputtext')])[5]"                     # Поле EANC
    input_category_card = "(//input[contains(@data-pc-name,'inputtext')])[6]"                 # Поле Category
    input_technology_card = "(//input[contains(@data-pc-name,'inputtext')])[7]"               # Поле Technology
    input_brand_card = "(//input[contains(@data-pc-name,'inputtext')])[8]"                    # Поле Brand
    unit_of_measure_card = "//span[contains(@class,'p-dropdown-label')]"                      # Селектор Unit of Measure
    units_of_measure_selector_card = f"(//li[contains(@class,'p-dropdown-item')])[{random.randint(1, 6)}]"           # Список Unit of Measure
    input_unit_card = "//input[contains(@data-pc-name,'pcinput')]"                            # Поле Unit

    ## Грид продуктов
    last_prod_name_in_grid = "(//div[contains(@class,'border-b-purple-400')])[1]"               # Имя последнего созданного продукта в гриде
    last_eanc_in_grid = "(//div[contains(@class,'text-ellipsis')])[1]"                                    # EAN Case последнего созданного продукта в гриде
    last_eanp_in_grid = "(//div[contains(@class,'text-ellipsis')])[2]"                                    # EAN Pc последнего созданного продукта в гриде
    last_category_in_grid = "(//div[contains(@class,'text-ellipsis')])[3]"                                # Категория последнего созданного продукта в гриде
    last_technology_in_grid = "(//div[contains(@class,'text-ellipsis')])[4]"                              # Технология последнего созданного продукта в гриде
    last_brand_in_grid = "(//div[contains(@class,'text-ellipsis')])[5]"                                   # Бренд последнего созданного продукта в гриде
    last_unit_in_grid = "(//div[contains(@class,'text-ellipsis')])[7]"                                    # Юнит последнего созданного продукта в гриде
    last_unit_of_measure_in_grid = "(//span[text()='Unit Of Measure']/following-sibling::div[contains(@class,'text-ellipsis')])[1]"      # Единица измерения последнего созданного продукта в гриде
    any_category_in_grid = f"(//span[text()='Category']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"     # Категория в гриде
    any_brand_in_grid = f"(//span[text()='Brand']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"           # Бренд в гриде
    any_unit_of_measure_in_grid = f"(//span[text()='Unit Of Measure']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"  # Единица измерения в гриде
    any_unit_in_grid = f"(//span[text()='Unit']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"             # Юнит в гриде
    any_technology_in_grid = f"(//span[text()='Technology']/following-sibling::div[contains(@class,'text-ellipsis')])[{random.randint(2, 10)}]"     # Технология в гриде

    ##  Форма созданного продукта
    value_of_unit_of_measure_card = "//span[contains(@class,'p-dropdown-label')]/span"   # Значение поля Unit of Measure

    ## Таба расширенных фильтров
    input_sku_name_filters = "(//input[contains(@data-pc-name,'inputtext')])[2]"                 # Поле SKU Name
    input_category_filters = "(//input[contains(@data-pc-name,'inputtext')])[3]"                 # Поле Category
    input_technology_filters = "(//input[contains(@data-pc-name,'inputtext')])[4]"               # Поле Technology
    input_brand_filters = "(//input[contains(@data-pc-name,'inputtext')])[5]"                    # Поле Brand
    input_unit_of_measure_filters = "(//input[contains(@data-pc-name,'inputtext')])[6]"          # Поле Unit of Measure
    input_unit_from_filters = "(//input[@data-pc-name='pcinput'])[1]"                            # Поле Unit(From)
    input_unit_to_filters = "(//input[@data-pc-name='pcinput'])[2]"                              # Поле Unit(To)

    # Getters
    def get_text_to_be_present_in_element_value_name(self, el1, el2):
        return self.text_to_be_present_in_element_value(el1, el2)

    def get_input_name_card(self):
        return self.element_is_clickable(self.input_name_card)

    def get_input_EANC_card(self):
        return self.element_is_clickable(self.input_EANC_card)

    def get_input_category_card(self):
        return self.element_is_clickable(self.input_category_card)

    def get_input_technology_card(self):
        return self.element_is_clickable(self.input_technology_card)

    def get_input_brand_card(self):
        return self.element_is_clickable(self.input_brand_card)

    def get_input_unit_card(self):
        return self.element_is_clickable(self.input_unit_card)

    def get_input_search_grid(self):
        return self.element_is_clickable(self.input_search_grid)

    # Actions

    def enter_in_name_input(self, el):
        return self.get_input_name_card().send_keys(el)

    def enter_in_eanc_input(self, el):
        return self.get_input_EANC_card().send_keys(el)

    def enter_in_eanp_input(self, el):
        return self.element_is_clickable(self.input_EANP_card).send_keys(el)

    def enter_in_category_input(self, el):
        return self.get_input_category_card().send_keys(el)

    def enter_in_technology_input(self, el):
        return self.get_input_technology_card().send_keys(el)

    def enter_in_brand_input(self, el):
        return self.get_input_brand_card().send_keys(el)

    def enter_in_unit_input(self, el):
        return self.get_input_unit_card().send_keys(el)

    def enter_in_search_field(self, name):
        return self.get_input_search_grid().send_keys(name)


    def enter_in_sku_name_input_filters(self, el):
        return self.element_is_clickable(self.input_sku_name_filters).send_keys(el)

    def enter_in_category_input_filters(self, el):
        return self.element_is_clickable(self.input_category_filters).send_keys(el)

    def enter_in_brand_input_filters(self, el):
        return self.element_is_clickable(self.input_brand_filters).send_keys(el)

    def enter_in_technology_input_filters(self, el):
        return self.element_is_clickable(self.input_technology_filters).send_keys(el)

    def enter_in_unit_of_measure_input_filters(self, el):
        return self.element_is_clickable(self.input_unit_of_measure_filters).send_keys(el)

    def enter_in_unit_from_input_filters(self, el):
        return self.element_is_clickable(self.input_unit_from_filters).send_keys(el)

    def enter_in_unit_to_input_filters(self, el):
        return self.element_is_clickable(self.input_unit_to_filters).send_keys(el)


    # Methods
    def open_products_dict(self):
        with allure.step("Open Products page"):
            Logger.add_start_step(method="open_products_dict")
            self.click_button(self.side_button_modules)
            self.click_button(self.link_products)
            self.assert_word(self.is_visible(self.head_of_page), "Products")
            print("Открыта страница Products")
            Logger.add_end_step(url=self.driver.current_url, method="open_products_dict")


    def create_product(self):
        """Создание продукта"""
        with allure.step("Create Product"):
            Logger.add_start_step(method="create_product")
            self.click_button(self.button_create_new_card)
            self.enter_in_name_input(self.create_name)
            self.enter_in_eanc_input(self.create_eanc)
            self.enter_in_eanp_input(self.create_eanp)
            self.enter_in_category_input(self.create_category)
            self.enter_in_technology_input(self.create_technology)
            self.enter_in_brand_input(self.create_brand)
            self.click_button(self.unit_of_measure_card)
            self.click_button(self.units_of_measure_selector_card)
            self.enter_in_unit_input(self.create_unit)
            print("Все поля карточки продукта заполнены")
            self.click_button(self.button_create_card)
            self.is_not_visible(self.button_create_card)
            try:
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print("------------------Баг: Тостовое сообщение об успехе не отобразилось--------------------------")
            self.browser_refresh()

            """Проверка, что создан корректный продукт"""
            fact_eanc = self.get_text(self.last_eanc_in_grid)
            fact_eanp = self.get_text(self.last_eanp_in_grid)
            fact_name = self.get_text(self.last_prod_name_in_grid)
            fact_technology = self.get_text(self.last_technology_in_grid)
            fact_category = self.get_text(self.last_category_in_grid)
            fact_brand = self.get_text(self.last_brand_in_grid)
            fact_unit = self.get_text(self.last_unit_in_grid)
            print(f"Веденное имя продукта при создании: {self.create_name}, значение последнего созданного продукта: {fact_name}")
            print(f"Веденный EAN Case продукта при создании: {self.create_eanc}, значение последнего созданного продукта: {fact_eanc}")
            print(f"Веденный EAN Pc продукта при создании: {self.create_eanp}, значение последнего созданного продукта: {fact_eanp}")
            print(f"Веденный Category продукта при создании: {self.create_category}, значение последнего созданного продукта: {fact_category}")
            print(f"Веденный Technology продукта при создании: {self.create_technology}, значение последнего созданного продукта: {fact_technology}")
            print(f"Веденный Brand продукта при создании: {self.create_brand}, значение последнего созданного продукта: {fact_brand}")
            print(f"Веденный Unit продукта при создании: {self.create_unit}, значение последнего созданного продукта: {fact_unit}")
            assert self.create_name == fact_name, "Имя продукта не соответствует созданному"
            assert str(self.create_eanc) == str(fact_eanc), "EAN Case продукта не соответствует созданному"
            assert str(self.create_eanp) == str(fact_eanp), "EAN Pc продукта не соответствует созданному"
            assert self.create_category == fact_category, "Категория продукта не соответствует созданной"
            assert self.create_technology == fact_technology, "Технология продукта не соответствует созданной"
            assert self.create_brand == fact_brand, "Бренд продукта не соответствует созданному"
            assert str(self.create_unit) == str(fact_unit), "Юнит продукта не соответствует созданному"
            print("Создан корректный продукт")
            Logger.add_end_step(url=self.driver.current_url, method="create_product")



    def delete_product_from_three_dots_grid(self):
        """Удаление продукта через троеточие в гриде"""
        with allure.step("Delete Product using Dots In Grid"):
            Logger.add_start_step(method="delete_product_from_three_dots_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self._3_dots_grid)
            self.click_button(self.link_delete_restore_in_3_dots_grid)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что продукт переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении через троеточие в гриде"
            print("Продукт успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_product_from_three_dots_grid")



    def delete_product_from_checkbox_grid(self):
        """Удаление продукта через чекбокс в гриде"""
        with allure.step("Delete Product using Checkbox in Grid"):
            Logger.add_start_step(method="delete_product_from_checkbox_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до удаления: {count_of_items_before}")
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

            """Проверка, что продукт переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении продукта через чекбокс"
            print("Продукт успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_product_from_checkbox_grid")



    def delete_4_product_from_checkbox_grid(self):
        with allure.step("Multiselection Deleted Product using Checkboxes in Grid"):
            """Удаление четырех продуктов через чекбоксы в гриде"""
            Logger.add_start_step(method="delete_4_product_from_checkbox_grid")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до удаления: {count_of_items_before}")
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

            """Проверка, что продукты переместились во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 4, \
                "Ошибка при удалении продуктов через чекбоксы"
            print("Продукты успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="delete_4_product_from_checkbox_grid")




    def select_all_delete_product(self):
        """Массовое удаление продуктов через Select All в гриде"""
        with allure.step("Delete Product using Select All"):
            Logger.add_start_step(method="select_all_delete_product")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до удаления: {count_of_items_before}")
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

            """Проверка, что продукты переместился во вкладку Deleted"""
            self.browser_refresh()
            self.element_is_visible(self.count_items_in_footer_grid)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - int(count_deleted_items), \
                "Ошибка при удалении продуктов через Select All"
            print("Продукты успешно удалены")
            Logger.add_end_step(url=self.driver.current_url, method="select_all_delete_product")



    def delete_product_from_card(self):
        """Удаление продукта через карточку продукта"""
        with allure.step("Delete Product from Card"):
            Logger.add_start_step(method="delete_product_from_card")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до удаления: {count_of_items_before}")
            self.click_button(self.last_prod_name_in_grid)
            print("Карточка продукта открыта")
            self.click_button(self._3_dots_card)
            print("Клик на троеточие")
            self.click_button(self.link_delete_in_3_dots_card)
            print("Клик на Delete")
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print("------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что продукт переместился во вкладку Deleted"""
            self.browser_refresh()
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до удаления: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при удалении продукта через карточку"
            print("Продукт успешно удален")
            Logger.add_end_step(url=self.driver.current_url, method="delete_product_from_card")



    def find_product_by_name(self):
        """Поиск продукта по имени продукта"""
        with allure.step("Find Product by Name"):
            Logger.add_start_step(method="find_product_by_name")
            any_name_in_grid = self.get_text(self.any_item_name)
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

            """Проверка, что найден корректный продукт"""
            first_name_in_grid = self.get_text(self.last_prod_name_in_grid)
            print(f"Имя первого отображаемого продукта в гриде: {first_name_in_grid}")
            assert str(any_name_in_grid) == str(first_name_in_grid), "Ошибка при поиске или имена продуктов не совпадают"
            print("Найден корректный продукт")
            Logger.add_end_step(url=self.driver.current_url, method="find_product_by_name")



    def find_product_by_id(self):
        """Поиск созданного продукта по ID"""
        with allure.step("Find Product by ID"):
            Logger.add_start_step(method="find_product_by_id")
            self.click_button(self.any_item_name)
            any_id = self.get_text(self.item_id)
            print(f"Выбранное для поиска ID продукта: {any_id}")
            self.click_button(self.x_icon_card)
            self.is_not_visible(self.button_create_card)
            self.enter_in_search_field(any_id)
            print(f"ID продукта '{any_id}' введено в поле поиска")
            self.get_input_search_grid().send_keys(Keys.RETURN)
            print("Enter")
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break

            """Проверка, что найден корректный продукт"""
            self.click_button(self.last_prod_name_in_grid)
            first_id = self.get_text(self.item_id)
            print(f"ID первого отображаемого продукта в гриде: {first_id}")
            assert str(any_id) == str(first_id), "Ошибка при поиске или id продуктов не совпадают"
            print("Найден корректный продукт")
            Logger.add_end_step(url=self.driver.current_url, method="find_product_by_id")



    def update_product(self):
        with allure.step("Update Product"):
            Logger.add_start_step(method="update_product")
            """Информация о последнем созданном в гриде продукте до апдейта"""
            name_before = self.get_text(self.last_prod_name_in_grid)
            eanc_before = self.is_visible(self.last_eanc_in_grid).get_attribute("title")
            eanp_before = self.is_visible(self.last_eanp_in_grid).get_attribute("title")
            technology_before = self.element_is_present(self.last_technology_in_grid).get_attribute("title")
            category_before = self.is_visible(self.last_category_in_grid).get_attribute("title")
            brand_before = self.is_visible(self.last_brand_in_grid).get_attribute("title")
            unit_before = self.is_visible(self.last_unit_in_grid).get_attribute("title")
            unit_of_measure_before = self.is_visible(self.last_unit_of_measure_in_grid).get_attribute("title")

            """Открытие правой панели и редактирование информации"""
            self.click_button(self.last_prod_name_in_grid)
            self.click_button(self.mode_switcher)
            self.get_input_name_card().clear()
            self.enter_in_name_input(self.update_name)
            self.get_input_EANC_card().clear()
            self.enter_in_eanc_input(self.update_eanc)
            self.get_input_category_card().clear()
            self.enter_in_category_input(self.update_category)
            self.get_input_technology_card().clear()
            self.enter_in_technology_input(self.update_technology)
            self.get_input_brand_card().clear()
            self.enter_in_brand_input(self.update_brand)
            card_unit_of_measure_before = self.element_is_present(self.unit_of_measure_card).get_attribute("aria-label")
            self.click_button(self.unit_of_measure_card)
            for item in self.elements_are_present(self.dropdown):
                el = item.get_attribute("aria-label")
                if el != card_unit_of_measure_before:
                    item.click()
                    break
            self.get_input_unit_card().clear()
            self.enter_in_unit_input(self.update_unit)
            self.click_button(self.button_save)
            try:
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print("------------------Баг: Тостовое сообщение об успехе не отобразилось--------------------------")
            self.click_button(self.x_icon)
            self.is_not_visible(self.x_icon)
            self.browser_refresh()

            """Информация о последнем созданном в гриде продукте после апдейта"""
            name_after = self.get_text(self.last_prod_name_in_grid)
            eanc_after = self.is_visible(self.last_eanc_in_grid).get_attribute("title")
            eanp_after = self.is_visible(self.last_eanp_in_grid).get_attribute("title")
            technology_after = self.element_is_present(self.last_technology_in_grid).get_attribute("title")
            category_after = self.is_visible(self.last_category_in_grid).get_attribute("title")
            brand_after = self.is_visible(self.last_brand_in_grid).get_attribute("title")
            unit_after = self.is_visible(self.last_unit_in_grid).get_attribute("title")
            unit_of_measure_after = self.is_visible(self.last_unit_of_measure_in_grid).get_attribute("title")

            """Проверка, что информация о продукте успешно отредактирована"""
            print(f"Имя продукта до: {name_before}, после: {name_after}")
            print(f"EAN Case продукта до: {eanc_before}, после: {eanc_after}")
            print(f"EAN Pc продукта до: {eanp_before}, после: {eanp_after} - не изменялся")
            print(f"Category продукта до: {category_before}, после: {category_after}")
            print(f"Technology продукта дом: {technology_before}, после: {technology_after}")
            print(f"Brand продукта до: {brand_before}, после: {brand_after}")
            print(f"Unit продукта до: {unit_before}, после: {unit_after}")
            print(f"Unit of Measure продукта до: {unit_of_measure_before}, после: {unit_of_measure_after}")
            assert name_before != name_after, "Имя продукта не обновилось"
            assert str(eanc_before) != str(eanc_after), "EAN Case продукта не обновился"
            assert str(eanp_before) == str(eanp_after), "EAN Pc продукта изменился"
            assert category_before != category_after, "Категория продукта не обновилась"
            assert technology_before != technology_after, "Технология продукта не обновилась"
            assert brand_before != brand_after, "Бренд продукта не обновился"
            assert str(unit_before) != str(unit_after), "Юнит продукта не обновился"
            assert str(unit_of_measure_before) != str(unit_of_measure_after), "Unit of Measure продукта не обновился"
            print("Продукт успешно отредактирован")
            Logger.add_end_step(url=self.driver.current_url, method="update_product")


    def restore_product_from_three_dots_grid(self):
        """Восстановление продукта из помеченных на удаление через троеточие в гриде"""
        with allure.step("Restore Product using Dots in Grid"):
            Logger.add_start_step(method="restore_product_from_three_dots_grid")
            self.click_button(self.deleted_tab_grid)
            self.is_visible(self.deleted_tab_grid_is_active)
            count = 0
            while self.get_text(self.count_items_in_footer_grid) == "0":
                time.sleep(1)
                count += 1
                if count == 10:
                    break
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке Deleted до рестора: {count_of_items_before}")
            self.click_button(self._3_dots_grid)
            self.click_button(self.link_delete_restore_in_3_dots_grid)
            try:
                self.click_button(self.button_delete_item)
                self.is_visible(self.toast_message_success)
            except self.ignored_exceptions:
                print(
                    "------------------Баг: Окно подтверждения или тостовое сообщение об успехе не отобразились--------------------------")

            """Проверка, что продукт переместился во вкладку All"""
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
            print(f"Количество продуктов на вкладке Deleted после рестора: {count_of_items_after}")
            assert int(count_of_items_after) == int(count_of_items_before) - 1, \
                "Ошибка при восстановлении продукта через троеточие в гриде"
            print("Продукт успешно восстановлен")
            Logger.add_end_step(url=self.driver.current_url, method="restore_product_from_three_dots_grid")



    def filters_product_by_sku_name(self):
        """Фильтрация продуктов по имени"""
        with allure.step("Filter Products by Name using All Filters"):
            Logger.add_start_step(method="filters_product_by_sku_name")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до фильтрации: {count_of_items_before}")
            any_name_in_grid = self.get_text(self.any_item_name)
            print(f"Выбранное для фильтрации имя продукта: {any_name_in_grid}")
            self.click_button(self.button_all_fiters)
            self.enter_in_sku_name_input_filters(any_name_in_grid)
            print("Имя продукта введено в поле SKU Name")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            print("Клик Apply")

            """Проверка, что продукты отфильтровались по SKU"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после фильтрации: {count_of_items_after}")
            if count_of_items_after < count_of_items_before:
                last_sku_name_in_grid = self.get_text(self.last_prod_name_in_grid)
                print(f"Имя первого отображаемого продукта в гриде: {last_sku_name_in_grid}")
                counter_all_filters_is_visible = False
                try:
                    counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
                except self.ignored_exceptions:
                    pass
                assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
                assert str(any_name_in_grid) == str(last_sku_name_in_grid), "Ошибка при фильтрации по имени или имена продуктов не совпадают"
            print("Фильтрация корректна")
            Logger.add_end_step(url=self.driver.current_url, method="filters_product_by_sku_name")



    def filters_product_by_category(self):
        """Фильтрация продуктов по категории"""
        with allure.step("Filter Products by Category using All Filters"):
            Logger.add_start_step(method="filters_product_by_category")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до фильтрации: {count_of_items_before}")
            any_category_in_grid_before = self.get_text(self.any_category_in_grid)
            print(f"Выбранная для фильтрации категория продукта: {any_category_in_grid_before}")
            self.click_button(self.button_all_fiters)
            self.enter_in_category_input_filters(any_category_in_grid_before)
            print(f"Категория продукта '{any_category_in_grid_before}' введена в поле Category")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            print("Клик Apply")

            """Проверка, что продукты отфильтровались по категории"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после фильтрации: {count_of_items_after}")
            last_category_in_grid_after = self.get_text(self.last_category_in_grid)
            print(f"Категории отфильтрованных продуктов в гриде: {last_category_in_grid_after}")
            counter_all_filters_is_visible = False
            try:
                counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
            except self.ignored_exceptions:
                pass
            assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
            assert str(any_category_in_grid_before) == str(last_category_in_grid_after), "Ошибка при фильтрации по категории или категории продуктов не совпадают"
            print("Фильтрация корректна")
            Logger.add_end_step(url=self.driver.current_url, method="filters_product_by_category")



    def filters_product_by_brand(self):
        """Фильтрация продуктов по бренду"""
        with allure.step("Filter Products by Brand using All Filters"):
            Logger.add_start_step(method="filters_product_by_brand")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до фильтрации: {count_of_items_before}")
            any_brand_in_grid_before = self.get_text(self.any_brand_in_grid)
            print(f"Выбранный для фильтрации бренд продукта: {any_brand_in_grid_before}")
            self.click_button(self.button_all_fiters)
            self.enter_in_brand_input_filters(any_brand_in_grid_before)
            print(f"Бренд продукта '{any_brand_in_grid_before}' введен в поле Brand")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            print("Клик Apply")

            """Проверка, что продукты отфильтровались по бренду"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после фильтрации: {count_of_items_after}")
            last_brand_in_grid_after = self.get_text(self.last_brand_in_grid)
            print(f"Бренды отфильтрованных продуктов в гриде: {last_brand_in_grid_after}")
            counter_all_filters_is_visible = False
            try:
                counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
            except self.ignored_exceptions:
                pass
            assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
            assert str(any_brand_in_grid_before) == str(last_brand_in_grid_after), "Ошибка при фильтрации по бренду или бренды продуктов не совпадают"
            print("Фильтрация корректна")
            Logger.add_end_step(url=self.driver.current_url, method="filters_product_by_brand")



    def filters_product_by_unit_of_measure(self):
        """Фильтрация продуктов по единице измерения"""
        with allure.step("Filter Products by Unit of Measure using All Filters"):
            Logger.add_start_step(method="filters_product_by_unit_of_measure")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до фильтрации: {count_of_items_before}")
            any_unit_of_measure_in_grid_before = self.get_text(self.any_unit_of_measure_in_grid)
            print(f"Выбранная для фильтрации единица измерения продукта: {any_unit_of_measure_in_grid_before}")
            self.click_button(self.button_all_fiters)
            self.enter_in_unit_of_measure_input_filters(any_unit_of_measure_in_grid_before)
            print(f"Единица измерения продукта '{any_unit_of_measure_in_grid_before}' введена в поле Unit of Measure")
            if self.get_text(self.counter_filters) == "1":
                self.click_button(self.button_apply_filters)
            print("Клик Apply")

            """Проверка, что продукты отфильтровались по единице измерения"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после фильтрации: {count_of_items_after}")
            last_unit_of_measure_in_grid_after = self.get_text(self.last_unit_of_measure_in_grid)
            print(f"Единицы измерения отфильтрованных продуктов в гриде: {last_unit_of_measure_in_grid_after}")
            counter_all_filters_is_visible = False
            try:
                counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
            except self.ignored_exceptions:
                pass
            assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
            assert str(any_unit_of_measure_in_grid_before) in str(last_unit_of_measure_in_grid_after), "Ошибка при фильтрации по единице измерения или единицы измерения продуктов не совпадают"
            print("Фильтрация корректна")
            Logger.add_end_step(url=self.driver.current_url, method="filters_product_by_unit_of_measure")



    def filters_product_by_unit(self):
        """Фильтрация продуктов по юниту"""
        with allure.step("Filter Products by Unit using All Filters"):
            Logger.add_start_step(method="filters_product_by_unit")
            count_of_items_before = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All до фильтрации: {count_of_items_before}")
            any_unit_in_grid_before = self.get_text(self.any_unit_in_grid)
            print(f"Выбранный для фильтрации юнит продукта: {any_unit_in_grid_before}")
            self.click_button(self.button_all_fiters)
            self.enter_in_unit_from_input_filters(any_unit_in_grid_before)
            self.enter_in_unit_to_input_filters(any_unit_in_grid_before)
            print(f"Юнит продукта '{any_unit_in_grid_before}' введен в поля Unit from и Unit to")
            if self.get_text(self.counter_filters) == "2":
                self.click_button(self.button_apply_filters)
            print("Клик Apply")

            """Проверка, что продукты отфильтровались по юниту"""
            self.is_not_visible(self.button_apply_filters)
            count_of_items_after = self.get_text(self.count_items_in_footer_grid)
            print(f"Количество продуктов на вкладке All после фильтрации: {count_of_items_after}")
            last_unit_in_grid_after = self.get_text(self.last_unit_in_grid)
            print(f"Юниты отфильтрованных продуктов в гриде: {last_unit_in_grid_after}")
            counter_all_filters_is_visible = False
            try:
                counter_all_filters_is_visible = self.is_visible(self.counter_all_filters)
            except self.ignored_exceptions:
                pass
            assert counter_all_filters_is_visible, "Не отображается каунтер на All Filters"
            assert str(any_unit_in_grid_before) == str(last_unit_in_grid_after), "Ошибка при фильтрации по юниту или юниты продуктов не совпадают"
            print("Фильтрация корректна")
            Logger.add_end_step(url=self.driver.current_url, method="filters_product_by_unit")



    def read_product(self):
        """Прочесть информацию о найденном продукте и сравнить с данными из грида"""
        with allure.step("Read Product"):
            """Найти продукт"""
            Logger.add_start_step(method="read_product")
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

            """Получить информацию о найденном продукте из грида"""
            grid_name = self.get_text(self.last_prod_name_in_grid)
            grid_eanc = self.get_text(self.last_eanc_in_grid)
            grid_eanp = self.get_text(self.last_eanp_in_grid)
            grid_technology = self.element_is_present(self.last_technology_in_grid).get_attribute("title")
            grid_category = self.get_text(self.last_category_in_grid)
            grid_brand = self.get_text(self.last_brand_in_grid)
            grid_unit_of_measure = self.get_text(self.last_unit_of_measure_in_grid)
            grid_unit = self.get_text(self.last_unit_in_grid)

            """Проверка, что информация в правой панели соответствует информации в гриде"""
            self.click_button(self.last_prod_name_in_grid)
            card_name = self.is_visible(self.input_name_card).get_attribute("value")
            card_eanc = self.is_visible(self.input_EANC_card).get_attribute("value")
            card_eanp = self.is_visible(self.input_EANP_card).get_attribute("value")
            card_category = self.is_visible(self.input_category_card).get_attribute("value")
            card_technology = self.element_is_present(self.input_technology_card).get_attribute("value")
            card_brand = self.is_visible(self.input_brand_card).get_attribute("value")
            card_unit = self.is_visible(self.input_unit_card).get_attribute("value")
            card_unit_of_measure = self.get_text(self.value_of_unit_of_measure_card)
            print(f"Имя продукта в гриде: {grid_name}, в карточке: {card_name}")
            print(f"EAN Case продукта в гриде: {grid_eanc}, в карточке: {card_eanc}")
            print(f"EAN Pc продукта в гриде: {grid_eanp}, в карточке: {card_eanp}")
            print(f"Category продукта в гриде: {grid_category}, в карточке: {card_category}")
            print(f"Technology продукта в гриде: {grid_technology}, в карточке: {card_technology}")
            print(f"Brand продукта в гриде: {grid_brand}, в карточке: {card_brand}")
            print(f"Unit продукта в гриде: {grid_unit}, в карточке: {card_unit}")
            print(f"Unit of Measure продукта в гриде: {grid_unit_of_measure}, в карточке: {card_unit_of_measure}")
            assert grid_name == card_name, "Имена продуктов не совпадают"
            assert grid_eanc == card_eanc, "EAN Case продуктов не совпадают"
            assert grid_eanp == card_eanp, "EAN Pc продуктов не совпадают"
            assert grid_category == card_category, "Category продуктов не совпадают"
            assert grid_technology == card_technology, "Technology продуктов не совпадают"
            assert grid_brand == card_brand, "Brand продуктов не совпадают"
            assert str(grid_unit) == str(card_unit), "Unit продуктов не совпадают"
            assert grid_unit_of_measure == card_unit_of_measure, "Unit of Measure продуктов не совпадают"
            print("Информация о продукте в карточке соответствует информации о продукте в гриде")
            Logger.add_end_step(url=self.driver.current_url, method="read_product")



    def check_button_clear_filters_products(self):
        """Проверить работу кнопки Clear в расширенных фильтрах"""
        with allure.step("Check button Clear in All Filters"):
            Logger.add_start_step(method="check_button_clear_filters_products")
            self.click_button(self.button_all_fiters)
            self.enter_in_sku_name_input_filters(random.randint(1, 10))
            self.enter_in_category_input_filters(random.randint(1, 10))
            self.enter_in_technology_input_filters(random.randint(1, 10))
            self.enter_in_brand_input_filters(random.randint(1, 10))
            self.enter_in_unit_of_measure_input_filters(random.randint(1, 10))
            self.enter_in_unit_from_input_filters(random.randint(1, 10))
            self.enter_in_unit_to_input_filters(random.randint(1, 10))
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
            Logger.add_end_step(url=self.driver.current_url, method="check_button_clear_filters_products")



    def check_x_icon_filters_products(self):
        """Проверить работу кнопки закрытия расширенных фильтров"""
        with allure.step("Check button X in All Filters"):
            Logger.add_start_step(method="check_x_icon_filters_products")
            self.click_button(self.button_all_fiters)
            self.enter_in_sku_name_input_filters(random.randint(1, 10))
            self.enter_in_category_input_filters(random.randint(1, 10))
            self.enter_in_technology_input_filters(random.randint(1, 10))
            self.enter_in_brand_input_filters(random.randint(1, 10))
            self.enter_in_unit_of_measure_input_filters(random.randint(1, 10))
            self.enter_in_unit_from_input_filters(random.randint(1, 10))
            self.enter_in_unit_to_input_filters(random.randint(1, 10))
            self.click_button(self.x_icon_filters)
            btn_apply_is_not_visible = False
            try:
                btn_apply_is_not_visible = self.is_not_visible(self.button_apply_filters)
            except self.ignored_exceptions:
                pass
            assert btn_apply_is_not_visible, "Кнопка закрытия расширенных фильтров не работает"
            print("Кнопка закрытия расширенных фильтров работает")
            Logger.add_end_step(url=self.driver.current_url, method="check_x_icon_filters_products")



    def check_x_icon_inside_filters_products(self):
        """Проверить работу индивидуальных кнопок очисток полей внутри расширенных фильтров"""
        with allure.step("Check individual buttons X in All Filters"):
            Logger.add_start_step(method="check_x_icon_inside_filters_products")
            self.click_button(self.button_all_fiters)
            self.enter_in_sku_name_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            self.enter_in_category_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            self.enter_in_technology_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            self.enter_in_brand_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            self.enter_in_unit_of_measure_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            self.enter_in_unit_from_input_filters(random.randint(1, 10))
            self.enter_in_unit_to_input_filters(random.randint(1, 10))
            self.click_button(self.x_icons_input_filters)
            x_icons_is_not_visible = False
            try:
                x_icons_is_not_visible = self.is_not_visible(self.x_icons_input_filters)
            except self.ignored_exceptions:
                pass
            assert x_icons_is_not_visible, "Индивидуальные кнопки очистки расширенных фильтров не работают"
            print("Индивидуальные кнопки очистки расширенных фильтров работают")
            Logger.add_end_step(url=self.driver.current_url, method="check_x_icon_inside_filters_products")



