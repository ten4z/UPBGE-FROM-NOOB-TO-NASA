import bge
import math
cont = bge.logic.getCurrentController()
sc = bge.logic.getCurrentScene()
obj = sc.objects
player = obj['player']
read_dict = bge.logic.globalDict

class MyGame():
    def read_or(self):
        xyz = player.localOrientation.to_euler()
        rotx = math.degrees(xyz[0])
        roty = math.degrees(xyz[1])
        rotz = math.degrees(xyz[2])
        read_dict['rotx'] = rotx
        read_dict['roty'] = roty
        read_dict['rotz'] = rotz        
        read_dict['posx'] = player.localPosition.x
        read_dict['posy'] = player.localPosition.y
        read_dict['posz'] = player.localPosition.z
        
def run(cont):    
    MyGame().read_or()
