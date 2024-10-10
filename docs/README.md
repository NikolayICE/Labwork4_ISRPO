# Geomitric_lib
```
Эта библиотека содержит файлы с функциями, благодаря которым можно рассчитать периметры и площади геометрических фигур. Есть функции для рассчета площади и периметра для круга, прямоугольника, квадрата и треугольника
```

## 1. circle.py
- def area(r)
    - Функция возвращает площадь окружности радиусом r
        Параметры:
            r (int): радиус окружности
        Возвращаемое значение:
            area(r): число, равное площади окружности с радиусом r
        Примеры вызова:
            area(3)     # 28.274333882308138

- def perimeter(r)
    - Функция возвращает длину окружности окружности радиусом r
        Параметры:
            r (int): радиус окружности
        Возвращаемое значение:
            perimeter(r): число, равное длине окружности с радиусом r
        Примеры вызова:
            perimeter(4)    #25.132741228718345

## 2. rectangle.py
- def area(a, b)
    - Функция возвращает площадь прямоугольника со сторонами a и b
        Параметры:
            a (int): первая сторона прямоугольника
            b (int): вторая сторона прямоугольника
        Возвращаемое значение:
            area(a, b): число равное площади прямоугольника a * b 
        Примеры вызова:
            area(3, 4)      # 12
- def perimeter(a, b):
    - Функция возвращает периметр прямоугольника со сторонами a и b
        Параметры:
            a (int): первая сторона прямоугольника
            b (int): вторая сторона прямоугольника
        Возвращаемое значение:
            perimeter(a, b): число равное периметру прямоугольника 2 * (a + b) 
        Примеры вызова:
            perimeter(3, 4)      # 14

## 3. square.py
- def area(a)
    - Функция возвращает площадь квадрата со стороной a
        Параметры:
            a (int): сторона квадрата
        Возвращаемое значение:
            area(a): число равное площади квадрата a * a 
        Примеры вызова:
            area(2)     # 4
- def perimeter(a)
    - Функция возвращает периметр квадрата со стороной a
        Параметры:
            a (int): сторона квадрата
        Возвращаемое значение:
            perimeter(a): число равное периметру квадрата 4 * a 
        Примеры вызова:
            perimeter(2)     # 8

## 4. triangle.py
- def area(a, h)
    - Функция возвращает площадь треугольника со стороной a и высотой h
        Параметры:
            a (int): сторона треугольника
            h (int): высота, проведенная к этой стороне
        Возвращаемое значение:
            area(a, h): число равное площади треугольника a * h / 2 
        Примеры вызова:
            area(3, 6)      # 9
- def perimeter(a, b, c)
    - Функция возвращает периметр треугольника со сторонами a, b, c
        Параметры:
            a (int): первая сторона треугольника
            b (int): вторая сторона треугольника
            c (int): третья сторона треугольника
        Возвращаемое значение:
            perimeter(a, b, c): число равное периметру треугольника a + b + c 
        Примеры вызова:
            perimeter(1, 2, 3)      # 6


# Change history with commit hashes
``` bash
    * 94f4058 (HEAD -> new_features_466371) added description for triangle.py
    * dff37a9 added description of file functions triangle.py
    * f761a12 added description of file functions square.py
    * 3a707f9 added description of file functions rectangle.py
    * ecda505 added description of file functions circle.py
    * 63bc45d fixed the code
    * 56a6dd5 added file triangle.py
    * 483f7e0 added new file
    | * 86edb1c (origin/release) L-05: Update Docs. Add user agreement info
    | * 438b89a L-05: Add user agreement
    | * 6adb962 L-03: Docs added
    | | * 3049431 (origin/feature) L-04: Add rectangle.py
    | |/  
    |/|   
    | | * b5b0fae (origin/develop) L-04: Update docs for calculate.py
    | | * d76db2a L-04: Add calculate.py
    | | * 51c40eb L-04: Doc updated for triangle
    | | * d080c78 L-04: Triangle added
    | |/  
    |/|   
    * | d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
    |/  
    * 8ba9aeb L-03: Circle and square added
```
