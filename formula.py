# import pandas as pd
# df = pd.read_csv('Languages.csv')
# language = set(df['ascii_name'])
# lat = set(df['latitude'])
# lngt = set(df['longitude'])
# coordinates = dict{language}

x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
km = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)
print(km)
