seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]
for sequence in seq:
    print(f"Последовательность целиком: {sequence}")
    print("Построчно:")
    for nucleotide in sequence:
        print(nucleotide)
print('Цикл выполнен')