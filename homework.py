from typing import Callable

def caching_fibonacci():
    cache= dict() #Створюємо порожній словник cache

    def fibonacci(n):
        #Перевіряємо, чи немає значення n у cache
        if n <= 0:
            return 0 
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        #Виконуємо рекурсивне обчислення
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

def generator_numbers(text: str):
    text_list = text.split(' ')
    new_list = list()
    for el in text_list:
        try:
            new_list.append(str(float(el)))
        except ValueError:
            continue
    yield ' '.join(new_list)




def sum_profit(text: str, func: Callable):
    new_text = str(next(func(text)))
    new_list = new_text.split(" ")
    summ = 0
    for el in new_list:
        summ += float(el)
    return summ

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



    






