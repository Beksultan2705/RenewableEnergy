import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path_bishkek = '/Users/diushaliev_beksultan/Desktop/DataSet_AirQuallityBishkek.csv'
path_osh = '/Users/diushaliev_beksultan/Desktop/DataSet_AirQuallityOsh.csv'

df_bishkek = pd.read_csv(path_bishkek)
df_osh = pd.read_csv(path_osh)

df_bishkek['City'] = 'Bishkek'
df_osh['City'] = 'Osh'

df_total = pd.concat([df_bishkek, df_osh])

df_total['Date'] = pd.to_datetime(df_total['Year'].astype(str) + '-' + df_total['Month'], format='%Y-%b')
df_total = df_total.sort_values('Date')

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_total, x='Date', y='AQI', hue='City', marker='o', linewidth=2)

plt.axhline(y=50, color='green', linestyle='--', alpha=0.5, label='Good (0-50)')
plt.axhline(y=100, color='orange', linestyle='--', alpha=0.5, label='Moderate (51-100)')
plt.axhline(y=150, color='red', linestyle='--', alpha=0.5, label='Unhealthy (101-150)')

plt.title('Сравнение качества воздуха (AQI): Бишкек vs Ош', fontsize=15)
plt.ylabel('Индекс AQI')
plt.xlabel('Дата')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

pivot_bishkek = df_bishkek.pivot(index="Month", columns="Year", values="AQI")

months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
pivot_bishkek = pivot_bishkek.reindex(months_order)

plt.figure(figsize=(10, 8))
sns.heatmap(pivot_bishkek, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={'label': 'AQI Index'})
plt.title('Сезонность загрязнения в Бишкеке (Heatmap)', fontsize=14)
plt.show()
