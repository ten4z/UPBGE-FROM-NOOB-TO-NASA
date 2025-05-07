import bge
cont = bge.logic.getCurrentController()
own = cont.owner
malha = own.meshes[0]
verts = malha.getVertexArrayLength(0)

class MyGame():
    def animarUVMap(self):
        for v in range(0, verts):
            ponto = malha.getVertex(0, v)
            uv = ponto.getUV()
            uv[1] += 0.0005
            ponto.setUV(uv)
            
        
def run():
    MyGame().animarUVMap()