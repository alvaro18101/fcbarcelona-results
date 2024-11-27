import pandas as pd
df = pd.read_csv('processed_matches.csv')

a = df[(df['Locality'] == 'local') & (df['Status'] == 'Win')]
print(a)
numero = 3.141592

print(f'{"%.2f" % numero}')