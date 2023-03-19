from selenium.webdriver.common.by import By
class YandexPage:
    SEARCH_LINE = [By.XPATH, "//input[@class='arrow__input mini-suggest__input']"]
    new_window_is_open = 2
    def __init__(self, driver):
        self.driver = driver
    def weit_for_load_yandex_page(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
    def get_count_of_windows(self):
        return len(self.driver.window_handles)