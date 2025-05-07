import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
tap = cont.sensors['tap']
set_cam = cont.actuators['set_cam']
tecla_direita = cont.sensors['tecla_direita']
tecla_esquerda = cont.sensors['tecla_esquerda']

class MyGame():
    def qualidadeTexto(self):
        for ob in obj:
            if 'txt' in ob:
                ob.resolution = 5
                ob.color = [0,0,0,1]
    def mudar_camera(self):
        if tap.positive:
            print("Game Iniciado.")

    def escolher_com_tecla(self):
        if tecla_direita.positive:
            print("tecla direita pressionada!")
            own['cam']+= 1

        if tecla_esquerda.positive:
            print("tecla esquerda pressionada!")
            own['cam'] -= 1

    def aplicar_camera(self):
        if own['cam'] == 0:
            own['cam'] = 3
        elif own['cam'] == 1:
            cont.activate(set_cam)
            set_cam.camera = 'camera_topo'
        elif own['cam'] == 2:
            cont.activate(set_cam)
            set_cam.camera = 'camera_frontal'
        elif own['cam'] == 3:
            cont.activate(set_cam)
            set_cam.camera = 'camera_perspectiva'
        elif own['cam'] == 4:
            own['cam']= 1
        else:
            own['cam'] = 0 

def run():
    MyGame().mudar_camera()
    MyGame().escolher_com_tecla()
    MyGame().aplicar_camera()
    MyGame().qualidadeTexto()