import math


def area(r):
    """
    Возвращает плоащадь круга

            Параметры:
                    r (float): радиус круга

            Возвращаемое значение:
                    math.pi * r * r (float): площадь круга
    """
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает периметр круга

            Параметры:
                    r (float): радиус круга

            Возвращаемое значение:
                    2 * math.pi * r (float): периметр круга
    """
    return 2 * math.pi * r
