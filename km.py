import pandas as pd
df = pd.read_csv('Languages.csv')
language = set(df['ascii_name'])
lat = set(df['latitude'])
lngt = set(df['longitude'])
coordinates = dict{language}
