# Задание 2: API-тестирование ручек для Stellar Burgers
https://stellarburgers.nomoreparties.site/

# Документация API
https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89

### Тесты:
test_create_user - тесты создания пользователя  
test_login- тесты авторизации пользователя  
test_edit_user_data - тесты на изменение пользовательских данных  
test_create_order - тесты на создание заказа  
test_get_order_list - тесты получения заказов пользователя  


### Запуск тестов
запустить все тесты:
```bash
pytest -v tests
```
зпустить все тесты с генерацией отчетов  
```bash
pytest tests --alluredir=allure_results 
```
