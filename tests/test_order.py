import allure
import pytest
from pages.orderpage import OrderPage
from pages.mainpage import MainPageLocators

class TestOrderScooter:
    @allure.title('Кнопка Заказать вверху страницы')
    @allure.description('В верхней части главной страницы ищем кнопку Заказать и кликаем на нее')
    def test_click_on_button_order_in_head(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_load_main_page()
        order_page.click_button_by_order_in_head()
        assert order_page.check_url() == order_page.orderpage_url
    @allure.title('Кнопка Заказать внизу страницы')
    @allure.description('В нижней части главной страницы ищем кнопку Заказать и кликаем на нее')
    def test_click_on_button_order_in_footer(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_load_main_page()
        order_page.click_button_by_order_in_footer()
        assert order_page.check_url() == order_page.orderpage_url
    @allure.title('Заполнение формы заказа')
    @allure.description('Заполняем форму заказа, которую видим после нажатия кнопки Заказать')
    @pytest.mark.parametrize('firstname, surname, address, metro, phonenumber, date, rental_periode, color, comment',
                             [['Иван', 'Иванов', 'г. Москва, ул Ивановская 13-133', 'Черкизовская', 89152541236, '22',
                               'двое суток', 'серый', 'Зимняя резина'],
                              ['Акакий', 'Тестов', 'г. Москва, ул Узкая 11-111', 'Сокольники', 89962312938, '27',
                               'сутки', 'черный', 'Летняя резина']])
    def test_filling_user_by_order(self, driver, firstname, surname, address, metro, phonenumber, date,
                                   rental_periode, color, comment):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.set_element_by_order_for_who(firstname, surname, address, metro, phonenumber)
        assert driver.find_element(*OrderPage.HEADER_ABOUT_RENT)
        order_page.set_element_by_order_about_rent(date, rental_periode, color, comment)
        assert driver.find_element(*OrderPage.ORDER_COMPLITED)