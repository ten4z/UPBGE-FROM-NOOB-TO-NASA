import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
scl = bge.logic.getSceneList()

tap = cont.sensors['tap']
keyboard = bge.logic.keyboard

class MyGame():
    def __init__(self):
        if tap.positive:
            print("Game iniciado.")

    def controls(self):                             
        if keyboard.inputs[bge.events.DKEY].active:
             obj['axis'].applyRotation([-0.2,0,0], True)

        if keyboard.inputs[bge.events.AKEY].active:
             obj['axis'].applyRotation([0.2,0,0], True)

        if keyboard.inputs[bge.events.SPACEKEY].active:
             obj['axis'].applyMovement([2,0,0], True)

        if keyboard.inputs[bge.events.WKEY].active:
             obj['axis'].applyMovement([0,1,0], True)
        

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
    MyGame().controls()
    MyGame().play()