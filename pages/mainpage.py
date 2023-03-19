from selenium.webdriver.common.by import By
from pages.basepage import BasePageScooter
class MainPageLocators:
    LOGO_SCOOTER = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    HOW_MUCH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0']")
    HOW_MUCH_ANSWER = (By.XPATH, "//div[@id= 'accordion__panel-0']/p")
    WANT_SOME_SCOOTERS_QUESTION = [By.XPATH, "//div[@id='accordion__heading-1']"]
    WANT_SOME_SCOOTERS_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-1']/p"]
    HOW_CALCULATE_RENTAL_TIME_QUESTION = [By.XPATH, "//div[@id='accordion__heading-2']"]
    HOW_CALCULATE_RENTAL_TIME_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-2']/p"]
    CAN_ORDER_TODAY_QUESTION = [By.XPATH, "//div[@id='accordion__heading-3']"]
    CAN_ORDER_TODAY_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-3']/p"]
    CAN_EXPEND_RETURN_EARLIER_QUESTION = [By.XPATH, "//div[@id='accordion__heading-4']"]
    CAN_EXPEND_RETURN_EARLIER_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-4']/p"]
    CHARGING_WITH_A_SCOOTER_QUESTION = [By.XPATH, "//div[@id='accordion__heading-5']"]
    CHARGING_WITH_A_SCOOTER_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-5']/p"]
    CAN_CANCEL_ORDER_QUESTION = [By.XPATH, "//div[@id='accordion__heading-6']"]
    CAN_CANCEL_ORDER_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-6']/p"]
    LIVE_FURTHER_THAN_MKAD_QUESTION = [By.XPATH, "//div[@id='accordion__heading-7']"]
    LIVE_FURTHER_THAN_MKAD_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-7']/p"]
    BUTTON_ORDER_IN_HEAD = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    BUTTON_ORDER_IN_FOOTER = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    COOKIE = [By.XPATH, "//button[@id='rcc-confirm-button']"]
class MainPageScooter(BasePageScooter):
    question_is_selected = 'true'
    mainpage_url = 'https://qa-scooter.praktikum-services.ru/'
    answers = {'how_much': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
               'some_scooters': 'Пока что у нас так: один заказ — один самокат. ' \
                                  'Если хотите покататься с друзьями, можете просто сделать несколько заказов' \
                                  ' — один за другим.',
               'how_calculate': 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня.' \
                                  ' Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                                  'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
               'can_order_today': 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
               'can_expend': 'Пока что нет! Но если что-то срочное — всегда можно позвонить' \
                                  ' в поддержку по красивому номеру 1010.',
               'charging_with_a_scooter': 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток' \
                                  ' — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
               'can_cancel': 'Да, пока самокат не привезли. Штрафа не будет, ' \
                                  'объяснительной записки тоже не попросим. Все же свои.',
               'further_than_mkad': 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'}
    def wait_for_load_main_page(self):
        self.wait_for_element_located(*MainPageLocators.LOGO_SCOOTER)
    def set_element_by_main_page(self, by, locator):
        element = self.driver.find_element(by, locator)
        self.scroll_to_element(element)
        self.wait_for_element_to_be_clickable(by, locator)
        element.click()
    def get_answer_from_main_page(self, by, locator):
        self.wait_for_element_to_be_clickable(by, locator)
        answer = self.driver.find_element(by, locator)
        return answer.text
    def get_attribute_for_question(self, by, locator):
        question = self.driver.find_element(by, locator)
        return question.get_attribute('aria-expanded')
    def clear_message_about_cookie(self):
        self.accept_cookie(*MainPageLocators.COOKIE)