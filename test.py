import pandas as pd
df = pd.read_csv('processed_matches.csv')

a = df[(df['Locality'] == 'local') & (df['Status'] == 'Win')]
print(a)