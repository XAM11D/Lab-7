def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Error: Please enter a valid numeric value for age."
def task2(num1, num2):
    try:
        return num1 * num2
    except TypeError:
        return "Error: Please enter valid numeric values for numbers."
def task3(input_str):
    try:
        if isinstance(input_str, str):
            return len(input_str)
        else:
            raise TypeError
    except TypeError:
        return "Error: Please enter a string, not a numeric value."
def task4(int_list):
    try:
        total = sum(int_list)
        return total
    except TypeError:
        return None
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
data = [('John', (2, 2, 3)), ('Jane', (4, 3, 5)), ('Jack', (5, 4, 4))]
print(task5(data))  
