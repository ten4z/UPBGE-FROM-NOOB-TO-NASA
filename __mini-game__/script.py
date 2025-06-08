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
        planet = obj['planet']
        ori = planet.localPosition
        if obj['axis'].getDistanceTo(planet) >= 120:
            obj['axis'].applyMovement([-1, 0, 0], True)
        direcao = obj['axis'].localPosition - planet.localPosition
        obj['Cube']. localPosition = (obj['axis'].localPosition + planet.localPosition)/2
        obj['Cube'].localScale = [direcao.length/2, 1.0, 1.0]
        obj['Cube'].alignAxisToVect(direcao, 0)
        obj['axis'].alignAxisToVect(direcao, 0)
        
def run():
    MyGame().play()