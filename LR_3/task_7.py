s = input("Введите строку текста на русском языке: ")

# проверка, есть ли данные буквы в тексе
def has_letter(text, letter):
    has_l = letter in text.lower()
    return has_l

# подсчет количества каждой буквы
def cnt(text, letter):
    cnt_letter = len([x for x in text.lower() if x == letter])
    return cnt_letter

if not (has_letter(s,'и')) and not (has_letter(s,'т')):
    print('таких букв нет')
else:
    print(f'Буква "И" в тексте встречается {cnt(s, "и")} раз. Буква "Т" в тексте встречается {cnt(s, "т")} раз.')


# а в конце я вспомнила про существование функции count(), ну да ладно, так интереснее :)
