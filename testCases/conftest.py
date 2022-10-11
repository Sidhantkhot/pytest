from selenium import webdriver
from selenium.webdriver.chrome.service import service as ChromeService
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "ff":
        driver = webdriver.Firefox(
            executable_path= "C:/Users/SIDHANT/.wdm/drivers/geckodriver/win64/0.31/geckodriver.exe" )
    else:
        driver = webdriver.Edge()

    # driver.maximize_window()

    return driver


# ======== HTML REPORT ======#

def pytest_configure(config):
    config._metadata["Project Name"] = "nopcommerce"
    config._metadata["Module Name"] = "customer"
    config._metadata["Tester Name"] = "Sidhant"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


def pytest_addoption(parser):  # this will get value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")
