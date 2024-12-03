import re
from typing import Callable

text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")

def generator_numbers(text: str):
    # Перевіряємо, чи є вхідний параметр рядком
    if not isinstance(text, str):
        raise TypeError("Вхід має бути рядком!")
    
    pattern = r"\b\d+(?:\.\d+)?\b"  # Регулярний вираз для чисел

    try:
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                yield float(match)  # Перетворюємо знайдене число в float
            except ValueError:
                print(f"Не вдалося перетворити '{match}' на число.")  # Лог помилки
    except Exception as e:
        print(f"Помилка в регулярному виразі: {e}")

def sum_profit(text: str, func: Callable):
    # Перевіряємо, чи є вхідний параметр рядком
    if not isinstance(text, str):
        raise TypeError("Вхід має бути рядком!")
    # Перевіряємо, чи func є callable
    if not callable(func):
        raise TypeError("Другий аргумент має бути callable!")
    
    try:
        return sum(func(text))  # Використовуємо передану функцію для обробки text
    except Exception as e:
        print(f"Помилка під час обчислення суми: {e}")
        return 0  # Якщо виникла помилка, повертаємо 0

# Якщо скрипт виконується безпосередньо
if __name__ == "__main__":
    try:
        total_income = sum_profit(text, generator_numbers)  # Передаємо текст і генератор
        print(f"Загальний дохід: {total_income}")
    except TypeError as e:
        print(f"Помилка: {e}")
