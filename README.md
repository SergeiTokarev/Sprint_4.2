# проект автоматизации тестирования отдельного функционала учебного сервиса по заказу самокатов https://qa-scooter.praktikum-services.ru/
1. Проект реализован с помощью фреймвойрка pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Тесты сгруппированы в файлы в дирректории tests:
accordion.py
test_click_on_how_much
test_click_on_want_some_scooters
test_transition_to_main_page_click_logo
test_transition_to_yandex_page
4.Классы страниц, локаторы, методы для работы с элементами страниц находятся в директории  pages
в файлах basepage.py (общие методы), mainpage.py, orderpage.py, yandexpage.py.
5. Команда для запуска pytest -v tests/filename.py --alluredir=allure_results
6.Отчеты о тестировании находятся в директории allure_results
7.Просмотр отчетов: allure serve allure_results