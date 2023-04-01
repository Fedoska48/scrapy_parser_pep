# scrapy_parser_pep
# Проект асинхронного парсинга PEP*
*Python Enhancement Proposals

### Технологический стек

Python 3.9, Scrapy 2.5.1

### Автор

Никита Сергеевич Федяев

Telegram: [@nsfed](https://t.me/nsfed)

### О приложении:

Приложение позволяет собрать информацию о документации PEP с ресурса: https://peps.python.org/

### Подготовка к работе парсера

Клонирование репозитория:

*git clone git@github.com:Fedoska48/scrapy_parser_pep.git*

Необходимо создать вирутальное окружение (способ зависит от операционной системы)

Здесь и ниже для Windows:

*python -m venv venv*

Активировать виртуальное окружение:

*source venv/Scripts/activate*

Установить зависимости:

*pip install -r requirements.txt*

## Инструкция:

Находясь в директории проекта, необходимо вызвать в терминале команду:

***scrapy crawl pep***

В папке **/results** находятся результаты парсинга в формате .csv

- pep_(data).csv :: номер PEP, название и статус
- status_summary_(data).csv :: статистика PEP по статусам и сумма документов PEP
