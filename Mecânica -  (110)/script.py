import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = bge.logic.getCurrentScene()
scl = bge.logic.getSceneList()
obj = scn.objects
tap = cont.sensors['tap']

clique = cont.sensors['clique']
mmove = cont.sensors['mmove']
mo_next = cont.sensors['mo_btn_next']

class MyGame():
    nextCont = None
    current_sc = None
    objList = ['Suzanne', 'Cube', 'Cone', 'Torus']
    def doTap(self):
        if tap.positive:            
            print("this is a tap") 
    def stopAllScenes(self):
        for sc in scl:
            for texto in self.objList:                
                if texto in sc.objects: 
                    own['playPause'] = False                   
                    sc.suspend()
        
    def nextScene(self):
        if own['curScene'] == 'suzanne': 
            own['curScene'] = 'cube' 
        elif own['curScene'] == 'cube': 
            own['curScene'] = 'cone' 
        elif own['curScene'] == 'cone': 
            own['curScene'] = 'torus' 
        elif own['curScene'] == 'torus': 
            own['curScene'] = 'suzanne'  
            
    def previousScene(self):
        if own['curScene'] == 'suzanne': 
            own['curScene'] = 'torus' 
        elif own['curScene'] == 'cube': 
            own['curScene'] = 'suzanne' 
        elif own['curScene'] == 'cone': 
            own['curScene'] = 'cube' 
        elif own['curScene'] == 'torus': 
            own['curScene'] = 'cone'   
                     
    def scTransition(self):
        self.current_sc = own['curScene']        
        for sc in scl:
            if sc.name == "Scene":                
                self.nextCont = sc.objects['btn_play'].controllers[0]                
            elif sc.name == self.current_sc:
                if sc.name == "suzanne":
                    sc.objects['Suzanne'].localPosition = [0, -10.0, 0]
                    sc.objects['Suzanne'].visible = True
                    if own['playPause'] == True:
                        sc.resume()
                    else:
                        sc.suspend()

                elif sc.name == "cube":
                    sc.objects['Cube'].visible = True
                    sc.objects['Cube'].localPosition = [0, -10.0, 0]
                    if own['playPause'] == True:
                        sc.resume()
                    else:
                        sc.suspend()

                elif sc.name == "torus":
                    sc.objects['Torus'].visible = True
                    sc.objects['Torus'].localPosition = [0, -10.0, 0]
                    if own['playPause'] == True:
                        sc.resume()
                    else:
                        sc.suspend()
                elif sc.name == "cone":
                    sc.objects['Cone'].visible = True
                    sc.objects['Cone'].localPosition = [0, -10.0, 0]
                    if own['playPause'] == True:
                        sc.resume()
                    else:
                        sc.suspend()
            else:
                for texto in self.objList:                
                    if texto in sc.objects:
                        sc.objects[texto].visible = False
            if self.nextCont is not None:
                next_scene = self.nextCont.owner.scene                                    
                if own['withSound'] == True:
                    if self.nextCont.sensors['btn_click'].positive:
                        cont.activate(cont.actuators['clickSound'])
                        next_scene.objects['btn_sound'].replaceMesh('btn_nosound_over', True, False)
                    else:
                        next_scene.objects['btn_sound'].replaceMesh('btn_sound', True, False)
                if self.nextCont.sensors['btn_next'].positive:
                    print("sensor detected!")
                    print("and the scene is: ", self.nextCont.owner.scene)
                    next_scene.objects['btn_next'].replaceMesh('btn_next_over', True, False)
                    if self.nextCont.sensors['btn_click'].positive:
                        self.nextScene()
                else:
                    next_scene.objects['btn_next'].replaceMesh('btn_next', True, False)
                    
                if self.nextCont.sensors['btn_previous'].positive:  
                    next_scene.objects['btn_previous'].replaceMesh('btn_previous_over', True, False)
                    if self.nextCont.sensors['btn_click'].positive:
                        self.previousScene()  
                else:
                    next_scene.objects['btn_previous'].replaceMesh('btn_previous', True, False)
                if self.nextCont.sensors['btn_play'].positive:  
                    next_scene.objects['btn_play'].replaceMesh('btn_play_over', True, False)
                    if self.nextCont.sensors['btn_click'].positive:
                        cont.activate(cont.actuators['togglePlay'])
                else:
                    next_scene.objects['btn_play'].replaceMesh('btn_play', True, False) 
                if self.nextCont.sensors['btn_sound'].positive:  
                    if self.nextCont.sensors['btn_click'].positive:
                        cont.activate(cont.actuators['toggleSound'])

                if self.nextCont.sensors['btn_stop'].positive:  
                    next_scene.objects['btn_stop'].replaceMesh('btn_stop_over', True, False)
                    if self.nextCont.sensors['btn_click'].positive:
                        self.stopAllScenes()
                else:
                    next_scene.objects['btn_stop'].replaceMesh('btn_stop', True, False)              
        
    def playGame(self):        
        pass        
        
def run():
    MyGame().doTap()
    MyGame().scTransition()
    MyGame().playGame()