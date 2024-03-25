# Система математических вычислений.
состоит из **двух** компонентов
1. Решение квадратных уровнений
2. Сложение

Запуск прилождений
`python3 kvur.py`

Пример кода 
```python3
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
```
