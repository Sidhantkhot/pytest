from selenium.webdriver.common.by import By


class LoginPage:
    text_box_username = "//*[@id='Email']"
    text_box_password = "//*[@id='Password']"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.text_box_username).clear()
        self.driver.find_element(By.XPATH, self.text_box_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.text_box_password).clear()
        self.driver.find_element(By.XPATH, self.text_box_password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
