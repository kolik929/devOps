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
