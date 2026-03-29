l = []
i = 0
sum = 0
N = int(input("введите длину вашего массива: "))
for k in range (N):
    num = int(input("введите элемент массива: "))
    l.append(num)

while i < N:
    if l[i] % 2 != 0:
        sum = sum + l[i]
    i += 1

print(sum)