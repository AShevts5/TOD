from functools import lru_cache

num = int(input("Введите число, факториал которого нужно расчитать: "))

@lru_cache(maxsize = None)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"{num}! = {factorial(num)}")