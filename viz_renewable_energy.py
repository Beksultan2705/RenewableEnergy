import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/diushaliev_beksultan/Desktop/7-2-1-1.csv'

try:
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    share_df = df[df['SERIES'].str.contains('Доля', case=False, na=False)]
    hydro_df = df[df['SERIES'].str.contains('Производство', case=False, na=False)]

    plt.figure(figsize=(10, 6))
    plt.plot(share_df['Year'], share_df['Value'], marker='o', linestyle='-', color='#2ca02c', linewidth=2, label='Доля ВИЭ (%)')

    plt.title('Динамика доли возобновляемой энергии в КР (2007-2024)', fontsize=14, pad=15)
    plt.xlabel('Год', fontsize=12)
    plt.ylabel('Процент (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Ошибка: Файл не найден по пути {file_path}. Проверьте правильность написания.")
