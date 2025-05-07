import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects

#bge.types.BL_ActionActuator(SCA_IActuator)
ActAnim = cont.actuators['ActAnim']


KX_ACTIONACT_PLAY = bge.logic.KX_ACTIONACT_PLAY
KX_ACTIONACT_PINGPONG = bge.logic.KX_ACTIONACT_PINGPONG

class MyGame():
    def runAnim(self):
        
        cont.activate(ActAnim)        
        ActAnim.action = "CubeAction"
        ActAnim.frameStart = 0.0
        ActAnim.frameEnd = 100.0
        ActAnim.mode = KX_ACTIONACT_PLAY



def run():
    MyGame().runAnim()