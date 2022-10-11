import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchCustomer:
    email_txtbx = "//*[@id='SearchEmail']"
    fname_txtbx = "//*[@id='SearchFirstName']"
    lname_txtbx = "//*[@id='SearchLastName']"
    search_btn = "//*[@id='search-customers']"
    row_xpath = "//*[@id='customers-grid']/tbody//tr"
    col_xpath = "//*[@id='customers-grid']/tbody//tr[1]/td"
    table_xpath = "//*[@id='customers-grid']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_txtbx).send_keys(email)

    def enter_fname(self, fname):
        self.driver.find_element(By.XPATH, self.fname_txtbx).send_keys(fname)

    def enter_lname(self, lname):
        self.driver.find_element(By.XPATH, self.lname_txtbx).send_keys(lname)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_btn).click()

    def get_row_count(self):
        time.sleep(3)
        rc = len(self.driver.find_elements(By.XPATH, self.row_xpath))
        return rc

    def get_col_count(self):
        cc = len(self.driver.find_elements(By.XPATH, self.col_xpath))
        return cc

    def search_by_email(self, Email):
        flag = False
        for i in range(1,self.get_row_count() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            email = table.find_element(By.XPATH, f"//*[@id='customers-grid']/tbody/tr[{i}]/td[2]")
            if email.text == Email:
                flag = True
                break
        return flag

    def search_by_name(self, Name):
        flag = False
        for i in range(1,self.get_row_count() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, f"//*[@id='customers-grid']/tbody/tr[{i}]/td[3]")
            if Name in name.text:
                flag = True
                break
        return flag
