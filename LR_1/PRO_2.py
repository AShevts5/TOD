summ_p = 0
summ_o = 0
while True:
    c = int(input("Введите число: "))
    if c == 0:
        break
    summ_p = summ_p + c if c > 0 else summ_o = summ_o + c
print(f"Сумма положительных чисел = {summ_p}")    
print(f"Сумма отрицательных чисел = {summ_o}")    

