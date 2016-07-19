import time, math


'''
Author Hayder MA
Python 3.X compatiable program 
gives bearing in Degrees(and Rad.)
between two Geo-Points
write another script to get values from here
then adjust angle when needed
'''
def direction (angle):
    d = ""
    if (angle > 0 and angle < 90):
        d = "NE"
    elif (angle > 90 and angle < 180):
        d= "SE"
    elif (angle > 180 and angle < 270):
        d = "SW"
    elif (angle > 270 and angle < 360):
        d = "NW"
    elif (angle == 0):
        d= "N"
    elif (angle == 90 ):
        d = "E"
    elif (angle == 180):
        d = "S"
    elif (angle == 270):
        d = "W"

    return d

def toDegree(x):
    deg = 180 * (x / math.pi)
    if (deg < 0):
        deg = 360 - abs(deg) 
    return deg

def cal_bearing(lat1,long1,lat2,long2):
    print("Calculating Bearing for Grid : \n ",lat1," ",long1," \n from ",lat2," ",long2,"...")
    y = math.sin(long2-long1) * math.cos(lat2)
    
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1)* math.cos(lat2) * math.cos(long2-long1)

    bearing = math.atan2(y, x)
    
    
    return bearing
print ("Enter values in decimals (float) degrees form only \n")
lat1= float (input ("Lat. For Point 1 : "))
long1= float (input ("Long. For Point 1 : "))
lat2= float (input ("Lat. For Point 2 : "))
long2= float (input ("Long. For Point 2 : ")) 



print("coord1 = ",lat1 ,long1,"\n coor2 = ",lat2,long2)
angle = cal_bearing(lat1,long1,lat2,long2)
print("\nBearing = ",toDegree(angle)," Degrees " + direction(toDegree(angle))+"\n")



