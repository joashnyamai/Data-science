import matplotlib.pyplot as plt
import numpy as np

months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social_media = [70, 80, 90, 87, 92]

x = np.arange(len(months))
width = 0.25

plt.figure(figsize=(10, 6))
plt.bar(x - width, searches, width=width, label='Searches', color='dodgerblue')
plt.bar(x, direct, width=width, label='Direct', color='palevioletred')
plt.bar(x + width, social_media, width=width, label='Social Media', color='orange')

plt.xlabel('Months')
plt.ylabel('Visitors (in thousands)')
plt.title('Visitors by Web Traffic Sources')
plt.xticks(x, months)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("traffic_sources_plot.png")
plt.show()
