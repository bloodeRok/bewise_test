# Bewise
Этот проект реализует генерацию и сохранение вопросов викторины.

## Установка

### Требования
- [git](https://git-scm.com/)
- [docker](https://docs.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

### Запуск проекта
1. Клонируйте репозиторий:
`git clone https://github.com/bloodeRok/bewise_test.git`.
2. Перейдите в директорию проекта: `cd "path to project"`.
3. Создайте в корневом каталоге файл .env (пример находится в .env.example) 
и заполните его.
4. Запустите проект с помощью docker-compose: `docker-compose up -d --build`.

### Документация 
Документация к проекту доступна по адресу http://127.0.0.1:1883/api/swagger.
