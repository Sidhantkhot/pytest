import time
import faker
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.addcutomerpage import AddCustomer
from utility.customlogger import LogGen
from utility.readProperties import ReadConfig


class Test_003_AddNewCustomer:
    baseurl = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_add_new_customer(self, setup):
        self.logger.info("*********** Test_003_AddNewCustomer ***********")
        self.logger.info("*********** Verifying add new customer ***********")
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
        self.logger.info("*********** clicked customer link  ***********")
        self.addcust.click_add_new_btn()
        self.logger.info("*********** clicked add new customer button ***********")
        f = faker.Faker()
        self.email = f.email()
        self.addcust.enter_email(self.email)
        self.logger.info(f"*********** entered email {self.email} ***********")
        self.addcust.enter_pwd("admin123")
        self.logger.info("*********** entered password admin123 ***********")
        self.fname = f.first_name()
        self.addcust.enter_fname(self.fname)
        self.logger.info(f"*********** entered first name {self.fname}***********")
        self.lname = f.last_name()
        self.addcust.enter_lname(self.lname)
        self.logger.info(f"*********** entered last name {self.lname}***********")
        self.addcust.select_gender("Male")
        self.logger.info("*********** selected gender male***********")
        self.addcust.select_dob("9/9/2022")
        self.logger.info("*********** entered date of birth 9/9/2022 ***********")
        self.addcust.enter_company_name("busyQa")
        self.logger.info(f"*********** entered company name busyQa ***********")
        self.addcust.tic_tax_chkbx()
        self.logger.info("*********** tic mark to checkbox ***********")
        self.addcust.select_newsletter("Your store name")
        self.logger.info("*********** selected newsletter for Your store name ***********")
        self.addcust.select_vendor_mngr("Vendor 1")
        self.logger.info(f"*********** selected vendor manager Vendor 1 ***********")
        # lst = ["Administrators", "Forum Moderators", "Registered", "Vendors", "Guests"]
        # for i in lst:
        #     self.addcust.select_cust_role(i)
        self.addcust.select_cust_role("Vendors")
        self.logger.info(f"*********** selected customer role Vendors ***********")
        time.sleep(2)
        self.addcust.add_comment(".....")
        self.addcust.click_save_btn()
        msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']")
        if "The new customer has been added successfully." in msg.text:
            assert True
            self.logger.info(f"**{msg.text}**")
            self.logger.info(f"*********** Add customer test passed***********")
        else:
            self.logger.info(f"*********** Add customer test failed***********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_cust.png")
        self.logger.info("*********** Add customer test completed***********")

        self.driver.close()
