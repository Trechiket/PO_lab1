# Contents
- [Общее описание решения](#общее-описание-решения)
- [Описание функций](#описание-функций)
    - [Circle](#circle)
    - [Rectangle](#rectangle)
    - [Square](#square)
    - [Triangle](#triangle)
- [История изменения проекта](#история-изменения-проекта)
- [Unit tests для функции sin](#unit-tests-для-функции-sin)
    - [Описание файла](#описание-файла)
    - [Включенные тесты](#включенные-тесты)
    - [Запуск тестов](#запуск-тестов)

# Общее описание решения
1. Создал папку на компьютере в которую клонировал исходный
репозиторий с помощью команды **git clone**
2. Перешел в репозиторий и создал новую ветку *new_features_408310*
c помощью команды **git branch**
3. Создал новый файл **rectangle.py** c кодом для вычисления площади и периметра прямоугольника.
Добавил файл в индекс с помощью команды **git add**
4. Сделаем коммит с помощью команды **git commit -m** c информацией
о том что был добавлен новый файл **rectangle.py**
5. Создал новый файл **triangle.py** c кодом для вычисления площади и периметра треугольника.
Добавил файл в индекс с помощью команды **git add**
6. Пофиксил ошибку в вычислении перимтра прямоугольника в файле 
**rectangle.py** и зафиксировал изменения в индекс с помощью команды
**git add**
7. Сделаем коммит с помощью команды **git commit -m** c информацией
о том что был добавлен новый файл **rectangle.py**
8. Построил граф всего репозитория с однострочным выводом коммитов
с помощью команды **git log --graph --oneline --all**
9. Построил граф истории текущей ветки с однострочным выводом коммитов
с помощью команды **git log --graph --oneline**
10. Построив граф истории, я взял хэши последних двух коммитов 
и посмотрел изменения которые были в них внесены с помощью команды
**git show**
11. Перешёл в главную ветку **main** c помощью команды **git checkout main**
и слил ветку *new_features_408310* в ветку **main** с помощью
команды **git merge**
12. Для того чтобы сделать **Pull Request**, я сначала форкнул
репозиторий товарища, а после клонировал его себе на компьютер.
Создал и перешел на новую ветку, внёс в репозиторий изменения, добавив новый файл
**romb.py**, зафиксировал их в индекс, сделал коммит и запушил
в свой репозиторий. Далее на гитхабе я сделал **Pull Request**
своему товарищу, предварительно обсудив его с ним, и дождался
его принятия
13. Удалил ветку *new_features_408310* c помощью команды 
**git branch -d new_features_408310**



# Описание функций
## Circle
### def area(r)
- **Описание функции**: Функция возвращает площадь круга по заданному радиусу
- **Параметры**: *r (float)* - радиус круга
- **Возвращаемое значение**: *math.pi * r * r (float)* - площадь круга


    input: 1
    output: 3.141592653589793


### def perimeter(r)
- **Описание функции**: Функция возвращает длину окружности по заданному радиусу
- **Параметры**: *r (float)* - радиус окружности
- **Возвращаемое значение**: *2 * math.pi * r (float)* - длина окружности


    input: 1
    output: 6.283185307179586



## Rectangle
### def area(a, b)
- **Описание функции**: Функция возвращает площадь прямоугольника по заданным сторонам
- **Параметры**: *a (float)* - сторона прямоугольника <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                 *b (float)* - сторона прямоугольника
- **Возвращаемое значение**: *a * b (float)* - площадь прямоугольника


    input: 1.5, 2.5
    output: 3.75


### def perimeter(a, b)
- **Описание функции**: Функция возвращает периметр прямоугольника по заданным сторонам
- **Параметры**: *a (float)* - сторона прямоугольника <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                 *b (float)* - сторона прямоугольника
- **Возвращаемое значение**: *2 * (a + b) (float)* - периметр прямоугольника


    input: 1.5, 2.5
    output: 8.0



## Square
### def area(a)
- **Описание функции**: Функция возвращает площадь квадрата по заданной стороне
- **Параметры**: *a (float)* - сторона квадрата 
- **Возвращаемое значение**: *a * a (float)* - площадь квадрата


    input: 1.25
    output: 1.5625


### def perimeter(a)
- **Описание функции**: Функция возвращает периметр квадрата по заданной стороне
- **Параметры**: *a (float)* - сторона квадрата
- **Возвращаемое значение**: *4 * a (float)* - периметр квадрата


    input: 1.25
    output: 5.0



## Triangle
### def area(a, h)
- **Описание функции**: Функция возвращает площадь треугольника по заданной стороне и проведенной к ней высоте
- **Параметры**: *a (float)* - сторона треугольника <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                 *h (float)* - высота треугольника
- **Возвращаемое значение**: *a * h / 2 (float)* - площадь треугольника


    input: 2.5, 1.2
    output: 1.5

### def perimeter(a, b, c)
- **Описание функции**: Функция возвращает периметр треугольника по заданным сторонам
- **Параметры**: *a (float)* - сторона треугольника <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                 *b (float)* - сторона треугольника <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                 *c (float)* - сторона треугольника
- **Возвращаемое значение**: *(a + b + c) (float)* - периметр прямоугольника


    input: 1.5, 2.5, 2
    output: 5.7


# История изменения проекта


✶&nbsp; <span style="color:orange;">commit dabea2aff868a955b71ad520d6423c4d2ee6d2fe</span> (<span style="color:blue;">HEAD -></span> <span style="color:lightgreen;">main</span>) <br>
&nbsp;<span style="color:red;">|</span> &nbsp; Author: Trechiket <gregory.b9@mail.ru> <br>
&nbsp;<span style="color:red;">|</span> &nbsp; Date: &emsp;   Wed Sep 27 15:27:17 2023 +0300 <br>
&nbsp;<span style="color:red;">|</span> <br>
&nbsp;<span style="color:red;">|</span> &emsp;&emsp;&emsp; new file <br>
&nbsp;<span style="color:red;">|</span> <br>
✶&nbsp; <span style="color:orange;">commit 809b219f5d0858e4d732fc6e94eb3f17c4587723</span> (<span style="color:red;">origin/main</span>, <span style="color:red;">origin/HEAD</span>) <br>
&nbsp;<span style="color:red;">|</span> &nbsp; Author: Trechiket <gregory.b9@mail.ru> <br>
&nbsp;<span style="color:red;">|</span> &nbsp; Date:   Thu Sep 21 21:40:07 2023 +0300 <br>
&nbsp;<span style="color:red;">|</span> <br>
&nbsp;<span style="color:red;">|</span> &emsp;&emsp;&emsp; fixed mistake in rectangle.py <br>
&nbsp;<span style="color:red;">|</span> <br>
✶&nbsp; <span style="color:orange;">commit 9eee4b65424644bc12a440b4861d89c351df65ac</span> <br>
&nbsp;<span style="color:red;">|</span> &nbsp; Author: Trechiket <gregory.b9@mail.ru> <br>
&nbsp;<span style="color:red;">|</span> &nbsp; Date:   Thu Sep 21 21:36:18 2023 +0300<br>
&nbsp;<span style="color:red;">|</span><br>
&nbsp;<span style="color:red;">|</span> &emsp;&emsp;&emsp; add new file - rectangle.py<br>
&nbsp;<span style="color:red;">|</span> <br>
✶&nbsp; <span style="color:orange;">commit d078c8d9ee6155f3cb0e577d28d337b791de28e2</span><br>
&nbsp;<span style="color:red;">|</span> &nbsp; Author: smartiqa <info@smartiqa.ru><br>
&nbsp;<span style="color:red;">|</span> &nbsp; Date:   Thu Mar 4 14:55:29 2021 +0300<br>
&nbsp;<span style="color:red;">|</span><br>
&nbsp;<span style="color:red;">|</span> &emsp;&emsp;&emsp; L-03: Docs added<br>
&nbsp;<span style="color:red;">|</span><br>
✶&nbsp; <span style="color:orange;">commit 8ba9aeb3cea847b63a91ac378a2a6db758682460</span><br>
&nbsp;<span style="color:red;">|</span> &nbsp; Author: smartiqa <info@smartiqa.ru><br>
&nbsp;<span style="color:red;">|</span> &nbsp; Date:   Thu Mar 4 14:54:08 2021 +0300<br>
&nbsp;<span style="color:red;">|</span><br>
&nbsp;<span style="color:red;">|</span> &emsp;&emsp;&emsp; L-03: Circle and square added<br>
&nbsp;<span style="color:red;">|</span>

# Unit tests для функции sin

## Описание файла

В файле `sin.py` представлен набор юнит-тестов для проверки математической функции синус (`sin`) из стандартной библиотеки `math` Python. Тесты предназначены для проверки корректности работы функции `sin` для ключевых значений в пределах одного периода функции.

## Включенные тесты

В файле `sin.py` реализованы следующие тесты:

- `test_sin_zero`: Проверяет, что `sin(0)` равен `0.0`.
- `test_sin_pi_half`: Убеждается, что `sin(pi/2)` равен `1.0`.
- `test_sin_pi`: Гарантирует, что `sin(pi)` равен `0.0`.
- `test_sin_three_pi_half`: Проверяет, что `sin(3*pi/2)` равен `-1.0`.
- `test_sin_two_pi`: Подтверждает, что `sin(2*pi)` равен `0.0`.
- `test_sin_pi_divide_four`: Тестирует, что `sin(pi/4)` равен `sqrt(2)/2`.
- `test_sin_pi_divide_six`: Проверяет, что `sin(pi/6)` равен `0.5`.
- `test_sin_pi_divide_three`: Проверяет, что `sin(pi/3)` равен `sqrt(3)/2`.

Эти тесты охватывают важные углы, включая кратные `pi/6`, `pi/4`, `pi/3`, `pi/2` и `pi`. Каждый тест верифицирует результат функции `sin` по сравнению с известными значениями, используя `assertAlmostEqual` для учета особенностей арифметики с плавающей точкой.

## Запуск тестов

Для запуска тестов перейдите в директорию проекта и выполните следующую команду:

```bash
python -m unittest sin_tests.py
