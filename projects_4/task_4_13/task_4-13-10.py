l = []
i = 1
sum = 0
N = int(input("введите длину вашего массива: "))
for k in range (N):
    num = int(input("введите элемент массива: "))
    l.append(num)

while i < N:
    sum = sum + l[i]
    i = i + 2

print(sum)