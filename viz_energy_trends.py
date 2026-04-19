import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
values = [25.8, 26.7, 21.2, 24.8, 27.3, 23.5, 21.0, 25.1, 23.4, 29.8, 30.2]

colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(years)))

colors[-1] = to_rgba('#1f7a1f')

fig, ax = plt.subplots(figsize=(13, 7.5))

bars = ax.bar(years, values, color=colors, width=0.75, edgecolor='white', linewidth=0.7)

ax.text(10, values[-1] + 0.8, '2020\n30%',
        ha='center', va='bottom', fontsize=13, fontweight='bold', color='#1f7a1f')

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.25,
            f'{height:.1f}%', ha='center', va='bottom', fontsize=10.5, fontweight='medium')

ax.set_title('Kyrgyzstan — Renewable Energy Consumption\n(% of Total Final Energy Consumption)',
             fontsize=16, fontweight='bold', pad=25)

ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xlabel('World Bank Data', fontsize=10, color='gray')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_alpha(0.3)
ax.spines['bottom'].set_alpha(0.3)

ax.grid(axis='y', linestyle='--', alpha=0.3, zorder=0)
ax.set_axisbelow(True)

ax.set_ylim(19, 33)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.tight_layout()
plt.show()
