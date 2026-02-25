donor = input("Введите группу крови донора (O, A, B, AB): ").strip().upper()
patient = input("Введите группу крови пациента (O, A, B, AB): ").strip().upper()
print("\n--- РЕЗУЛЬТАТ ---")
if donor == "O" or donor == patient:
    print(f"Переливание крови группы {donor} пациенту с группой {patient} ВОЗМОЖНО")
elif donor == "A" and patient == "AB":
    print(f"Переливание крови группы A пациенту с группой AB ВОЗМОЖНО")
elif donor == "B" and patient == "AB":
    print(f"Переливание крови группы B пациенту с группой AB ВОЗМОЖНО")
else:
    print(f"Переливание крови группы {donor} пациенту с группой {patient} НЕВОЗМОЖНО")
    