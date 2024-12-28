from base.base_class import Base
from selenium import webdriver
import allure

from pages.client_page import ClientPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

@allure.feature("Smoke Suite for Client Page")
class TestSmokeClientPage:
    """Создание продукта"""
    @allure.title("Create Client")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_client(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()

        cp.create_client()

    """Удаление клиента через троеточие в гриде"""
    @allure.title("Delete Client using Dots In Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_from_three_dots_grid(self, driver):

        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()

        cp.delete_client_from_three_dots_grid()


    """Удаление клиента через чекбокс в гриде"""
    @allure.title("Delete Client using Checkbox in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_from_checkbox_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()

        cp.delete_client_from_checkbox_grid()

    """Удаление 4х клиентов через чекбоксы в гриде"""
    @allure.title("Multiselection Deleted Clients using Checkboxes in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_4_clients_from_checkbox_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.delete_4_clients_from_checkbox_grid()


    """Удаление клиентов через Select All"""
    @allure.title("Delete Client using Select All")
    @allure.severity("Critical")
    @pytest.mark.smoke
    # @pytest.mark.skip
    def test_select_all_delete_client(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.select_all_delete_client()

    """Удаление клиента через карточку клиента"""
    @allure.title("Delete Client from Card")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_from_card(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.delete_client_from_card()


    """Найти клиента по имени через поле Search"""
    @allure.title("Find Client by Name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_find_client_by_name(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.find_client_by_name()


    """Найти клиента по ID через поле Search"""
    @allure.title("Find Client by ID")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_find_client_by_id(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.find_client_by_id()

    """Редактирование клиента"""
    @allure.title("Update Client")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_update_client(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.update_client()

    """Рестор клиента через троеточие в гриде"""
    @allure.title("Restore Client using Dots in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_restore_client_from_three_dots_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.restore_client_from_three_dots_grid()


    """Отфильтровать клиента по имени через расширенные фильтры"""
    @allure.title("Filter Client by Name using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_by_name(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.filters_client_by_name()

    """Отфильтровать клиентов по типу через расширенные фильтры"""
    @allure.title("Filter Client by Type using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_by_type(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.filters_client_by_type()


    """Отфильтровать клиентов по Invoice Type через расширенные фильтры"""
    @allure.title("Filter Client by Invoice Type using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_by_invoice_type(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.filters_client_by_invoice_type()


    """Отфильтровать клиентов по Affiliation через расширенные фильтры"""
    @allure.title("Filter Client by Affiliation using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_by_affiliation(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.filters_client_by_affiliation()


    """Отфильтровать клиентов по Dispatch Start Before Day через расширенные фильтры"""
    @allure.title("Filter Clients by Dispatch Start Before Day using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_by_dispatch_start_before_day(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.filters_client_by_dispatch_start_before_day()


    """Отфильтровать клиентов по Dispatch End Before Day через расширенные фильтры"""
    @allure.title("Filter Clients by Dispatch End Before Day using All Filters")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_filters_client_by_dispatch_end_before_day(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cp = ClientPage(driver)
        cp.open_clients_dict()
        cp.filters_client_by_dispatch_end_before_day()