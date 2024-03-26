# task_manager
Планировщик задач, в котором каждая задача имеет поля: имени, описания и состояния ("добавлена", "в работе", "выполнена"). К данному планировщику разработать API, работающий поверх HTTP

## Стек:
- Python
- Django Rest Framework
- Docker
- UWSGI
- nginx
- swagger
- PostgreSQL
- djoser для jwt(хотя он нигде не используется)

## Запуск проекта
 
 env.example -> .env

 run_uwsgi.sh -> LF

# Docker

 docker-compose up -d --build

 docker-compose up

 Миграции и сбор статики в файле run_uwsgi.sh, применяются при сборке контейнера
 
 docker-compose exec tasks_app createsuperuser(для доступа к админ панели)

# Локально

 env.POSTGRES_HOST -> localhost

 (данные для Postgres в файле .env.example)

 cd task_manager\app

 python manage.py runserver

 python manage.py makemigrations

 python manage.py createsuperuser(для доступа в админ панель)


## Описание

Небольшое API для создания задач, документация по http://127.0.0.1/swagger/

Альтернативно управление через админ-панель http://127.0.0.1/admin/