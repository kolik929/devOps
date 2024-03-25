print("Вас привет система сложения чисел")
bad_data = True
while bad_data:
    try:
        a = int(input("Введите a:"))
        b = int(input("Введите b:"))
        bad_data = False
    except ValueError:
        print("Не пиши фигню.")
    except:
        print("Чет фигня какая-то")
print(f'Сумма {a} и {b}  равна {a + b}')
