from menu.mainMenu import design as designPrincipal
from menu.calculateTipMenu import design as designOpcion1
from menu.divideAmountsMenu import design as designOpcion2
from menu.optionTipMenu import design as designOpcionTip1
from server.findAllTip import optionTipOne
from server.findByIdTip import optionTipThree
from server.deleteByIdTip import optionTipFour
from tabulate import tabulate
import keyboard

while True:
    match designPrincipal():
        case 1: 
            while True:
              option = designOpcionTip1()
              if(option == 1): designOpcion1()
              elif(option == 2): print(tabulate(optionTipOne(), headers="keys"))
              elif(option == 3): 
                try:
                  keyboard.is_pressed('ctrl+c')
                  id = int(input("Ingrese el id de la propina que desea consultar: "))
                  if(id < 0):
                      raise ValueError()
                  print(tabulate([optionTipThree(id)], headers="keys"))
                except ValueError as e:
                    print("\tUsuario los datos solicitados no son válidos, ingrese datos de tipo entero")
                except KeyboardInterrupt:
                    print("`\n\tSeñor usuario no presionó Ctrl+C, termine la ejecución del programa y selecione una de las opciones disponibles")
              elif(option == 4): 
                try:
                  keyboard.is_pressed('ctrl+c')
                  id = int(input("Ingrese el id de la propina que desea consultar: "))
                  if(id < 0):
                      raise ValueError()
                  optionTipFour(id)
                  print("Propina eliminada con éxito")
                except ValueError as e:
                    print("\tUsuario los datos solicitados no son válidos, ingrese datos de tipo entero")
                except KeyboardInterrupt:
                    print("`\n\tSeñor usuario no presionó Ctrl+C, termine la ejecución del programa y selecione una de las opciones disponibles")
  

              elif(option == 6): break
        case 2: designOpcion2()
        case 3:
            print("""
            =============================================
              ¡Gracias por usar el Simulador de Propina!
            =============================================
            """)
            exit()

