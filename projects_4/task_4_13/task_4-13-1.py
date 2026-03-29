X = int(input("введите X:"))
Y = int(input("введите Y:"))
Z = int(input("введите Z:"))
W = int(input("введите W:"))
min = X

if min > Y:
    min = Y
elif min > Z:
    min = Z
elif min > W:
    min = W

print (min)