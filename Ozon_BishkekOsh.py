import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = r'C:\Users\User\OneDrive\Desktop\Whole Datasets\DataSet_Ozon.csv'
SAFE_LEVEL = 50

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])

    bishkek_data = df[df['City'] == 'Bishkek']
    osh_data = df[df['City'] == 'Osh']

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(bishkek_data['Date'], bishkek_data['Ozone_ppb'],
            color='#ff4b4b', label='Bishkek', linewidth=2, marker='o', markersize=4)
    ax.plot(osh_data['Date'], osh_data['Ozone_ppb'],
            color='#00d4ff', label='Osh', linewidth=2, marker='s', markersize=4)

    ax.axhline(y=SAFE_LEVEL, color='yellow', linestyle='--', linewidth=1.5, alpha=0.8, label='WHO Threshold (50 ppb)')

    ax.fill_between(df['Date'].unique(), SAFE_LEVEL, df['Ozone_ppb'].max() + 10,
                    color='yellow', alpha=0.05)

    ax.set_title('Ozone Concentration Monitoring: Bishkek vs Osh (2026)', fontsize=16, pad=20)
    ax.set_xlabel('Observation Date', fontsize=12)
    ax.set_ylabel('Ozone Level (ppb)', fontsize=12)
    ax.set_ylim(0, max(df['Ozone_ppb'].max() + 5, SAFE_LEVEL + 10))

    ax.grid(True, linestyle='--', alpha=0.2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.gcf().autofmt_xdate()
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    plt.tight_layout()
    plt.show()
else:
    print(f"File not found: {file_path}")
