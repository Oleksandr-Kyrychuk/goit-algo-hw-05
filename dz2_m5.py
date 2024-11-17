import re

text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")

def generator_numbers(text: str):
    # Перевіряємо, чи є вхідний параметр рядком
    if not isinstance(text, str):
        raise TypeError("Вхід має бути рядком!")
    
    pattern = r"\b\d+(?:\.\d+)?\b"  # Використовуємо регулярний вираз для чисел

    try:
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                yield float(match)  # Перетворюємо знайдене число в float
            except ValueError:
                print(f"Не вдалося перетворити '{match}' на число.")  # Лог помилки
    except Exception as e:
        print(f"Помилка в регулярному виразі: {e}")

def sum_profit(text: str):
    # Перевіряємо, чи є вхідний параметр рядком
    if not isinstance(text, str):
        raise TypeError("Вхід має бути рядком!")
    
    try:
        return sum(generator_numbers(text))
    except Exception as e:
        print(f"Помилка під час обчислення суми: {e}")
        return 0  # Якщо виникла помилка, повертаємо 0 як значення
 # Якщо скрипт виконується безпосередньо, а не імпортується як модуль
if __name__ == "__main__":
# Використання
    try:
     total_income = sum_profit(text)
     print(f"Загальний дохід: {total_income}")
    except TypeError as e:
     print(f"Помилка: {e}")
