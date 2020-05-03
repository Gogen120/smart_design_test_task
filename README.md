# Тестовое задание Smart Design

### Локальный запуск
**Переменные окружения**:
* MONGO_HOST - хост MongoDB (если запускается в докере, то должен быть равен имени контейнера, в котором запущена MongoDB, т.е `smart_design.mongo`)
* MONGO_PORT - порт MongoDB (по-умолчанию 27017)
* DB_NAME - имя базы, к которой подключиться (по-умоланию `smart_design`)

Для запуска должен быть установлен `docker` и `docker-compose`.
Контейнеры с mongo и веб-сервером поднимаются следующей командой: `docker-compose -f dc.dev.yaml up --build -d`

После выполнения этой команды должны быть видны 2 контейнера. Увидеть их можно командой `docker ps`

Можно запустить сервер локально: Для этого нужно поднять только контейнер с MongoDB, а сервер запустить с помощью следующих команд: `pip install -e .`, `python -m smart_design_store`

### Curl команды для прохождения тестового сценария
1. Создание товара:
    ```curl -d '{"name":"IPhone22", "description":"brand new iphone", "params":[{"name":"size", "value": "20"}, {"name": "color", "value": "black"}]}' -H "Content-Type: application/json" -X POST http://localhost:8080/product```

2. Нахождение товара по параметрам:
    ```curl -d '{"param_name":"color", "param_value":"black"}' -H "Content-Type: application/json" -X POST http://localhost:8080/product/params```

3. Получение деталей найденного товара:
    ```curl http://localhost:8080/product/id/<id из предыдущего запроса>```
