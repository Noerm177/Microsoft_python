import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


class DashBoardPage:

    URL = "https://www.microsoft.com/en-us/"

    FIND_TEXT = (By.XPATH, '//*[@id="onestore-quicklinksmodule-yts04ji-quicklink1"]/div')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#search.c-glyph')
    CLOSE_POP = (By.CLASS_NAME, 'c-glyph.glyph-cancel')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, text):
        search_btn = self.browser.find_element(*self.SEARCH_BUTTON)
        search_btn.click()
        search_btn.send_keys(text + Keys.RETURN)

    def see_results(self):
        close_btn = self.browser.find_element(*self.CLOSE_POP)
        close_btn.click()
        return self.browser.title 


