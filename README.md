Стек технологий:

База данных: MySQL
Кэширование: Redis
Язык программирования: Python
Фреймворк: Django
Фронтенд: HTML (очень базовый)
О сайте:
Простой сайт для записи ежедневных задач.

Самое интересное, чему научился:

Реализовал бекенд, включая регистрацию пользователей, с привязкой к базе данных.
Настроил кэширование с использованием технологии Redis:
В TaskList кэшируется сериализованный список задач текущего пользователя.
В TaskDetail кэшируются детали задачи текущего пользователя.
Проверил работу кэширования с помощью Postman.
Подключил Docker с использованием docker-compose, что позволило управлять контейнерами для приложения, базы данных MySQL и Redis. Это упростило развертывание проекта и интеграцию всех компонентов в единую среду.
Добавил использование переменных окружения для хранения конфиденциальных данных (например, паролей, настроек базы данных) и спрятал их в файле .env, который был исключен из системы контроля версий с помощью .gitignore.
