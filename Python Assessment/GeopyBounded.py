print("\nProgram to find that any point is bounded by another point of radius 'r': ")

from geopy.distance import great_circle as D

data = [(29.37996, 79.46684), (29.37996, 79.46689)]

radius = 4.844688950131238
coord_1 = data[0]
coord_2 = data[1]

dist = D(coord_1, coord_2).meters

if dist < radius:
    print(f"Point is inside the Enclosed Boundary\n")
elif dist > radius:
    print(f"Point is outside the Enclosed Boundary\n")
else:
    print(f"Point is In the Boundary\n")
