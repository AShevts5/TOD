from random import *
a = randint(1, 100)
while True:
    user = int(input("Угадайте число (диапазон от 1 до 100): "))
    if user == a:
        print("Угадал, умочка")
        break
    else:
        print("Бро, ну шо за беспредел")
        if user > a:
            print("Твое число больше")
        else:
            print("Твоё число меньше")
        cont = input(("Хочешь продолжить угадывать? Yes/exit: "))
        if cont == "exit":
            break
        else:
            continue
    
            
 