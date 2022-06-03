sample100 = pd.read_csv('sample100.csv')
lat_max = sample100["latitude"].max()
lat_min = sample100["latitude"].min()
long_max = sample100["longitude"].max()
long_min = sample100["longitude"].min()

def distance(x1, x2, y1, y2):
    x_dist = abs(x1 - x2)
    if x_dist > 180:
        x_dist = 360 - x_dist
    y_dist = abs(y1 - y2)
    if y_dist > 180:
        y_dist = 360 - y_dist
    deg = (x_dist ** 2 + y_dist ** 2) ** (0.5)
    return deg

max_dist = distance(lat_max, lat_min, long_max, long_min)
segment = max_dist / 6
dist = {segment: "Very Hot", (segment*2): "Hot", (segment*3): "Warm", (segment*4): "Cool", (segment*5): "Cold", (segment*6): "Very Cold"}