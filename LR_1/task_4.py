hours = int(input("Введите количество часов: "))
money = int(input("Введите заработок в час: "))
salary = hours * money
salary = salary * 1.5 if hours > 40 else salary
print(f"Зарплата в день = {salary}")
