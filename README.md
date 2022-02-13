# tz Библиотека книг в которой можно выбрать интересующую книгу

## **Мини-проект "Библиотека книг"**
* проект написан на Django 4 + Django Rest Framework
* в качестве тестирования прошу использовать приложение postman, либо сайт https://www.postman.com/
* база данных подкючена через postgresql

### Реализованы следующие задачи:
1) Регистрация пользователя -
**/api/create_user/**

* username
* password

2) Авторизация пользователя
**/api-auth/login/**

#### Поля для заполнения (POST-запрос)
* username
* password

3) CRUD модели Книги с фильтрацией по автору, жанру и сортировка по дате выпуска
**/api/books/**

#### Поля для заполнения
* name
* authors
* genre
* image 
* description
* release_date

4) Создание модели Авторов
**/admin/**

#### Поля для заполнения
* first_name
* last_name
* image 
* birthday_year

5) Создание модели Жанр книг
**/admin/**

#### Поля для заполнения
* name
