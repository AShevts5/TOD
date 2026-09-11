days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
m = int(input("Введите номер месяца: "))
if m not in months:
    print("Ну обшииибся")
else:
    for i in range(len(days)+1): 
        if m == i+1:
            print(days[i])
    