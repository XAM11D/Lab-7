# Lab-7
Лабораторна робота №X: Обробка даних у Python з обробкою помилок

Мета роботи
Мета цієї лабораторної роботи - навчитися працювати з обробкою даних у Python, а також ознайомитися з механізмами обробки винятків для забезпечення коректної роботи програм. Очікувані результати включають написання та тестування функцій з обробкою числових даних, рядків та списків, а також реалізацію обробки можливих помилок.

Опис завдання
Завдання 1: Перетворення віку на ціле число.
Завдання 2: Множення двох чисел.
Завдання 3: Повернення довжини рядка.
Завдання 4: Повернення суми елементів списку.
Завдання 5: Обчислення середнього бала для кожного студента зі списку.

Виконання роботи
Завдання 1:
def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Error: Please enter a valid numeric value for age."

# Приклад використання:
print(task1("25"))  # Виведе: 25
print(task1("twenty"))  # Виведе: Error: Please enter a valid numeric value for age.

Завдання 2:
def task2(num1, num2):
    try:
        return num1 * num2
    except TypeError:
        return "Error: Please enter valid numeric values for numbers."

# Приклад використання:
print(task2(3, 4))  # Виведе: 12
print(task2(3, "four"))  # Виведе: Error: Please enter valid numeric values for numbers.

Завдання 3:
def task3(input_str):
    try:
        if isinstance(input_str, str):
            return len(input_str)
        else:
            raise TypeError
    except TypeError:
        return "Error: Please enter a string, not a numeric value."

# Приклад використання:
print(task3("Hello"))  # Виведе: 5
print(task3(1234))  # Виведе: Error: Please enter a string, not a numeric value.

Завдання 4:
def task4(int_list):
    try:
        total = sum(int_list)
        return total
    except TypeError:
        return None

# Приклад використання:
print(task4([1, 2, 3, 4, 5]))  # Виведе: 15
print(task4([1, 2, "three", 4, 5]))  # Виведе: None

Завдання 5:
def calculate_average(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return 0

def task5(data):
    try:
        result = []
        for item in data:
            name, grades = item[0], item[1]
            avg_grade = calculate_average(grades)
            result.append((avg_grade, name))
        return result
    except Exception:
        return "List processing error!"

# Приклад використання:
data = [('John', (2, 2, 3)), ('Jane', (4, 3, 5)), ('Jack', (5, 4, 4))]
print(task5(data))  # Виведе: [(2.3333333333333335, 'John'), (4.0, 'Jane'), (4.333333333333333, 'Jack')]

Приклади виводу програми:
Завдання 1: 25, Error: Please enter a valid numeric value for age.
Завдання 2: 12, Error: Please enter valid numeric values for numbers.
Завдання 3: 5, Error: Please enter a string, not a numeric value.
Завдання 4: 15, None
Завдання 5: [(2.33, 'John'), (4.0, 'Jane'), (4.33, 'Jack')]


Вимоги до середовища:Python 3.x
