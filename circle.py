import math


def area(r):
    ''' Функция возвращает площадь окружности радиусом r
        Параметры:
            r (int): радиус окружности
        Возвращаемое значение:
            area(r): число, равное площади окружности с радиусом r
        Примеры вызова:
            area(3)     # 28.274333882308138 '''
    return math.pi * r * r


def perimeter(r):
    ''' Функция возвращает длину окружности окружности радиусом r
        Параметры:
            r (int): радиус окружности
        Возвращаемое значение:
            perimeter(r): число, равное длине окружности с радиусом r
        Примеры вызова:
            perimeter(4)    #25.132741228718345 '''
    return 2 * math.pi * r

