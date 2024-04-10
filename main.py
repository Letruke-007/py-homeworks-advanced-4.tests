import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from config import EMAIL, PASSWORD, TOKEN

# Домашнее задание Коллекции данных

# Задача 1. Визиты в Россию

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def visits_in_russia(geo_logs):
    sorted_geo_logs = []
    result = [geo_log for geo_log in geo_logs if "Россия" in next(iter(geo_log.values()))]
    return result


print(visits_in_russia(geo_logs))

# Задача 2. Уникальные гео-ID

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def uniq_geo_id(ids):
    sorted_ids = []
    for elm in ids.values():
        sorted_ids += elm
    sorted_ids = sorted(set(sorted_ids))
    return sorted_ids


print(uniq_geo_id(ids))

# Задача 3. Частотность поисковых запросов по количеству слов

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


def queries_frequency(queries):
    counter1 = 0
    counter2 = 0
    counter3 = 0

    for i in range(len(queries)):
        words = queries[i].split(' ')
        if len(words) == 1:
            counter1 += 1
        elif len(words) == 2:
            counter2 += 1
        elif len(words) == 3:
            counter3 += 1
    res_ = counter1 + counter2 + counter3

    if res_ != 0:
        return (f'Поисковых запросов, состоящих из 1 слова, {counter1 / res_ * 100}%\n'
                f'Поисковых запросов, состоящих из 2 слов, {counter2 / res_ * 100}%\n'
                f'Поисковых запросов, состоящих из 3 слов, {counter3 / res_ * 100}%')
    else:
        return 'Все поисковые запросы не подходят под критерии поиска (1,2 или 3 слова)'

print(queries_frequency(queries))

# Задача 4. Возврат значения с максимальные объемом продаж

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def max_sales_sources(sources):
    res_ = sorted(sources.items(), key=lambda x: x[1])
    return res_[-1]


print(max_sales_sources(stats)[1])


# Задача 2. Автотест API Яндекса

# Создаем функцию создания папки в Яндекс Диск
def create_new_directory_in_yandex_disk(name):
    
  # Указываем базовый URL
    base_url = 'https://cloud-api.yandex.net'

    # Указываем токен для авторизации
    token = TOKEN

    # Прописываем заголовки и URL для создания папки
    headers = {'Authorization': token}
    url_for_creating_new_directory = base_url + '/v1/disk/resources'

    # Указываем параметры (название создаваемой папки)
    params = {'path': f'{name}'}

    # Создаем запрос на создание папки, выполняем его, возвращаем результат и статус код
    response = requests.put(url_for_creating_new_directory,
                            headers=headers,
                            params=params)

    return response.json(), response.status_code


# Выводим результат выполнения функции и статус код в принт (на примере папки Music)
print(create_new_directory_in_yandex_disk('Music'))

# Создаем функцию проверки существования папки с заданным значением
def check_directory_exist(name):
    # Указываем базовый URL
    base_url = 'https://cloud-api.yandex.net'

    # Указываем токен для авторизации
    token = 'y0_AgAAAABeEx4RAADLWwAAAAEBfeq1AADSxclQIV5LK7INMf2RdmcoKiiTxA'

    # Прописываем заголовки и URL для проверки существования папки
    headers = {'Authorization': token}
    url_for_check_directory_exist = base_url + '/v1/disk/resources'

    # Указываем параметры проверяемой на наличие папки
    params = {'path': f'{name}'}

    # Создаем запрос на проверку наличия на Яндексе Диске папки с заданным названием
    response = requests.get(url_for_check_directory_exist,
                            headers=headers,
                            params=params)
    # Возвращаем статус код
    return response.status_code


print(check_directory_exist('Music'))

# Задача 3. Дополнительная (не обязательная)
# Применив selenium, напишите unit-test для авторизации на Яндексе
# по url: https://passport.yandex.ru/auth/

# Создаем функцию авторизации в Яндексе с использованием selenium
def _login_in_profile(browser):
    browser.find_element(By.ID, 'passp-field-login').send_keys(EMAIL)
    time.sleep(1)
    browser.find_element(By.ID, 'passp:sign-in').click()
    time.sleep(1)
    browser.find_element(By.ID, 'passp-field-passwd').send_keys(PASSWORD)
    browser.find_element(By.ID, 'passp:sign-in').click()
    time.sleep(2)

