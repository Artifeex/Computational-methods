import math
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def SympsonMethod(points):
    countSegments = len(points) - 1
    a = points[0][0]
    b = points[len(points) - 1][0]
    h = (b - a) / countSegments
    result = points[0][1] + points[len(points) - 1][1]
    for i in range(1, countSegments):
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
    h = (b - a) / countSegments
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
    h = (b - a) / countSegments
    result = 7 * points[0][1] + 7 * points[len(points) - 1][1]
    for i in range(1, countSegments):
        if i % 4 == 0:
            result += 14 * points[i][1]
        elif i % 4 == 2:
            result += 12 * points[i][1]
        else:
            result += 32 * points[i][1]
    result *= 2 * h / 45
    return result


def GetPoints(a, b, n, function):
    h = (b - a) / n
    points = []
    for i in range(n+1):
        points.append((a + (i * h), function(a + (i * h))))
    return points


def Function1(x):
    return 3 * x**3 - 2 * x**2 + 7


def Function2(x):
    return math.sin(x) + 1 / math.cos(x)


def Function4(x):
    return math.sin(x) ** 2


def Function3(x):
    return math.exp(1 / x) / x ** 2


def PrintMenu():
    print("1) 3 * x^3 - 2 * x^2 + 7 [-3, 3]")
    print("2) sin(x) + 1 / cos(x), [-pi/4, pi/4]")
    print("3) e^(1/x) / x^2, [1, 3]")
    print("4) sin^2(x) , [pi/3, 2pi/3]")
    print("9) Очистить экран")
    print("0) Выход")


def main():
    countIterations = 6
    exit = False
    while not exit:
        PrintMenu()
        choice = int(input("Выберите функцию: "))
        if choice == 1:
            reference = 6
            a = -3
            b = 3
            print("3 * x^3 - 2 * x^2 + 7 [-3, 3]]")
            print("Истинное значение = {0}".format(reference))
            for k in range(1, countIterations):
                countVerticies = 12 * k + 1
                countSegments = countVerticies - 1
                points1 = GetPoints(a, b, countSegments, Function1)
                result = SympsonMethod(points1)
                print("countSegments = " + str(countSegments))
                print("--------------------------------------------")
                print("Метод Симпсона: {0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = ThreeEighthsMethod(points1)
                print("Метод 3/8:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = FivePointsMethod(points1)
                print("Метод пятиточия:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                print()
        elif choice == 2:
            reference = 1.762747174039086
            a = -math.pi / 4
            b = math.pi / 4
            print("Выбрана функция: sin(x) + 1 / cos(x) , [-pi/4, pi/4]")
            print("Истинное значение = {0}".format(reference))
            for k in range(1, countIterations):
                countVerticies = 12 * k + 1
                countSegments = countVerticies - 1
                points1 = GetPoints(a, b, countSegments, Function2)
                result = SympsonMethod(points1)
                print("countSegments = " + str(countSegments))
                print("--------------------------------------------")
                print("Метод Симпсона: {0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = ThreeEighthsMethod(points1)
                print("Метод 3/8:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = FivePointsMethod(points1)
                print("Метод пятиточия:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                print()
        elif choice == 3:
            reference = 1.322669403372956
            a = 1
            b = 3
            print("Выбрана функция: e^(1/x) / x^2, [1, 3]")
            print("Истинное значение = {0}".format(reference))
            for k in range(1, countIterations):
                countVerticies = 12 * k + 1
                countSegments = countVerticies - 1
                points1 = GetPoints(a, b, countSegments, Function3)
                result = SympsonMethod(points1)
                print("countSegments = " + str(countSegments))
                print("--------------------------------------------")
                print("Метод Симпсона: {0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = ThreeEighthsMethod(points1)
                print("Метод 3/8:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = FivePointsMethod(points1)
                print("Метод пятиточия:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                print()
        elif choice == 4:
            reference = 0.9566114774905182
            a = math.pi / 3
            b = 2 * math.pi / 3
            print("Выбрана функция sin^2(x) , [pi/3, 2pi/3]")
            print("Истинное значение = {0}".format(reference))
            for k in range(1, countIterations):
                countVerticies = 12 * k + 1
                countSegments = countVerticies - 1
                points1 = GetPoints(a, b, countSegments, Function4)
                result = SympsonMethod(points1)
                print("countSegments = " + str(countSegments))
                print("--------------------------------------------")
                print("Метод Симпсона: {0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = ThreeEighthsMethod(points1)
                print("Метод 3/8:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                result = FivePointsMethod(points1)
                print("Метод пятиточия:{0}".format(result))
                print("Ошибка: {0}".format(abs(result - reference)))
                print("--------------------------------------------")
                print()
        elif choice == 9:
            cls()
        elif choice == 0:
            exit = True
        print()
        print()


if __name__ == "__main__":
    main()

