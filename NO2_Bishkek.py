import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

file_path = r'C:\Users\User\OneDrive\Desktop\no2_pollution_data_2026(1).csv'
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 7))

plt.fill_between(df['Date'], df['NO2_ppb'], color="mediumaquamarine", alpha=0.2)
sns.lineplot(data=df, x='Date', y='NO2_ppb', color="seagreen", linewidth=2.5, marker='o', markersize=7)

plt.axhspan(0, 5, color='green', alpha=0.05, label='Excellent (0-5 ppb)')
plt.axhspan(5, 10, color='orange', alpha=0.05, label='Acceptable (5-10 ppb)')

max_val = df['NO2_ppb'].max()
max_date = df.loc[df['NO2_ppb'].idxmax(), 'Date']

plt.annotate(f'Pollution Peak: {max_val} ppb',
             xy=(max_date, max_val),
             xytext=(max_date, max_val + 0.8),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
             fontsize=10, fontweight='bold', ha='center')

plt.title('Air Quality Analysis: NO2 Concentration', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Date (April 2026)', fontsize=12)
plt.ylabel('NO2 Level (ppb)', fontsize=12)

plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d %b'))
plt.xticks(df['Date'], rotation=45)

plt.legend(loc='upper left')
plt.tight_layout()

plt.show()
