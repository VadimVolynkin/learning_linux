
# ===============================================================================================
# REST (REpresentational State Transfer) 
# сервисы на базе REST называют RESTful
# ===============================================================================================
# REST API абстрактный слой между клиентом и сервером
# REST API не должен зависеть от бекэнда
# REST работает по HTTP
# по REST протоколу работает AJAX
# четкого стандарта на REST нет
# желательно чтобы данные ответа не содержали лишней информации. Минимум запросов - максимум полезных данных.
# после попадания API на прод вносить правки в него нельзя. Если очень надо - создается новый роут с новой версией.


# ===== ВАЖНО
# при проектировании API нужно определить единую структуру ответов для всех разработчиков в команде
# составить документацию к API
# тесты к API

# ===== 6 ПРАВИЛ REST архитектуры

# 1. Клиент-Сервер
Должно быть разделение между сервером, который предлагает сервис и клиентом, который использует ее.

# 2. Stateless
Клиент каждый раз отправляет запрос серверу со всеми параметрами(сервер не обязан хранить информацию о состоянии клиента - каждый запрос как новый).

# 3. Кэширование
В каждом запросе клиента должно явно содержаться указание о возможности кэширования ответа и получения ответа из существующего кэша.

# 4. Уровневая система
Клиент может взаимодействовать не напрямую с сервером, а с произвольным количеством промежуточных узлов. При этом клиент может не знать о существовании промежуточных узлов, за исключением случаев передачи конфиденциальной информации.

# 5. Унификация
Унифицированный программный интерфейс сервера.
????

# 6. Код по запросу
Сервера могут поставлять исполняемый код или скрипты для выполнения их на стороне клиентов.



# ===============================================================================================
# RESOURCES and METHODS
# ===============================================================================================
# ресурсы представлены в виде URI
# клиенты работают с ресурсами отправляя на URI доступные HTTP методы
# данные в теле запроса могут быть JSON blob, XML или аргументы в URL
# данные в теле ответа обычно JSON blob или XML

GET      
# получить example.com/api/v1/articles/123
# данные передаются в самом URL

POST
# создать   example.com/api/v1/articles
# данные отправляются в теле запроса

PUT
# обновить  example.com/api/v1/articles/123
# данные отправляются в теле запроса

DELETE
# удалить   example.com/api/v1/articles/123
# данные передаются в самом URL 

HEAD
# выполнить какое то другое действие example.com/api/v1/logout

# ===============================================================================================
# ТИПИЧНЫЙ ОТВЕТ JSON
# ===============================================================================================
# код ответа можно передать:
# - в структуре ответе в "status": 200(при таком варианте http статус всегда 200)
# - добавить к статусу http ответа

{
  "status": 200,
  "data": {
    "title": "Article 123",
    "text": "some text"
  }
}


200 # успешно

400 # неправильные входные данные
401 # неавторизованный доступ
404 # отсутствует запращиваемый URI(нет такой страницы)
405 # метод запроса не поддерживается

500 # внутренняя ошибка сервера(что угодно)
507 # переполненное хранилище
524 # таймаут превышен


# ===============================================================================================
# ПРИМЕР ТЕСТА API для сущности Пользователь
# ===============================================================================================

1. Получить список всех
2. Добавить нового
3. Получить список всех, убедиться что новый там есть
4. Отредактировать пользователя
5. Прочитать пользователя, убедиться что редактирование было успешным
6. Удалить пользователя
7. Получить всех, убедиться что удаленного пользователя нет














