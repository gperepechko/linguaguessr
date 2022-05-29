import json
import pandas as pd

df = pd.DataFrame(columns=['ascii_name','latitude','longitude'])
with open('sample100.json') as file:
    data = json.load(file)
features = data['features']
for feature in features:
    language = feature['properties']['language']
    ascii_name = language['ascii_name']
    latitude = language['latitude']
    longitude = language['longitude']
    df = df.append({'ascii_name':ascii_name,'latitude':latitude,'longitude':longitude}, ignore_index=True)
print(df)
df.to_csv('sample100.csv')
