import pandas as pd

df = pd.read_csv('manga_df.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('output_manga.csv', index=False)

df = pd.read_csv('manga_df2.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('output_manga2.csv', index=False)

df = pd.read_csv('manga_df3.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('output_manga23.csv', index=False)

df.drop_duplicates()
