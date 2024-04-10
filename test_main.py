import pytest
import requests
from config import EMAIL, PASSWORD
from main import visits_in_russia, geo_logs, uniq_geo_id, max_sales_sources, stats, check_directory_exist, \
    _login_in_profile, create_new_directory_in_yandex_disk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# ______________________________________
# Задача №1 unit-tests
# Напишите тесты на любые 3 задания из занятия «Коллекции данных»
# модуля «Основы языка программирования Python».

# Создаем тест для проверки корректности работы функции visits_in_russia (пока без параметризации)
def test_visits_in_russia_ok():
    result = visits_in_russia(geo_logs)
    expected = [
        {'visit1': ['Москва', 'Россия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    assert result == expected

# Cоздаем тест для проверки корректности работы функции uniq_geo_id с параметризацией
@pytest.mark.parametrize(
    'ids, expected', (
            [
                {'user1': [213, 213, 213, 15, 213],
                 'user2': [54, 54, 119, 119, 119],
                 'user3': [213, 98, 98, 35]
                 },
                [15, 35, 54, 98, 119, 213]
            ],
            [
                {'user1': [177, 13, 14, 1, 14],
                 'user2': [1765, 23, 23, 23, 1765],
                 'user3': [2, 100, 4141, 35]
                 },
                [1, 2, 13, 14, 23, 35, 100, 177, 1765, 4141]
            ])
)
def test_uniq_geo_ids_ok(ids, expected):
    result = uniq_geo_id(ids)
    assert result == expected

# Создаем тест для проверки функции определения ресурса с максимальной продажей (с декоратором, пропускающим тест, 
# если значение менее 130)

@pytest.mark.skipif(max_sales_sources(stats)[1] < 130, reason='Too small value')
def test_max_sales_sources_skipped():
    result = max_sales_sources(stats)[1]
    assert result > 100

# ______________________________________
# Задача 2. Автотест API Яндекса

# Создаем тест для проверки функции создания новой папки в Яндекс Диске, пропускаем тест, если результат проверки 409 (путь уже существует)

@pytest.mark.skipif(create_new_directory_in_yandex_disk('Music')[-1] == 409, reason='Path already exists')
def test_check_of_directory_creation_ok():
    result = create_new_directory_in_yandex_disk('Music')[-1]
    expected = 201
    assert result == expected

# Создаем тест для  проверки функции определения наличия папки в Яндекс Диске 

def test_check_directory_exist_ok():
    result = check_directory_exist('Music')
    expected = 200
    assert result == expected

# Создаем тест с проверкой наличия предлагаемой к созданию папки на Яндекс Диске

def test_check_of_directory_creation_failed_409():
    result = create_new_directory_in_yandex_disk('Music')[-1]
    expected = 409
    assert result == expected


# Задача 3. Дополнительная (не обязательная)
# Применив selenium, напишите unit-test для авторизации на Яндексе
# по url: https://passport.yandex.ru/auth/

# Создаем тест с проверкой успешности авторизации в Яндексе (путем проверки успешного входа на страницу id.yandex.ru/personal)

def test_authorization_successfully_finished():
    browser = webdriver.Chrome()
    browser.get("https://passport.yandex.ru/auth")
    time.sleep(2)
    _login_in_profile(browser)
    response = requests.get("https://id.yandex.ru/personal").status_code
    expected = 200
    assert response == expected




