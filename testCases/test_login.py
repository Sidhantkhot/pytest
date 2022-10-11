import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utility.customlogger import LogGen
from utility.readProperties import ReadConfig


class Test_001_Login:
    baseurl = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_page_title(self, setup):
        self.logger.info("*********** Test_001_Login ***********")
        self.logger.info("*********** Verifying Home Page Title ***********")

        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Test Home Page Title passed  ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage.png")
            assert False
            self.driver.close()
            self.logger.error("*********** Test Home Page Title failed  ***********")

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*********** Verifying Login Page Title ***********")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********** Test Login Page Title passed  ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.driver.close
            self.logger.error("*********** Test Login Page Title failed ***********")
