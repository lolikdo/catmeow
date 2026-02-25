reagent_name = input("Введите название нового реактива:")
reagent_quatity = int(input("Введите количество реактива (целое число):"))
report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report)
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report)
