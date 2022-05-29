def distance(x1, x2, y1, y2):
    x_dist = abs(x1 - x2)
    if x_dist > 180:
        x_dist = 360 - x_dist
    y_dist = abs(y1 - y2)
    if y_dist > 180:
        y_dist = 360 - y_dist
    deg = (x_dist ** 2 + y_dist ** 2) ** (0.5)
    return deg
