from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver
    def scroll_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)
    def go_to_page(self, url):
        self.driver.get(url)
    def wait_for_element_located(self, by, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by, locator)))
    def wait_for_element_to_be_clickable(self, by, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))
    def check_url(self):
        return self.driver.current_url
    def accept_cookie(self, by, locator):
        try:
            self.driver.find_element(by, locator).click()
        except NoSuchElementException:
            pass