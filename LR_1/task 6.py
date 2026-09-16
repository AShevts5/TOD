days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [i for i in range (1, 13)]
m = int(input("Введите номер месяца: "))
if m not in months:
    print("Ну обшииибся")
else:
    for i in range(len(days)): 
        if m == i+1:
            print(f"Количество дней = {days[i]}")
    