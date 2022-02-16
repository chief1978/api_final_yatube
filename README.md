### О проекте
Учебный проект API для Yatube. Выполнено в рамках выполнения 9 спринта курса Python-разработчик [Япрактикум](https://practicum.yandex.ru/)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:chief1978/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
> используйте комманду python для Windows окружения

```
python3 -m venv env
```

> для Linux
```
source env/bin/activate
```

> для Windows
```
source env/Script/activate
```

Установите pip

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### OpenAPI

После установки доступен OpenAPI Redoc. Интерфейс достпен по адресу [127.0.0.1:8000](http://127.0.0.1:8000)

### Примеры запросов:

Получить список публикаций:

> http://127.0.0.1:8000/api/v1/posts/

Ответ:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
