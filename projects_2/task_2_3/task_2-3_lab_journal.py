researcher = input("Введите ФИО исследователя: ")
date = input("Введите дату проведения эксперимента: ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод по эксперименту: ")
HORIZONTAL = '-'
VERTICAL = '|'
CORNER = '+'
WIDTH = 50
with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write(f"{CORNER}{HORIZONTAL * WIDTH}{CORNER}\n")
    file.write(f"{VERTICAL} Электронный лабораторный журнал{' ' * (WIDTH - len(' Электронный лабораторный журнал') - 1)}{VERTICAL}\n")
    file.write(f"{CORNER}{HORIZONTAL * WIDTH}{CORNER}\n")
    file.write(f"{VERTICAL} ФИО исследователя : {researcher:<{WIDTH - len(' ФИО исследователя : ') - 1}}{VERTICAL}\n")
    file.write(f"{VERTICAL} Дата             : {date:<{WIDTH - len(' Дата             : ') - 1}}{VERTICAL}\n")
    file.write(f"{VERTICAL} Эксперимент      : {experiment_name:<{WIDTH - len(' Эксперимент      : ') - 1}}{VERTICAL}\n")
    file.write(f"{CORNER}{HORIZONTAL * WIDTH}{CORNER}\n")
    file.write(f"{VERTICAL} Вывод:{' ' * (WIDTH - len(' Вывод:') - 1)}{VERTICAL}\n")
    max_text_width = WIDTH - 4  
    words = conclusion.split()
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_text_width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            file.write(f"{VERTICAL} {current_line:<{max_text_width}} {VERTICAL}\n")
            current_line = word

    if current_line:
        file.write(f"{VERTICAL} {current_line:<{max_text_width}} {VERTICAL}\n")
    
    file.write(f"{CORNER}{HORIZONTAL * WIDTH}{CORNER}\n")

print("\nДанные успешно сохранены в journal.txt")