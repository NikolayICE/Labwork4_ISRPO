def area(a, h):
    ''' Функция возвращает площадь треугольника со стороной a и высотой h
        Параметры:
            a (int): сторона треугольника
            h (int): высота, проведенная к этой стороне
        Возвращаемое значение:
            area(a, h): число равное площади треугольника a * h / 2 
        Примеры вызова:
            area(3, 6)      # 9'''
    return a * h / 2

def perimeter(a, b, c):
    ''' Функция возвращает периметр треугольника со сторонами a, b, c
        Параметры:
            a (int): первая сторона треугольника
            b (int): вторая сторона треугольника
            c (int): третья сторона треугольника
        Возвращаемое значение:
            perimeter(a, b, c): число равное периметру треугольника a + b + c 
        Примеры вызова:
            perimeter(1, 2, 3)      # 6'''
    return a + b + c