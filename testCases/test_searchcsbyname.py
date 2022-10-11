import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.addcutomerpage import AddCustomer
from pageObjects.searchcustomerpage import SearchCustomer
from utility.customlogger import LogGen
from utility.readProperties import ReadConfig


class Test_006_SearchCustomer:
    baseurl = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen().loggen()

    @pytest.mark.regression
    def test_search_by_first_name(self, setup):
        self.logger.info("*********** Test_006_SearchCustomer ***********")
        self.logger.info("*********** Verifying search customer by name functionality ***********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()

        self.addcust = AddCustomer(self.driver)
        self.addcust.click_drp_menu()
        self.logger.info("*********** clicked customer drop menu ***********")
        self.addcust.click_cust_lnk()
        self.logger.info("*********** clicked customer link ***********")
        self.sc = SearchCustomer(self.driver)
        self.sc.enter_fname("Victoria")
        self.logger.info("*********** entered first name in first name text box : victoria ***********")
        self.sc.click_search_button()
        self.logger.info("*********** clicked search button ***********")
        result = self.sc.search_by_name("Victoria")
        if result == True:
            assert True
            self.logger.info("*********** displaying victoria in table ***********")
            self.logger.info("*********** test passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "testserchbyname.png")
            assert False
            self.driver.close()
            self.logger.info("test failed")

        self.logger.info("*********** Test search by first name completed ***********")
