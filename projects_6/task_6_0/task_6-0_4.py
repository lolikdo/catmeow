import pandas as pd

df = pd.read_csv("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv")

with open("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/modes.txt", 'w', encoding='utf-8') as f:
    for col in df.columns:
        mode_vals = df[col].mode()
        mode_val = mode_vals.iloc[0]
        f.write(f"{col}\t{mode_val}\n")
