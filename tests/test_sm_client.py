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