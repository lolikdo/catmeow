import pandas as pd

df = pd.read_csv("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv")

with open("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/cv_tusk_by_gender.txt", 'w', encoding='utf-8') as f:
    for gender in df['gender'].unique():
        subset = df[df['gender'] == gender]['tusk_length_cm']
        mean_val = subset.mean()
        std_val = subset.std()
        cv = (std_val / mean_val) * 100 if mean_val != 0 else float('nan')
        
        f.write(f"{gender}\tСр. длина клыков={mean_val:.2f} см\tCV={cv:.2f}%\n")