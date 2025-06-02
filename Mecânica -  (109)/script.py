import GameLogic
scene = GameLogic.getCurrentScene()
controller = GameLogic.getCurrentController()

obj = controller.owner
class PlayVideo():
	def play(self):
		if "Video" in obj:
			video = obj["Video"]
			video.refresh(True)

		else:
			import VideoTexture
			matID = VideoTexture.materialID(obj, "MA" + obj['material'])
			video = VideoTexture.Texture(obj, matID)
			
			movieName = obj['arquivoDeVideo']
			
			movie = GameLogic.expandPath('//' + movieName)
			
			video.source = VideoTexture.VideoFFmpeg(movie)
			
			video.source.scale = True	
			
			obj["Video"] = video	
			if "loop" in obj:		
				if obj['loop'] == True:
					video.source.repeat = -1		
				else:
					video.source.repeat = 0
			
			video.source.play()
		controller.activate(controller.actuators["Sound"])

def run():
	PlayVideo().play()
    
