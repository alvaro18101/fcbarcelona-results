import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('processed_matches.csv')

fig, ax = plt.subplots()
X = ['Victories', 'Defeats', 'Ties']
status = list(df['Status'])
counts = [status.count('Win'), status.count('Lose'), status.count('Draw')]
bar_labels = ['Victories', 'Defeats', 'Ties']
bar_colors = ['tab:green', 'tab:red', 'tab:blue']
ax.bar(X, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('Number of matches')
ax.set_title('Stats of victories')
ax.legend(title='Status')
plt.show()

fig, ax = plt.subplots()
ax.pie(counts, labels=bar_labels, autopct='%1.1f%%', colors=bar_colors)
plt.show()

X = range(1, len(df['CGD']) + 1)
plt.plot(X, df['CGD'], '.--')
plt.xlabel('Matches played')
plt.ylabel('Goals in favor')
plt.title('Cumulative Goal Difference')
plt.grid()
plt.show()


# data from https://allisonhorst.github.io/palmerpenguins/


species = ("Local", "Visiting")
penguin_means = {
    'Victories': (len(df[(df['Locality'] == 'local') & (df['Status'] == 'Win')]), len(df[(df['Locality'] == 'visiting') & (df['Status'] == 'Win')])),
    'Defeats': (len(df[(df['Locality'] == 'local') & (df['Status'] == 'Lose')]), len(df[(df['Locality'] == 'visiting') & (df['Status'] == 'Lose')])),
    'Tiers': (len(df[(df['Locality'] == 'local') & (df['Status'] == 'Draw')]), len(df[(df['Locality'] == 'visiting') & (df['Status'] == 'Draw')])),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, len(df))

plt.show()