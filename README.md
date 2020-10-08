Сайт приюта домашних животных.

Разворачиваем проект:

Скачайте репозиторий

Создайт виртуальное окружение:

python3 -m venv env
Активируйте виртуальное окружение:

 source env/bin/activate
Чтобы установить все требуемые библиотеки python в новом окружении выполните команду:

 pip install -r requirements.txt
Если у вас macOS до выполнения команды pip install -r requirements.txt выполните команду:

    env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2==2.8.4      
Для предотвращения появления ошибки (error: command 'gcc' failed with exit status 1.) при установке зависимостей.

Чтбы запустить сервер введите команду:

python manage.py runserver
Для входа в администравтивную панель проекта создайте суперпользователя при помощи команды:

python manage.py createsuperuser

https://boiling-scrubland-14840.herokuapp.com/
