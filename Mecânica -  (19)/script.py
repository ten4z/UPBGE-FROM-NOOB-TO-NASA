import bge
from datetime import datetime
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects

f2_key = cont.sensors['f2_key']

class MyGame():
    def doScreenShot(self):
        path = bge.logic.expandPath("//")
        if f2_key.positive:
            agora = datetime.now()
            txt = agora.strftime("%A %d. %B %Y %H-%M-%S")
            bge.render.makeScreenshot(path + txt + ".png")
            print("Screenshot Criado com Sucesso.")
        
def run():
    MyGame().doScreenShot()