l = []
i = 0
count = 0
N = int(input("введите длину вашего массива: "))
for k in range (N):
    num = int(input("введите элемент массива: "))
    l.append(num)

while i < N:
    if l[i] > 0:
        count = count + 1
    i += 1

print(count)