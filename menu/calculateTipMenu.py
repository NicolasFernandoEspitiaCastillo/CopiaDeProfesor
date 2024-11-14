from formula.logic import calcular_propina, calcular_total_con_propina
from server.saveTip import saveTip
import os
import keyboard

def design():
    while True:
        print(f"""
        =============================================
                    Cálculo de Propina
        =============================================""")
        try:
            keyboard.is_pressed('ctrl+c')
            total = int(input("\tIngrese el total a pagar (por ejemplo: 100, 200, 300): "))
            if(total < 0):
                raise ValueError()
            porcentaje = int(input("\tIngrese el porcentaje de propina (por ejemplo: 10, 15, 20): "))
            if(porcentaje < 0):
                raise ValueError()
            propina = calcular_propina(total, porcentaje)
            totalPagar = calcular_total_con_propina(total, propina)
            print(f"""
            =============================================
            La propina calculada es: ${propina}
            El total a pagar es: ${totalPagar}
            =============================================
            """)
            saveTip({'monto': total, 'propina': propina, 'montoTotalPagar': totalPagar, "porcentaje": porcentaje})
            opcion = int(input("\t¿Desea calcular otra propina? (1-S, 0-N): "))
            if(opcion == 0): return None
            os.system('clear')
        except ValueError as e:
            print("\tUsuario los datos solicitados no son válidos, ingrese datos de tipo entero")
        except KeyboardInterrupt:
            print("`\n\tSeñor usuario no presionó Ctrl+C, termine la ejecución del programa y selecione una de las opciones disponibles")
        

