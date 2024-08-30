1. Настройте свой сервер (система Ubuntu 22.04)
Для работы необходим Nginx, Gunicorn, Django
2. 

Создайте на сервере ssh ключ, запульте из репозиторий из gitlab

(git@github.com:TheShadowfish/CW_8_atomic_habits_docker.git) (git@gitlab.com:test1360134/cw_8.git) код проекта, Код клонировать на свой репозиторий и пулить оттуда. При необходимости прописать в config/settings.py адрес сервера в ALLOWED_HOSTS = [<адрес сервера>] (строка 17) Создайте на сервере в корне проекта файл .env по образцу .env-sample

На сервере должен быть установлен Docker и docker-compose (команда apt-install docker docker-compose)

Создание и последующий запуск контейнера командой docker-compose up -d --build, Либо docker-compose build, а затем docker-compose up -d

При необходимости заполните базу данными, демонстрационные данные:

docker exec -it <ID контейнера приложения> python3 manage.py loaddata data/users_data.json

docker exec -it <ID контейнера приложения> python3 manage.py loaddata data/habits_data.json

