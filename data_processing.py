import pandas as pd
import numpy as np

df = pd.read_csv('matches.csv')

main_team = 'FC Barcelona'

df['Locality'] = ['local' if i == main_team else 'visiting' for i in df['Local Team']]


df['Local Result'] = df['Result'].str.split('-').apply(lambda string: int(string[0]))
df['Visiting Result'] = df['Result'].str.split('-').apply(lambda string: int(string[1]))

status = []
for i in range(len(df)):
    conditions = [
        df['Local Result'][i] > df['Visiting Result'][i] and df['Locality'][i] == 'local',
        df['Local Result'][i] > df['Visiting Result'][i] and df['Locality'][i] == 'visiting',
        df['Local Result'][i] < df['Visiting Result'][i] and df['Locality'][i] == 'local',
        df['Local Result'][i] < df['Visiting Result'][i] and df['Locality'][i] == 'visiting',
    ]
    choices = ['Win', 'Lose', 'Lose', 'Win']

    status.append(np.select(conditions, choices, default = 'Draw'))

df['Status'] = status

goal_difference = []
for i in range(len(df)):
    goal_diff = abs(df['Local Result'][i] - df['Visiting Result'][i])
    if df['Status'][i] == 'Lose':
        goal_diff = -goal_diff
    goal_difference.append(goal_diff)

df['Goal Difference'] = goal_difference


cumulative_goal_difference = []
accumulated = 0
for i in df['Goal Difference']:
    accumulated += i
    cumulative_goal_difference.append(accumulated)

df['CGD'] = cumulative_goal_difference


df.to_csv('processed_matches.csv', index = False)