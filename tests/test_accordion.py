import allure

from pages.mainpage import MainPageScooter, MainPageLocators
class TestAccordionInMainPage:
    @allure.title('Сколько стоит и как оплатить')
    @allure.description('На странице ищем элемент аккордеона Сколько стоит и как оплатить и кликаем на него')
    def test_click_on_how_much(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.HOW_MUCH_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.HOW_MUCH_QUESTION) == \
               MainPageScooter.question_is_selected \
               and scooter_page.get_answer_from_main_page(*MainPageLocators.HOW_MUCH_ANSWER) == \
               scooter_page.answers['how_much']
    @allure.title('Хочу сразу несколько самокатов! Так можно?')
    @allure.description('На странице ищем элемент аккордеона Хочу сразу несколько самокатов! Так можно? '
                        'и кликаем на него')
    def test_click_on_want_some_scooters(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.WANT_SOME_SCOOTERS_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.WANT_SOME_SCOOTERS_QUESTION) \
               == MainPageScooter.question_is_selected \
               and scooter_page.get_answer_from_main_page(*MainPageLocators.WANT_SOME_SCOOTERS_ANSWER) \
               == scooter_page.answers['some_scooters']
    @allure.title('Как рассчитывается время аренды?')
    @allure.description('На странице ищем элемент аккордеона Как рассчитывается время аренды? и кликаем на него')
    def test_click_on_how_calculate_rental_time(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.HOW_CALCULATE_RENTAL_TIME_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.HOW_CALCULATE_RENTAL_TIME_QUESTION) \
               == MainPageScooter.question_is_selected \
               and scooter_page.get_answer_from_main_page(*MainPageLocators.HOW_CALCULATE_RENTAL_TIME_ANSWER) \
               == scooter_page.answers['how_calculate']
    @allure.title('Можно ли заказать самокат прямо на сегодня?')
    @allure.description('На странице ищем элемент аккордеона Можно ли заказать самокат прямо на сегодня? '
                        'и кликаем на него')
    def test_click_on_can_i_order_today(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.CAN_ORDER_TODAY_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.CAN_ORDER_TODAY_QUESTION) \
               == MainPageScooter.question_is_selected \
               and scooter_page.get_answer_from_main_page(*MainPageLocators.CAN_ORDER_TODAY_ANSWER) \
               == scooter_page.answers['can_order_today']
    @allure.title('Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description('На странице ищем элемент аккордеона Можно ли продлить заказ или вернуть самокат раньше? '
                        'и кликаем на него')
    def test_click_on_can_expent_reurn_earlier(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.CAN_EXPEND_RETURN_EARLIER_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.CAN_EXPEND_RETURN_EARLIER_QUESTION) \
               == MainPageScooter.question_is_selected \
               and scooter_page.get_answer_from_main_page(*MainPageLocators.CAN_EXPEND_RETURN_EARLIER_ANSWER) \
               == scooter_page.answers['can_expend']
    @allure.title('Вы привозите зарядку вместе с самокатом?')
    @allure.description('На странице ищем элемент аккордеона Вы привозите зарядку вместе с самокатом? '
                        'и кликаем на него')
    def test_click_on_charging_with_a_scooter(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.CHARGING_WITH_A_SCOOTER_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.CHARGING_WITH_A_SCOOTER_QUESTION) \
               == MainPageScooter.question_is_selected \
               and scooter_page.get_answer_from_main_page(*MainPageLocators.CHARGING_WITH_A_SCOOTER_ANSWER) \
               == scooter_page.answers['charging_with_a_scooter']
    @allure.title('Можно ли отменить заказ?')
    @allure.description('На странице ищем элемент аккордеона Можно ли отменить заказ? '
                        'и кликаем на него')
    def test_click_on_can_cancel_order(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.CAN_CANCEL_ORDER_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.CAN_CANCEL_ORDER_QUESTION) \
               == MainPageScooter.question_is_selected \
               and scooter_page.get_answer_from_main_page(*MainPageLocators.CAN_CANCEL_ORDER_ANSWER) \
               == scooter_page.answers['can_cancel']
    @allure.title('Я живу за МКАДом, привезёте?')
    @allure.description('На странице ищем элемент аккордеона Я живу за МКАДом, привезёте? '
                    'и кликаем на него')
    def test_click_on_live_further_than_mkad(self, driver):
        scooter_page = MainPageScooter(driver)
        scooter_page.wait_for_load_main_page()
        scooter_page.set_element_by_main_page(*MainPageLocators.LIVE_FURTHER_THAN_MKAD_QUESTION)
        assert scooter_page.get_attribute_for_question(*MainPageLocators.LIVE_FURTHER_THAN_MKAD_QUESTION) \
                == MainPageScooter.question_is_selected \
                and scooter_page.get_answer_from_main_page(*MainPageLocators.LIVE_FURTHER_THAN_MKAD_ANSWER) \
                == scooter_page.answers['further_than_mkad']