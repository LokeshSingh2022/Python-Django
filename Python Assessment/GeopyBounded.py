print("\nProgram to find that any point is bounded by another point of radius 'r': ")

from geopy.distance import great_circle as D

lst = [(29.38305, 79.46473), (29.38291, 79.46472), (29.38298, 79.46483), (29.38298, 79.46483), (29.38304, 79.46489), (29.38293, 79.46506), (29.38304, 79.46506), (29.38309, 79.46501)]
center_Coord = (29.38308, 79.46486)
Radius = 19.88205852403358
n = len(lst)-1

i=0
while n:
    coords_1 = center_Coord
    coords_2 = lst[i]
    i+=1
    n-=1
    dist = D(coords_1,coords_2).meters
    if dist < Radius:
        print(f"Point {lst[i]} is inside the Circle.")
    elif dist > Radius:
        print(f"Point {lst[i]} is outside the Circle.")
    else:
        print(f"Point {lst[i]} is on the Circle.")