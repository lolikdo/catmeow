pH = float(input("Введите значение pH"))
if pH < 0 or pH > 14:
    print("Некорректное значение pH. Допустимый диапазон: 0-14.")
elif pH < 7:
    print("Кислая среда")
elif pH == 7:
    print("Нейтральная среда")
else:
    print("Щелочная среда")
