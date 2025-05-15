import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
scl = bge.logic.getSceneList()
gdict = bge.logic.globalDict


class GameObject():
    def loc(self):
        pose_x = obj["player"].localPosition.x
        pose_y = obj["player"].localPosition.y
        gdict["px"] = pose_x
        gdict["py"] = pose_y
        xyz = obj["player"].localOrientation.to_euler()
        gdict["rot"] = [0, 0, xyz.z]
        
def getLoc():
    GameObject().loc()