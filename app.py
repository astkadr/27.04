def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return "Ошибка"
    return a / b

if __name__ == "__main__":
    print("1. Сложение, 2. Вычитание, 3. Умножение, 4. Деление")
    choice = input("Выбери номер операции: ")
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))

    if choice == '1': print("Результат:", add(num1, num2))
    elif choice == '2': print("Результат:", subtract(num1, num2))
    elif choice == '3': print("Результат:", multiply(num1, num2))
    elif choice == '4': print("Результат:", divide(num1, num2))