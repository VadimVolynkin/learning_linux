https://developer.mozilla.org/en-US/docs/Web/HTTP

# ===============================================================================================
# HTTP
# ===============================================================================================
# текстовый протокол прикладного уровня для передачи данных
# используется также в качестве транспорта для других протоколов прикладного уровня: SOAP, XML-RPC, WebDAV
# благодаря возможности указания способа кодирования сообщения клиент и сервер могут обмениваться двоичными данными
# HTTP протокол не хранит состояния. Сервер может хранить IP-адреса и заголовки запросов последних клиентов. Однако сам протокол не осведомлён о предыдущих запросах и ответах, в нём не предусмотрена внутренняя поддержка состояния.
# Для хранения информации о состоянии клиенты могут использовать куки, а сервера сессии.
# HTTP устанавливает отдельную TCP-сессию на каждый запрос; в более поздних версиях HTTP может несколько запросов в ходе одной TCP-сессии

# ПО для работы с HTTP делиться на 3 категории:
# - Серверы как основные поставщики услуг хранения и обработки информации (обработка запросов)
# - Клиенты — конечные потребители услуг сервера (отправка запроса)
# - Прокси (посредники) для выполнения транспортных служб


# ===============================================================================================
# message-body (Тело сообщения)
# ===============================================================================================
# используется для передачи тела объекта
# тело сообщения может быть добавлено в запрос, только если метод запроса допускает тело объекта
# присутствие тела в запросе отмечается добавлением к заголовкам запроса поля Content-Length или Transfer-Encoding
# тело включается или не включается в ответ в зависимости от метода запроса
# ответы 1xx (Информационные), 204 (Нет содержимого, No Content), и 304 (Не модифицирован, Not Modified) не должны содержать тела сообщения. Все другие ответы содержат тело сообщения, даже если оно имеет нулевую длину


# ===============================================================================================
# МЕТОДЫ
# ===============================================================================================
# Методы могут быть безопасными, идемпотентными или кэшируемыми.

GET
# обычно используется для получения информации от сервера.
# может использоваться для включения какого либо процесса, тогда нужно отправить ответ типа "процесс запущен"
# клиент может передавать параметры в URI так: GET /path/resource?param1=value1&param2=value2 HTTP/1.1

POST
# передает в теле запроса данные на сервер, обычно используется для создания новых записей
# используется для загрузки файлов на сервер
# в тело ответа следует включить сообщение об итоге выполнения запроса: 201 (Created) с указанием URI нового ресурса в заголовке Location
# ответ сервера на выполнение POST не кэшируется

PUT
# передает в теле запроса данные на сервер для изменения записи. 
# Если такой записи нет, то создает ее и возвращает 201 (Created).
# Если же ресурс был изменён, то сервер возвращает 200 (Ok) или 204 (No Content).
# ответ сервера на метод PUT не кэшируются. 

PATCH
# аналогично PUT, но обновляет только часть ресурса

DELETE
# удаляет указанный ресурс

HEAD
# запрашивает ресурс так же, как и GET, но возвращает только заголовки без тела. Позволяет узнать есть ли документ на сервере.
# заголовки ответа могут кэшироваться

OPTIONS
# OPTIONS используется для описания параметров соединения с ресурсом(оступные методы)
# Запрос OPTIONS *  вернет параметры для всего сервера
# Результат выполнения не кешируется

CONNECT
# преобразует соединение запроса в прозрачный TCP/IP-туннель, обычно для установления защищённого SSL-соединения через нешифрованный прокси

TRACE
# вернет запрос с указанием как промежуточные серверы добавляют или изменяют информацию в запросе


# ===============================================================================================
# КОДЫ ОТВЕТОВ СЕРВЕРА
# ===============================================================================================

# Информационный
100 Continue
101 Switching Protocols
103 Early Hints

# Успех
200 OK
201 Created
202 Accepted
203 Non-Authoritative Information
204 No Content
205 Reset Content
206 Partial Content

# Перенеправление
300 Multiple Choices
301 Moved Permanently
302 Found
303 See Other
304 Not Modified
307 Temporary Redirect
308 Permanent Redirect

# Ошибки клиента
400 Bad Request
401 Unauthorized
402 Payment Required
403 Forbidden
404 Not Found
405 Method Not Allowed
406 Not Acceptable
407 Proxy Authentication Required
408 Request Timeout
409 Conflict
410 Gone
411 Length Required
412 Precondition Failed
413 Payload Too Large
414 URI Too Long
415 Unsupported Media Type
416 Range Not Satisfiable
417 Expectation Failed
418 I'm a teapot
422 Unprocessable Entity
425 Too Early
426 Upgrade Required
428 Precondition Required
429 Too Many Requests
431 Request Header Fields Too Large
451 Unavailable For Legal Reasons

# Ошибки сервера
500 Internal Server Error
501 Not Implemented
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
505 HTTP Version Not Supported
506 Variant Also Negotiates
507 Insufficient Storage
508 Loop Detected
510 Not Extended
511 Network Authentication Required

# ===============================================================================================
# ЗАГОЛОВКИ
# ===============================================================================================
Set-Cookie: name=value       # просит установить куки для индентификации пользователя.
Cookie: name=value           # просит читать куки


HTTP/1.1 302 Moved Temporarily
Server: nginx
Date: Sat, 08 Mar 2014 22:29:53 GMT
Content-Type: text/html
Content-Length: 154
Connection: keep-alive
Keep-Alive: timeout=25
Location: http://habrahabr.ru/users/alizar/


# ===============================================================================================
# ПРИМЕР
# ===============================================================================================

# === ЗАПРОС КЛИЕНТА
GET /wiki/страница HTTP/1.1
Host: ru.wikipedia.org
User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5
Accept: text/html
Connection: close
(пустая строка)  

# === ОТВЕТ СЕРВЕРА
HTTP/1.1 200 OK
Date: Wed, 11 Feb 2009 11:20:59 GMT
Server: Apache
X-Powered-By: PHP/5.2.4-2ubuntu5wm1
Last-Modified: Wed, 11 Feb 2009 11:20:59 GMT
Content-Language: ru
Content-Type: text/html; charset=utf-8
Content-Length: 1234
Connection: close
(пустая строка)
(запрошенная страница в HTML)