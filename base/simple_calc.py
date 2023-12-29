def main():
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите арифметический знак (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Ошибка: нельзя делить на ноль.")
                return
            result = num1 / num2
        else:
            print("Ошибка: неверный арифметический знак, допускается + - * /.")
            return

        print(f"Результат: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Ошибка: некорректный ввод.")

if __name__ == "__main__":
    main()
