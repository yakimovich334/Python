def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_between(a, b):
    if a > b:
        a, b = b, a
    return [num for num in range(a, b + 1) if is_prime(num)]

def fib(k, a=0, b=1, result=None):
    if result is None:
        result = []
    if k == 0:
        return result
    result.append(a)
    return fib(k - 1, b, a + b, result)

# Основна програма
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

# Вивід простих чисел між a і b
print(f"Прості числа між {a} і {b}: {primes_between(a, b)}")

# Вивід чисел Фібоначчі
k = int(input("Введіть кількість чисел Фібоначчі: "))
print(f"Перші {k} чисел Фібоначчі: {fib(k)}")

