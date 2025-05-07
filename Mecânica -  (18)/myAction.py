import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
KX_ACTION_MODE_PLAY = bge.logic.KX_ACTION_MODE_PLAY
KX_ACTION_BLEND_BLEND = bge.logic.KX_ACTION_BLEND_BLEND

class MyGame():
    def animAction(self):
        print('playing the action')
        name = "CubeAction"
        start_frame = 0
        end_frame = 100
        layer = 0
        priority = 0
        blendin = 0
        play_mode = KX_ACTION_MODE_PLAY
        layer_weight = 0.0
        ipo_flags = 0
        speed = 1.0
        blend_mode=KX_ACTION_BLEND_BLEND
        
        own.playAction(name, start_frame, end_frame, layer, priority, blendin, play_mode, layer_weight, ipo_flags, speed, blend_mode)
        
def run():
    MyGame().animAction()