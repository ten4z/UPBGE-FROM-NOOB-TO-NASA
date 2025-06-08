import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects

class MyGame():    
    def doScreenShot(self):
        path = bge.logic.expandPath("//pictures/")  
        own['frame'] = 175      
        if  own['frame']  < 280:            
                        
            bge.render.makeScreenshot(path + "frame" + str(own['frame'] ) + ".png")
            print(str(own['frame']) + " Screenshot Criado faltam " + str(280 - own['frame']))
            own['frame'] += 1
            own['tempoFrame'] = 0
        else:
            own['frame'] = 281
                    
def render():
    MyGame().doScreenShot()