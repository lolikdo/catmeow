import pandas as pd

df = pd.read_csv("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv")

means = df.mean(numeric_only=True)

with open("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/means.txt", 'w', encoding='utf-8') as f:
    for col in means.index:
        f.write(f"{col}\t{means[col]:.2f}\n")
