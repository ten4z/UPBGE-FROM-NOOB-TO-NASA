import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
scl = bge.logic.getSceneList()

tap = cont.sensors['tap']

class MyGame():
    def __init__(self):
        if tap.positive:
            print("Game iniciado.")

    def play(self):
        pass
        #print("Game playing")
        
def run():
    MyGame().play()