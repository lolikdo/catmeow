N = int(input("введите число, чей факториал вы хотите найти: "))
factorial = 1
i = 2

while i <= N:
    factorial = factorial * i
    i += 1
print(factorial)