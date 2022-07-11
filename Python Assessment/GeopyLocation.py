#Great Circle Distance:
##It is the length of the shortest path between 2 points on a sphere. In this case, the earth is assumed to be a perfect sphere. 
##Below program illustrates how to calculate great-circle distance from latitude-longitude data.

print("We can locate any place on earth from its geographic coordinates.")
from geopy.distance import geodesic as dist
   
data = [(26.19339, 73.11566), (25.98418, 73.35779), (18.66547, 81.13568)]

def total_distance(lst):

    if len(lst) == 1:
        return None
    x = len(lst) - 1        
    i = 0
    d = 0
    
    while x:
        coords_1 = lst[i]
        coords_2 = lst[i+1]
        i += 1
        x -= 1
        d += dist(coords_1,coords_2).km
    return d

print(f"The Total distance would be: {total_distance(data)} Km")

## We can locate any place on earth from its geographic coordinates.
## The Total distance would be: 1149.2745548322673 Km