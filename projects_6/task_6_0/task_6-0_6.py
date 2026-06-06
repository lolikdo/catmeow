import pandas as pd

df = pd.read_csv("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv")

with open("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/iqr_by_gender.txt", 'w', encoding='utf-8') as f:
    for gender in df['gender'].unique():
        subset = df[df['gender'] == gender]['length_cm']
        q1 = subset.quantile(0.25)
        q3 = subset.quantile(0.75)
        iqr = q3 - q1
        f.write(f"{gender}\tQ1={q1:.1f} см\tQ3={q3:.1f} см\tIQR={iqr:.1f} см\n")