#import math

from math import sqrt as kvkoren
print("Вас привет система решения квадратных уравнений")
bad_data = True
while bad_data:
    try:
        a = int(input("Введите a:"))
        b = int(input("Введите b:"))
        c = int(input("Введите c:"))
        bad_data = False
    except ValueError:
        print("Не пиши фигню.")
    except ZeroDivisionError:
        print("Убери нули")
    except:
        print("Чет фигня какая-то")
D = b * b - (4 * a * c)
print(f'Дискриминант равен: {D}')
if D > 0:
    print('2 корня')
    d = kvkoren(D)
    X1 = ((-b) + d) / (2 * a)
    X2 = ((-b) - d) / (2 * a)
    print(f'Первый корень уравнения равен {X1} второй корень равен {X2}')
elif D == 0:
    print("один корень")
    X1 = (-(b)) / (2 * a)
    print("Корень уравнения равен {}".format(X1))
else:
    print("Уравнение не имеет корней")
