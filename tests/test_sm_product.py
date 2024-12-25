from base.base_class import Base
from selenium import webdriver
import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

@allure.feature("Smoke Suite for Product Page")
class TestSmokeProductPage:

    """Создание продукта"""
    @allure.title("Create Product")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_product(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.create_product()

    """Редактирование продукта"""
    @allure.title("Update Product")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_update_product(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.update_product()

    """Найти продукт по имени через поле Search"""
    @allure.title("Find Product by Name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_find_product_by_name(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.find_product_by_name()


    """Найти продукт по ID через поле Search"""
    @allure.title("Find Product by ID")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_find_product_by_id(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.find_product_by_id()


    """Удаление продукта через карточку продукта"""
    @allure.title("Delete Product from Card")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_product_from_card(self, driver):

        lp = LoginPage(driver)
        lp.authorization( )
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.delete_product_from_card()


    """Удаление продукта через троеточие в гриде"""
    @allure.title("Delete Product using Dots In Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_product_from_three_dots_grid(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.delete_product_from_three_dots_grid()


    """Удаление продукта через чекбокс в гриде"""
    @allure.title("Delete Product using Checkbox in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_product_from_checkbox_grid(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.delete_product_from_checkbox_grid()


    """Удаление 4х продуктов через чекбоксы в гриде"""
    @allure.title("Multiselection Deleted Product using Checkboxes in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_4_product_from_checkbox_grid(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.delete_4_product_from_checkbox_grid()


    """Удаление продуктов через Select All"""
    @allure.title("Delete Product using Select All")
    @allure.severity("Critical")
    @pytest.mark.smoke
    # @pytest.mark.skip
    def test_select_all_delete_product(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.select_all_delete_product()


    """Рестор продукта через троеточие в гриде"""
    @allure.title("Restore Product using Dots in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_restore_product_from_three_dots_grid(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()

        pp.restore_product_from_three_dots_grid()


    """Отфильтровать продукт по имени через расширенные фильтры"""
    @allure.title("Filter Products by Name using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_product_by_sku_name(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.filters_product_by_sku_name()


    """Отфильтровать продукт по категории через расширенные фильтры"""
    @allure.title("Filter Products by Category using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_product_by_category(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.filters_product_by_category()


    """Отфильтровать продукт по бренду через расширенные фильтры"""
    @allure.title("Filter Products by Brand using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_product_by_brand(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.filters_product_by_brand()


    """Отфильтровать продукт по единице измерения через расширенные фильтры"""
    @allure.title("Filter Products by Unit of Measure using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_product_by_unit_of_measure(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.filters_product_by_unit_of_measure()


    """Отфильтровать продукт по юниту через расширенные фильтры"""
    @allure.title("Filter Products by Unit using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_product_by_unit(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.filters_product_by_unit()


    """Прочитать информацию о продукте"""
    @allure.title("Read Product")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_read_product(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.read_product()


    """Проверить работу кнопки Clear в расширенных фильтрах"""
    @allure.title("Check button Clear in All Filters")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_check_button_clear_filters(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.check_button_clear_filters()


    """Проверить работу иконки Х в расширенных фильтрах"""
    @allure.title("Check button X in All Filters")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_check_x_icon_filters(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.check_x_icon_filters()


    """Проверить работу индивидуальных кнопок очистки расширенных фильтров"""
    @allure.title("Check individual buttons X in All Filters")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_check_x_icon_inside_filters(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        pp = ProductPage(driver)
        pp.open_products_dict()
        pp.check_x_icon_inside_filters()
