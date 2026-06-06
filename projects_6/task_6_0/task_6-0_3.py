import pandas as pd

df = pd.read_csv("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv")

medians = df.median(numeric_only=True)

with open("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/medians.txt", 'w', encoding='utf-8') as f:
    for col in medians.index:
        f.write(f"{col}\t{medians[col]:.2f}\n")
