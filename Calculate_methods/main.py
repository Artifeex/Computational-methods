import math


def SympsonMethod(points):
    countSegments = len(points) - 1
    a = points[0][0]
    b = points[len(points) - 1][0]
    h = b - a / countSegments
    result = points[0][1] + points[len(points) - 1][1]
    for i in range(1, countSegments):
        # если четный, то * 2
        if i % 2 == 0:
            result += 2 * points[i][1]
        # нечетный
        else:
            result += 4 * points[i][1]
    result *= h/3
    return result


def ThreeEighthsMethod(points):
    countSegments = len(points) - 1
    a = points[0][0]
    b = points[len(points) - 1][0]
    h = b - a / countSegments
    result = points[0][1] + points[len(points) - 1][1]
    for i in range(1, countSegments):
        if i % 3 == 0:
            result += 2 * points[i][1]
        else:
            result += 3 * points[i][1]
    result *= 3*h / 8
    return result


def FivePointsMethod(points):
    countSegments = len(points) - 1
    a = points[0][0]
    b = points[len(points) - 1][0]
    h = b - a / countSegments
    result = 7 * points[0][1] + 7 * points[len(points) - 1][1]
    for i in range(1, countSegments):
        if i % 4 == 0:
            result += 14 * points[len(points) - 1][1]
        elif i % 4 == 2:
            result += 12 * points[len(points) - 1][1]
        else:
            result += 32 * points[len(points) - 1][1]
    result *= 2 * h / 45
    return result


def GetPoints(function, a, b, step):
    points = []
    while a <= b:
        x = a
        y = function(x)
        points.append((x, y))
        a += step
    return points


def Function1(x):
    return 3 * x**3 - 2 * x**2 + 7


def Function2(x):
    return math.sin(x) + 1 / math.cos(x)


def Function3(x):
    return math.exp(1 / x) / x ** 2


