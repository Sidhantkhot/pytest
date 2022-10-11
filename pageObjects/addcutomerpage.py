import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    nav_cust_drp = "//i[@class='nav-icon far fa-user']"  # "//p[text()=' Customers']"
    cutomer_lnk = "(//a[@href='/Admin/Customer/List'])[1]"
    add_new_btn_xpath = "//a[@class='btn btn-primary']"
    email_txt_box = "//input[@id='Email']"
    pwd_txt_box = "//input[@id='Password']"
    fname_txt_box = "//*[@id='FirstName']"
    lname_txt_box = "//*[@id='LastName']"
    gender_rb_m = "//*[@id='Gender_Male']"
    gender_rb_f = "//*[@id='Gender_Female'"
    dob_txt_box = "//*[@id='DateOfBirth']"
    company_tx_box = "//*[@id='Company']"
    tax_ex_chkbx = "//*[@id='IsTaxExempt']"
    newsletter_lstbx = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    nl_your_store = "//li[text()='Your store name']"
    nl_test_store = "//li[text()='Test store 2']"
    cust_role_tx_box = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    cust_role = "//*[@id='SelectedCustomerRoleIds']"
    cust_role_adm = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    cust_role_frm_mod = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    cust_role_gust = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    cust_role_reg = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    cust_role_vend = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    deselect_cust_role = "//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[2]"
    vendor_mngr = "//*[@id='VendorId']"
    adm_cmt = "//*[@id='AdminComment']"
    save_btn = "(//i[@class='far fa-save'])[1]"
    msg = "//div[@class='alert alert-success alert-dismissable']"
    def __init__(self, driver):
        self.driver = driver

    def click_drp_menu(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.nav_cust_drp)))
        element.click()
        # self.driver.find_element(By.XPATH, self.nav_cust_drp).click()

    def click_cust_lnk(self):
        self.driver.find_element(By.XPATH, self.cutomer_lnk).click()

    def click_add_new_btn(self):
        self.driver.find_element(By.XPATH, self.add_new_btn_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_txt_box).send_keys(email)

    def enter_fname(self, firstname):
        self.driver.find_element(By.XPATH, self.fname_txt_box).send_keys(firstname)

    def enter_lname(self, lastname):
        self.driver.find_element(By.XPATH, self.lname_txt_box).send_keys(lastname)

    def enter_pwd(self, password):
        self.driver.find_element(By.XPATH, self.pwd_txt_box).send_keys(password)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.gender_rb_m).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.gender_rb_f).click()

    def select_dob(self, dob):
        self.driver.find_element(By.XPATH, self.dob_txt_box).send_keys(dob)

    def enter_company_name(self, co_name):
        self.driver.find_element(By.XPATH, self.company_tx_box).send_keys(co_name)

    def tic_tax_chkbx(self):
        self.driver.find_element(By.XPATH, self.tax_ex_chkbx).click()

    def select_newsletter(self, newsletter):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.newsletter_lstbx)))
        element.click()
        if newsletter == "Your store name":
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.nl_test_store)))
            element.click()
        elif newsletter == "Test store 2":
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.nl_test_store)))
            element.click()

    def select_cust_role(self, customer_role):
        self.driver.find_element(By.XPATH, self.cust_role_tx_box).click()

        if customer_role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.cust_role_adm)

        elif customer_role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.cust_role_frm_mod)

        elif customer_role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.cust_role_vend)

        else:
            dele = self.driver.find_element(By.XPATH, self.deselect_cust_role)
            self.driver.execute_script("arguments[0].click();", dele)
            self.listitem = self.driver.find_element(By.XPATH, self.cust_role_gust)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def select_vendor_mngr(self, ven_manger):
        drp = self.driver.find_element(By.XPATH, self.vendor_mngr)
        select = Select(drp)
        select.select_by_visible_text(ven_manger)

    def add_comment(self,comment):
        self.driver.find_element(By.XPATH,self.adm_cmt).send_keys(comment)

    def click_save_btn(self):
        self.driver.find_element(By.XPATH, self.save_btn).click()

    def verify_msg(self):
        ele = self.driver.find_element(By.XPATH, self.msg)
        if "The new customer has been added successfully." ==ele.text():
            return "Pass"

