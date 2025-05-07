import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects

p1 = obj['p1']
p2 = obj['p2']
ob = obj['ob']

class MyGame():
    def ligarPontos(self):
        AXIS_X = 0
        direcao = p1.localPosition - p2.localPosition
        pm = (p1.localPosition + p2.localPosition) / 2
        d = direcao.length/2
        ob.localPosition = pm
        ob.localScale = [d, 0.1, 0.1]
        ob.alignAxisToVect(direcao, AXIS_X)
    
def run():
    MyGame().ligarPontos()