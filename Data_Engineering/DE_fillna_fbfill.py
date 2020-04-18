df.sort_values('year').groupby('Country Name')['GDP'].fillna(method='ffill').fillna(method='bfill')
