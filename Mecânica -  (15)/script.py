import GameLogic
scene = GameLogic.getCurrentScene()
controller = GameLogic.getCurrentController()
obj = controller.owner
scl = GameLogic.getSceneList()
gdict = GameLogic.globalDict

def myMap():

	
	if "RenderToTexture" in obj:
		obj["RenderToTexture"].refresh(True)
	
	else:		
		import VideoTexture
		for sc in scl:
			if sc.name == "Portrait":
				cam = sc.objects['cam']
				sc.active_camera =  sc.objects['default_cam']
				matID = VideoTexture.materialID(obj, "MA" + obj['material'])				
				renderToTexture = VideoTexture.Texture(obj, matID)
				renderToTexture.source = VideoTexture.ImageRender(sc,cam)
				obj["RenderToTexture"] = renderToTexture