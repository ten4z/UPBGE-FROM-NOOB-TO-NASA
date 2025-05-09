import bge 
from math import degrees, radians
cont = bge.logic.getCurrentController()
own = cont.owner

xyz = own.localOrientation.to_euler()
xyz.x = radians(30)
xyz.y = radians(-45)
xyz.z = radians(15)
own.localOrientation = xyz

print(degress(xyz.z))