import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
scl = bge.logic.getSceneList()
circle = obj["circle"]
gdict = bge.logic.globalDict

class CursorMap():
    def showMap(self):
        #print("must show the map")
        for sc in scl:
            if sc.name == "hud_engine":
                px = float(gdict["px"])
                py = float(gdict["py"])
                sc.objects["eixo_hud"].localPosition = [px, py, 0]
                sc.objects["cursor_hud"].localOrientation = gdict["rot"]
                
        if "RenderToTexture" in circle:
            circle["RenderToTexture"].refresh(True)
        else:
            import VideoTexture
            for sc in scl:
                if sc.name == "hud_engine":
                    cam = sc.objects["cam_hud"]
                    matID = VideoTexture.materialID(circle, "MA" + circle["material"])
                    renderToTexture = VideoTexture.Texture(circle, matID)
                    renderToTexture.source = VideoTexture.ImageRender(sc, cam)
                    circle["RenderToTexture"] = renderToTexture


def myMap():
    CursorMap().showMap()