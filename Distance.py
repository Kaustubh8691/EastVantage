from math import radians, cos, sin, asin, sqrt

def getDistance(latitude1, longitude1, latitude2, longitude2):
    r = 6373.0

    latitude1 = radians(latitude1)
    longitude1 = radians(longitude1)
    latitude2 = radians(latitude2)
    longitude2 = radians(longitude2)

    dlon = longitude2 - longitude1
    dlat = latitude2 - latitude1

    # haversine formula
    a = sin(dlat / 2)**2 + cos(latitude1) * cos(latitude2) * sin(dlon / 2)**2 
    c = 2 * asin(sqrt(a))

    distance = r * c
    return distance