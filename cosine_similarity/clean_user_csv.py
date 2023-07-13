import pandas as pd

df = pd.read_csv('users.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('output_users.csv', index=False)

df = pd.read_csv('users_part2.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('output_users2.csv', index=False)

df.drop_duplicates()
