# test_task_back

Тестовое задание (микросервис)

Для выполнения этого задания я выбрал фреймворк Django. В файле views.py приложения request_handler я реализовал функции Method_A и Method_B в соответствии с заданием.

Method_A возвращает json данные (new_json), полученные при обработке xml файла, на поступивший запрос.

Method_B принимает в качестве параметров три значения: символьный код валюты, дату 1 и дату 2. Затем он конвертирует дату в нужный для дальнейшего запроса формат (из YYYY-MM-DD в DD/MM/YYYY) и на основе ранее полученных json данных (new_json), при помощи функции parent_code_by_code, преобразует полученный символьный код в ParentCode, который тоже нужен для запроса. После этого Method_B делает запрос по сгенерированному url из полученных данных. В качестве ответа приходят xml данные. Вытаскиваем из них необходимые нам данные, преобразуем в json и отправляем на клиентскую сторону.

### Примеры вызовов методов:

1. http://127.0.0.1:8000/method_a/

![image](https://user-images.githubusercontent.com/35337991/130448928-6cbcf635-da5c-497a-8504-dd69d91472ce.png)

2. http://127.0.0.1:8000/method_b/USD/2001-03-02/2001-03-14/

![image](https://user-images.githubusercontent.com/35337991/130449215-29819534-99d5-4822-9d3b-27c9a06d04f3.png)

### Теперь вместе с клиентской частью:

1. Method_A

![image](https://user-images.githubusercontent.com/35337991/130449466-61d42e9d-2b3e-4781-b476-70140b8da762.png)

![image](https://user-images.githubusercontent.com/35337991/130449520-e19aec86-d035-4db2-9c9c-3889f309ade9.png)

2. Method_B

![image](https://user-images.githubusercontent.com/35337991/130449569-7b9e177a-6125-4101-89b0-4a6ad1d948fa.png)

![image](https://user-images.githubusercontent.com/35337991/130449624-32ff4664-f25e-4642-855f-e6d2624ff159.png)

Вот так выглядит страница при загрузке:

![image](https://user-images.githubusercontent.com/35337991/130449843-5288351c-987f-4f85-9f5d-5ce9b0540490.png)

### Использованные технологии:

1. Django 3: для написания бэкенда.
    1. Python 3.9
        1. Библиотека xmltodict: для преобразования xml в json
        2. Библиотека requests: для создания запроса на технические ресурсы Банка России
    2. Библиотека django-cors-headers: для разрешения входящих запросов
2. Vue: для написания фронтенда
    1. JavaScript
        1. Библиотека axios: для создания запроса на сервер django
    2. HTML
    3. CSS
