n = int(input("Введите количество чисел: "))
nums = []
print(f"Поочередно введите {n} чисел (-ла):")
for i in range(n):
    num = int(input())
    nums.append(num)

sr = sum(nums) / len(nums)
print(f"Среднее арифметическое = {sr}")