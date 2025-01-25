from base.base_class import Base
import os
from dotenv import load_dotenv, find_dotenv
import allure
from utilities.logger import logger

class LoginPage(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""

    load_dotenv(find_dotenv())

    # Locators
    button_login = "(//button[contains(@aria-label,'ProSpace')])"             # Button ProSpace
    input_login_field = "//input[@type='text']"                               # Input Login
    input_password_field = "//input[@type='password']"                        # Input Password
    button_signin = "//span[text()='Sign In']"                                # Button Sign in
    # header_of_promo_page = "//div[contains(text(),'Promo Portfolio')]"        # Заголовок страницы Промо Портфолио

    # Actions

    def get_main_word(self):
        return self.element_is_visible(self.head_of_page)

    def input_login(self, user_name):
        return self.element_is_clickable(self.input_login_field).send_keys(user_name)

    def input_password(self, password):
        return self.element_is_clickable(self.input_password_field).send_keys(password)

    def click_button_login(self):
        return self.element_is_clickable(self.button_login).click()


    def click_button_signin(self):
        return self.element_is_clickable(self.button_signin).click()

    # Methods
    def authorization(self):
        """Authorization"""
        with allure.step("Authorization"):
            logger.info("Authorization")
            self.driver.get(os.getenv("DEV_1"))
            self.driver.maximize_window()
            self.click_button_login()
            self.input_login(os.getenv("ADMIN_LOGIN"))
            self.input_password(os.getenv("ADMIN_PASSWORD"))
            self.click_button_signin()
            self.assert_word(self.get_main_word(), "Promo Portfolio")
            logger.info("Successful Authorization. Page Promo Portfolio is open")
