import bge
cont = bge.logic.getCurrentController()
own = cont.owner
malha = own.meshes[0]
verts = malha.getVertexArrayLength(0)
obj = own.scene.objects
def aplicar():    
    for v in range(0, verts):
        ponto = malha.getVertex(0, v)
        uv = ponto.getUV()
        x = own['fx']
        y = own['fy']
        if cont.sensors['tap'].positive:
            uv[0] += x*(0.125) + 128
            uv[1] += y*(0.125) + 128
            ponto.setUV(uv)            