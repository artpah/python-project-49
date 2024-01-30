### Место для бейджиков:
[![Actions Status](https://github.com/artpah/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artpah/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

#Название проекта
Игры разума (Brain Games)  
В проекте реализовано 5 игр. Ниже описание каждой игры.
- игра "Проверка на чётность"
Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное.
- игра "Калькулятор"
Суть игры в следующем: пользователю показывается случайное математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ.
- игра "НОД"(наибольший общий делитель)
Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
- игра "Арифметическая прогрессия"
Суть игры в следующем: пользователю показывается ряд чисел, который образует арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.
- игра "Простое ли число?"
Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число простое, или no — если непростое.  

 Условия для всех игр:
- при верном ответе пользователем игра продолжается, при неверном - завершается.
- всего пользователь должен дать верный ответ 3 раза, после этого игра завершается.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Разработка](#разработка)
- [Команда проекта/Автор](#команда-проекта)

## Технологии
- [Python 3.10.12](https://www.python.org/)
- [Flake8](https://pypi.org/project/flake8/)
- [Prompt](https://pypi.org/project/prompt/)
- [poetry](https://python-poetry.org/)
- [asciinema](https://acciinema.org/)

## Использование
Установите пакет с помощью команды:
pip install git+https://github.com/artpah/python-project-49

## Разработка

### Требования
Для установки и запуска проекта, необходим [poetry](https://python-poetry.org/).

### Установка зависимостей
Для установки зависимостей, выполните команду:
make install

### Запуск
Чтобы запустить утилиту в режиме разработки, выполните команду:
- [make brain-games](https://asciinema.org/a/466YtC9O1qldbScDNMb4PJsND/)
- [make brain-even](https://asciinema.org/a/SPsLRUeDvJU0nx0Uq9znoKOFF/)
- [make brain-calc](https://asciinema.org/a/tsSIGmyg1TR5MFBaFgdJrkaOB/)
- [make brain-gcd](https://asciinema.org/a/RDnAAIvX72n0f7BOiefhgvq63/)
- [make brain-progression](https://asciinema.org/a/NV7nfpBUqX23s68yNz7mimOuj/)
- [make brain-prime](https://asciinema.org/a/KEF9CbYvXfegkAF0fPLIq7yUp/)  
Для запуска утилиты напрямую, выполните команду:
[brain-games](https://asciinema.org/a/NarXhpSPKO5Wrt2ZIEzSzbCL9/)

### Создание билда
Чтобы выполнить сборку, выполните команду:
make build

### Установка
Чтобы выполнить установку пакета, выполните команду:
make package-install

### Удаление пакета
Чтобы выполнить удаление пакета, выполните команду:
poetry remove python-project-49

## Команда проекта
Автор:

- [Артём Пахолков](https://github.com/artpah) -
Python developer
