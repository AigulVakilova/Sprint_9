# Sprint_9 — Автотесты для сервиса Foodgram

## Описание проекта
Автотесты для учебного сервиса Foodgram. Проект содержит UI-тесты для проверки основных пользовательских сценариев: регистрации, авторизации и создания рецепта.

## Технологии
- Python 3.13
- Selenium 4.39.0
- pytest 9.0.1
- Allure 2.15.3
- Selenoid
- Docker
- Page Object Model (POM)

## Структура проекта
```
SPRINT_9/
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD GitHub Actions
├── assets/
│   └── omelette.png            # Тестовое изображение для загрузки
├── locators/                   # Локаторы элементов
│   ├── login_page_locators.py
│   ├── main_page_locators.py
│   ├── recipe_page_locators.py
│   └── registration_page_locators.py
├── pages/                      # Page Object Model
│   ├── base_page.py            # Базовые методы
│   ├── login_page.py           # Методы страницы авторизации
│   ├── main_page.py            # Методы главной страницы
│   ├── recipe_page.py          # Методы страницы создания рецепта
│   └── registration_page.py   # Методы страницы регистрации
├── tests/                      # Тесты
│   ├── test_login.py           # Тесты авторизации
│   ├── test_recipe.py          # Тесты создания рецепта
│   └── test_registration.py   # Тесты регистрации
├── allure-report/              # Сгенерированный Allure-отчёт
├── browsers.json               # Конфигурация браузеров для Selenoid
├── conftest.py                 # Фикстуры pytest
├── docker-compose.yml          # Сборка проекта с Selenoid
├── Dockerfile                  # Образ проекта с тестами
├── pytest.ini                  # Конфигурация pytest
├── requirements.txt            # Зависимости проекта
├── test_data.py                # Тестовые данные
└── urls.py                     # URL-адреса приложения
```

## Тестовые сценарии

| Файл | Что проверяет |
|------|--------------|
| `test_registration.py` | Создание нового аккаунта, переход на страницу авторизации |
| `test_login.py` | Авторизация пользователя, отображение кнопки «Выход» |
| `test_recipe.py` | Создание рецепта, отображение карточки с названием |

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск тестов локально
```bash
pytest -v
```

## Запуск через Docker с Selenoid
```bash
docker-compose up
```

## Генерация Allure-отчёта
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## CI/CD
Тесты запускаются автоматически при push в ветки `main` и `develop`.
Allure-отчёт публикуется в GitHub Pages.
