### test and linter statuses
[![Actions Status](https://github.com/artpah/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artpah/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)


# Игры разума (Brain Games)  
В проекте реализовано 5 игр. Ниже описание каждой игры.  
Суть игр:
- игра "Проверка на чётность"  
пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное.
- игра "Калькулятор"  
пользователю показывается случайное математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ.
- игра "НОД"(наибольший общий делитель)  
пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
- игра "Арифметическая прогрессия"  
пользователю показывается ряд чисел, который образует арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.
- игра "Простое ли число?"  
пользователю показывается случайное число. И ему нужно ответить yes, если число простое, или no — если непростое.  

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
```shell
python3 -m pip install --user
git+https://github.com/artpah/python-
project-49.git
```
## Удаление
Удалите пакет с помощью команды:  
```shell
python3 -m pip unistall hexlet-code
```

## Разработка

### Требования
Для установки и запуска проекта, необходим [poetry](https://python-poetry.org/).

### Установка зависимостей
Для установки зависимостей, выполните команду:
``` shell
poetry install
```

### Запуск
Чтобы запустить утилиты, выполните команды:
- [brain-games](https://asciinema.org/a/bL7NxoNwJU2QkSrw4hXgx3gyC/)
- [brain-even](https://asciinema.org/a/j1R61S0JDzU2DOHtl7B2WPxLL/)
- [brain-calc](https://asciinema.org/a/5WhzVPrpoFFgMB8tSGr1V6eJ1/)
- [brain-gcd](https://asciinema.org/a/zQYb8ucXwe7Hn5DLbVZEBty5U/)
- [brain-progression](https://asciinema.org/a/EcQ4F9hzCA1JcqnAkD747Mwh1/)
- [brain-prime](https://asciinema.org/a/LQq3rMEcbwLqMaU0efMBBj8PS/)


### Создание билда
Чтобы выполнить сборку, выполните команду:
```shell
poetry build
```

### Установка
Чтобы выполнить установку пакета, выполните команду:
```shell
poetry package-install
```

## Команда проекта
Автор:

- [Артём Пахолков](https://github.com/artpah) -
Python developer
