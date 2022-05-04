import json
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver import Chrome


CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10


@pytest.fixture(scope='session')
def config():#Create a json file with browser an wait time
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def browser(config):#Create the set up driver 
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.implicitly_wait(config['wait_time'])
    driver.maximize_window()
    yield driver  # Return the driver object at the end of setup
    driver.quit()
