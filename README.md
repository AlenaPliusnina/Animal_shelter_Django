# Сайт приюта домашних животных / Animals shelter web-site

     Django, Sqlite3
     
В репозитории представлен проект для локального запуска. Также проект опубликован на heroku, посмотреть на работу можно по ссылке: https://boiling-scrubland-14840.herokuapp.com/

Разворачиваем проект локально:

1. Скачайте репозиторий.

2. Создайт виртуальное окружение: 
    
       python -m venv env
    
3. Активируйте виртуальное окружение:

       source env/bin/activate
    
4. Чтобы установить все требуемые библиотеки python в новом окружении выполните команду:
     
       pip install -r requirements.txt
    
  Если у вас macOS до выполнения команды pip install -r requirements.txt выполните команду:

    env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2==2.8.4
    
  Для предотвращения появления ошибки (error: command 'gcc' failed with exit status 1.) при установке зависимостей.

5. Чтбы запустить сервер введите команду:

       python manage.py runserver
    
6. Для входа в администравтивную панель проекта создайте суперпользователя при помощи команды:

       python manage.py createsuperuser
 

# Скриншоты

![Главная](/screenshots/screen_1.png)

![Кошки](/screenshots/screen_2.png)

![Кошки подробнее](/screenshots/screen_3.png)

![Собаки](/screenshots/screen_4.png)

![Собаки подробнее](/screenshots/screen_5.png)

![Попугаи](/screenshots/screen_6.png)

![Попугаи подробнее](/screenshots/screen_7.png)

![Контакты](/screenshots/screen_8.png)
