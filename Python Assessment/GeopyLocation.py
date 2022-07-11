#Great Circle Distance:
##It is the length of the shortest path between 2 points on a sphere. In this case, the earth is assumed to be a perfect sphere. 
##Below program illustrates how to calculate great-circle distance from latitude-longitude data.

print("We can locate any place on earth from its geographic coordinates.")
from geopy.distance import great_circle as GC
   
data = [(34.15191, 77.57611), (34.15124, 77.57662), (34.15057, 77.57714), (34.14958, 77.57800), (34.14859, 77.57886), (34.14729, 77.58000), (34.14599, 77.58114), (34.14405, 77.58283), (34.14211, 77.5845)]

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
        d += GC(coords_1,coords_2).meters
    return d

print(f"The Total distance would be: {total_distance(data)} Meters")

## We can locate any place on earth from its geographic coordinates.
## The Total distance would be: 1149.2745548322673 Km