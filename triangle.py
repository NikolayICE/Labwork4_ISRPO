def area(a, h):
    if a < 0 or h < 0:
        raise ValueError("Base and height must be non-negative")
    return a * h / 2

def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("All sides must be non-negative")
    return a + b + c
