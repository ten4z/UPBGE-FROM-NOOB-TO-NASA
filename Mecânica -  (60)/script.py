import bge
import math
cont = bge.logic.getCurrentController()
own = cont.owner
sc = bge.logic.getCurrentScene()
obj = sc.objects
dict_mm = bge.logic.globalDict
pose_camera = obj['cursor']

class MiniMapa():
    def write_or(self):        
        xyz = pose_camera.localOrientation.to_euler()
        xyz[0] = math.radians(dict_mm['rotx'])
        xyz[1] = math.radians(dict_mm['roty'])
        xyz[2] = math.radians(dict_mm['rotz'])
        pose_camera.localOrientation = xyz.to_matrix()
        pose_camera.localPosition = [dict_mm['posx'],dict_mm['posy'],dict_mm['posz']]
        
def run(cont):
    MiniMapa().write_or()