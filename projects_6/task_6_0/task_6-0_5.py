import pandas as pd

df = pd.read_csv("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv")

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
percentiles = [0.25, 0.50, 0.75, 0.90, 0.95, 1.00]
names = ['25', '50', '75', '90', '95', 'Max']

with open("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/percentiles.txt", 'w', encoding='utf-8') as f:
    for col in numeric_cols:
        f.write(f"\n{col}:\n")
        for p, name in zip(percentiles, names):
            val = df[col].quantile(p)
            f.write(f"  Перцентиль {name}:\t{val:.1f}\n")
