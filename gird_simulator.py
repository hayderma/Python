import time, math


'''
Author Hayder MA
Python 3.X compatiable, program gives bearing in Degrees(and Rad.)
between two Geo-Points, write another script to get values from here
and adjust angle when needed
'''

def toDegree(x):
    deg = 180 * (x / math.pi)
    if (deg < 0):
        deg = 360 - abs(deg) 
    return deg

def cal_bearing(lat1,long1,lat2,long2):
    print("Calculating Bearing for Grid : \n ",lat1," ",long1," \n from ",lat2," ",long2,"...")
    y= math.sin(long2-long1) * math.cos(lat2)
    x=math.cos(lat1) * math.sin(lat2) - math.sin(lat1)* math.cos(lat2) * math.cos(long2-long1)
    bearing= math.atan2(y, x)
    
    
    return bearing
angle=270  

lat1= 30.894722
long1= -97.900556

i=0;
lat2= lat1
long2=long1
while (250>i):
    lat2+=0.00131
    long2-=0.00131
    #adj()
    #time.sleep(2)
    i+=1

print("coord1 = ",lat1 ,long1,"\n coor2 = ",lat2,long2)
angle = cal_bearing(lat1,long1,lat2,long2)
print("\nBearing = ",toDegree(angle)," Degrees\n")



