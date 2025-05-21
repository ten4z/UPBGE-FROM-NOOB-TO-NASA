import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
scl = bge.logic.getSceneList()

tap = cont.sensors['tap']
txt = obj["txt"]
txt.resolution = 5
txt["Text"] = "debug"
cubo = obj["Cube"]

class MyGame():
    def __init__(self):
        if tap.positive:
            print("Game iniciado.")

    def play(self):
        

        
                
        if cubo["girar"] == True:
            cont.activate(cont.actuators["Motion"])
        else:
            cont.deactivate(cont.actuators["Motion"])
            
        if cont.sensors['Keyboard'].positive:                            
            if cubo["girar"] == True:
                cubo["girar"] = False
                
            elif cubo["girar"] == False:
                cubo["girar"] = True

                    
       
        
def run():
    MyGame().play()