import pandas as pd
df = pd.read_csv('C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv')
print("tusk_length_cm:")
print(df['tusk_length_cm'])
min_kleuk = df['tusk_length_cm'].min()
max_kleuk = df['tusk_length_cm'].max()
print(f"\nCамые короткие клыки: {min_kleuk} см")
print(f"Cамые длинные клыки: {max_kleuk} см")
