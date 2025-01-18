## Aggregator

Предоставляет интерфейс для обзора фаззинг целей.
Обращается к модулям `agent`.


## Создание окружения

    $ apt install python3 python-is-python3

    $ python -m venv /path/to/new/virtual/environment
    $ source <venv>/bin/activate
    $ pip install -r requirements.txt

## App
Директория `app` содержит Django-проект `fi_aggregator`,
реализующий аггрегацию иноформации о фаззинг процессах.

Активация миграций

    $ python manage.py migrate

После изменения моделей, обновить миграции:

    $ python manage.py makemigrations <app_name>

Проверить SQL для миграции (изменение БД не происходит):

    $ python manage.py sqlmigrate <app_name> 0001

Суперпользователь:

    $ python manage.py createsuperuser

Запуск под сервером разработки

    $ python manage.py runserver
