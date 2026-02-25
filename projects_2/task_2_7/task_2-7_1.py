files = ["seq1", "seq2", "seq3", "seq4"]
data = ('_23.01.2026')
for name in files:
    new_name = name + ".fasta" + data
    print(f"{new_name}")