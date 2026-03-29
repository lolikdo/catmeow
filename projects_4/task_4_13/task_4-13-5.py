N = int(input("введите, из скольки чисел хотите ввести наибольшее: "))
i = 1
max = 0

while i <= N:
    num = int(input("введите число: "))
    if num > max:
        max = num
    i += 1

print(max)