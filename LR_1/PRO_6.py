from math import sqrt

print("Последовательно введите значения коэффициентов a, b, c:")
a, b, c = int(input()), int(input()), int(input())
D = b**2 - 4*a*c
if D < 0:
    print("Корней нет")
elif D == 0:
    x = -b / 2*a
    print(f"x = {x}")
else:
    x1 = (-b + sqrt(D)) / (2*a)
    x2 = (-b + sqrt(D)) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")