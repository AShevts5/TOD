days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')

def infa(i):
    c = 'выходной' if i >= 5 else 'рабочий день'
    print(f"{i+1}-й день недели - {days[i]}, {c}")

result = list(map(infa, range(len(days))))
print(result)



            