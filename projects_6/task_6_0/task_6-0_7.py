import pandas as pd

df = pd.read_csv("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/wild_boars.csv")

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

with open("C:/Users/Asus/OneDrive/Документы/maiorova_us/projects_6/task_6_0/variation_stats.txt", 'w', encoding='utf-8') as f:
    for col in numeric_cols:
        var = df[col].var()
        std = df[col].std()
        mean_val = df[col].mean()
        cv = (std / mean_val) * 100 if mean_val != 0 else float('nan')
        
        f.write(f"{col}\n")
        f.write(f"  Дисперсия:\t{var:.2f}\n")
        f.write(f"  Стандартное отклонение:\t{std:.2f}\n")
        f.write(f"  Коэффициент вариации:\t{cv:.2f}%\n\n")