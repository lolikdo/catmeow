medium_name = input("Введите название питательной среды:")
agricultural_concentration = input("Введите концетрацию агара")
sterilization_temmperature = input("Введите температуру стерилизации")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(medium_name + "\n")
    file.write(f" Концентрация агара: {agricultural_concentration}%\n")
    file.write(f" Температура стерилизации:: {sterilization_temmperature}\n")
print("\nФайл 'recipe.txt' успешно сформирован")