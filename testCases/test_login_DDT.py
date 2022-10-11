import pytest

from pageObjects.LoginPage import LoginPage
from utility.customlogger import LogGen
from utility.readProperties import ReadConfig
from utility import xlutils


class Test_002_Login_DDT:
    baseurl = ReadConfig.get_app_url()
    path = ".\\TestData\\logindata.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self, setup):
        self.logger.info("*********** Test_002_DDT_login ***********")
        self.logger.info("*********** Verifying Login Page Title ***********")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.rows = xlutils.get_row_count(self.path, 'Sheet1')

        lst = []
        for r in range(2, self.rows + 1):
            self.username = xlutils.read_xl_data(self.path, 'Sheet1', r, 1)
            self.password = xlutils.read_xl_data(self.path, 'Sheet1', r, 2)
            self.exp = xlutils.read_xl_data(self.path, 'Sheet1', r, 3)

            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login_button()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("**** passed ****")
                    self.lp.click_logout_button()
                    lst.append("pass")

                elif self.exp == "fail":
                    self.logger.inf("**** failed ****")
                    self.lp.click_logout_button()
                    lst.append("fail")

            elif act_title != exp_title :
                if self.exp == "pass":
                    self.logger.info("**** failed ****")
                    lst.append("pass")

                elif self.exp == "fail":
                    self.logger.info("**** failed ****")
                    lst.append("pass")

        if "fail" not in lst:
            self.logger.info("*********** Test Login DDT passed ***********")
            assert True
            self.driver.close()
        else:
            self.logger.info("*********** Test Login DDT failed ***********")
            assert False
            self.driver.close()

        self.logger.info("*********** Test Login DDT completed ***********")
