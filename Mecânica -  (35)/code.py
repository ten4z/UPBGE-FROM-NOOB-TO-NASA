



import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects


class MyFunGame():
    def playGame(self):
        print("Script via Editor externo >>>")
        print("Este script fica fora na Aplicacao")
        print("Portanto arquivo Visivel no modo de Producao")



def run():    
    MyFunGame().playGame()
    