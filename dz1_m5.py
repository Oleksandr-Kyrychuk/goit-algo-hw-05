def caching_fibonacci():
    cache = {}  # Ініціалізація порожнього словника для кешування

    def fibonacci(n):  # Внутрішня функція для обчислення чисел Фібоначчі
        try:
            if not isinstance(n, int):  # Перевірка, чи є аргумент цілим числом
                raise TypeError("Аргумент має бути цілим числом.")
            if n < 0:  # Перевірка на від'ємне значення
                raise ValueError("Число Фібоначчі не може бути від'ємним.")
            
            if n == 0:  # Базовий випадок: якщо n == 0, повертаємо 0
                return 0
            elif n == 1:  # Базовий випадок: якщо n == 1, повертаємо 1
                return 1
            elif n in cache:  # Перевіряємо, чи є значення вже в кеші
                return cache[n]
            
            # Якщо значення немає в кеші, обчислюємо та зберігаємо його
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        except TypeError as e:
            print(f"Помилка типу: {e}")
            return None
        except ValueError as e:
            print(f"Помилка значення: {e}")
            return None
        except Exception as e:
            print(f"Невідома помилка: {e}")
            return None
    
    return fibonacci  # Повертаємо тільки внутрішню функцію

# Якщо скрипт виконується безпосередньо
if __name__ == "__main__":
    fib = caching_fibonacci()  # Отримуємо внутрішню функцію
    print(fib(10))  # Обчислюємо 10-те число Фібоначчі

    # Тестування помилок
    print(fib(-5))  # Тестуємо від'ємне число
    print(fib("a"))  # Тестуємо неправильний тип аргументу
