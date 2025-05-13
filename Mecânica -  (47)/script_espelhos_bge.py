import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
espelho = obj['espelho']
class MyGame():
    def espelhos(self):
        if "Render_Textura_Espelho" in espelho:
            espelho["Render_Textura_Espelho"].refresh(True)
        else:
            import VideoTexture
            camera = obj["cam_espelho"]
            camera.visible = True
            camera.lens = 18
            ID_Material = VideoTexture.materialID(espelho, "MA" + espelho["material"])
            renderToTexture = VideoTexture.Texture(espelho, ID_Material)
            renderToTexture.source = VideoTexture.ImageRender(scn, camera)
            espelho["Render_Textura_Espelho"] = renderToTexture

    def play(self):
        print("Game playing")
        
def run():
    MyGame().espelhos()
    MyGame().play()