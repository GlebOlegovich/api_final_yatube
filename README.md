# api_final

1) Клонировать репозиторий и перейти в него в командной строке
2) Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

3) Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4) Выполнить миграции:

```
python3 manage.py migrate
```

5) Запустить проект:

```
python3 manage.py runserver
```
6) Через постман можете делать запросы к нашему API, документация доступна по ссылке 
<http://127.0.0.1:8000/redoc/>


## 20.10.2021 - Отправка на 1ое ревью
Ну, уже хоть не ухожу в академ, остальное допилим)))