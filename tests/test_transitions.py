import allure
import pytest
from pages.orderpage import OrderPage
from pages.yandexpage import YandexPage

class TestTransitions:
    @allure.title('Переход на главную страницу')
    @allure.description('Кликаем на логотип самоката вверху страницы и переходим на главную')
    def test_transition_to_main_page_click_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.set_element_by_main_page(*OrderPage.LOGO_SCOOTER)
        assert order_page.check_url() == order_page.mainpage_url

    @allure.title('Переход на страницу Яндекса')
    @allure.description('Кликаем на надпись Яндекс вверху страницы и переходим на страницу Яндекса')
    def test_transition_to_yandex_page(self, driver):
        yandex_page = YandexPage(driver)
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.set_element_yandex()
        yandex_page.weit_for_load_yandex_page()
        assert yandex_page.get_count_of_windows() == yandex_page.new_window_is_open