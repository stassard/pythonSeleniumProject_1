import allure
from pages.client_products_page import ClientProductsPage
from pages.login_page import LoginPage
import pytest

@allure.feature("Smoke Suite for Client Products Page")
class TestSmokeClientProductsPage:
    """Создание матрицы Клиент Продукт"""
    @allure.title("Create Client Product")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_client_products(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.create_client_product()

    """Удаление матрицы Клиент Продукт через троеточие в гриде"""
    @allure.title("Delete Client Product using Dots In Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_product_from_three_dots_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.delete_client_product_from_three_dots_grid()


    """Удаление матрицы Клиент Продукт через чекбокс в гриде"""
    @allure.title("Delete Client Product using Checkbox in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_product_from_checkbox_grid(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.delete_client_product_from_checkbox_grid()


    """Удаление 4х матриц Клиент Продукт через чекбоксы в гриде"""
    @allure.title("Multiselection Deleting Client Product using Checkboxes in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_4_client_product_from_checkbox_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.delete_4_client_product_from_checkbox_grid()


    """Удаление матриц Клиент Продукт через Select All"""
    @allure.title("Delete Client Product using Select All")
    @allure.severity("Critical")
    @pytest.mark.smoke
    # @pytest.mark.skip
    def test_select_all_delete_client_product(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.select_all_delete_client_product()


    """Удаление матрицы Клиент Продукт через карточку матрицы"""
    @allure.title("Delete Client Product from Card")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_product_from_card(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.delete_client_product_from_card()


    """Найти матрицу Клиент Продукт по Product SKU Name через поле Search"""
    @allure.title("Find Client Product by Product SKU Name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_find_client_product_by_product_sku_name(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.find_client_product_by_sku_name()


    """Найти матрицу Клиент Продукт по ID через поле Search"""
    @allure.title("Find Client Product by ID")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_find_client_product_by_id(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.find_client_product_by_id()


    """Прочитать информацию о найденной матрице Клиент Продукт и сравнить с данными из грида"""
    @allure.title("Read Client Product")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_read_client_product(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.read_client_product()


    """Рестор матрицы Клиент Продукт через троеточие в гриде"""
    @allure.title("Restore Client Product using Dots in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_restore_client_product_from_three_dots_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.restore_client_product_from_three_dots_grid()


    """Отфильтровать матрицы Клиент Продукт по имени клиента через расширенные фильтры"""
    @allure.title("Filter Client Products by Client using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_product_by_client(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.filters_client_product_by_client()


    """Отфильтровать матрицы Клиент Продукт по имени продукта через расширенные фильтры"""
    @allure.title("Filter Client Products by Product using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_product_by_product(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.filters_client_product_by_product()


    """Проверить работу кнопки Clear в расширенных фильтрах"""
    @allure.title("Check button Clear in All Filters")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_check_button_clear_filters_client_products(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.check_button_clear_filters_client_products()


    """Проверить работу иконки Х в расширенных фильтрах"""
    @allure.title("Check button X in All Filters")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_check_x_icon_filters_client_products(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.check_x_icon_filters_client_products()


    """Проверить работу индивидуальных кнопок очистки расширенных фильтров"""
    @allure.title("Check individual buttons X in All Filters")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_check_x_icon_inside_filters_client_products(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.check_x_icon_inside_filters_client_products()