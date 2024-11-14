from formula.logic import calcular_propina, calcular_total_con_propina, dividir_total
import os
import keyboard

def design():
    opcion = 1
    while opcion:
        print(f"""
        =============================================
            Dividir Cuenta entre Varias Personas
        =============================================""")
        try:
            keyboard.is_pressed('ctrl+c')
            total = int(input("\tIngrese el monto total de la cuenta: $"))
            if(total < 0):
                raise ValueError()
            porcentaje = int(input("\tIngrese el porcentaje de propina (por ejemplo: 10, 15, 20): "))
            if(porcentaje < 0):
                raise ValueError()
            personas = int(input("\tIngrese el número de personas: "))
            if(personas < 0):
                raise ValueError()
            propina = calcular_propina(total, porcentaje)
            totalMasPropina = calcular_total_con_propina(total, propina)
            print(f"""
            =============================================
            La propina calculada es: ${propina}
            El total a pagar es: ${totalMasPropina}
            Monto por persona: ${dividir_total(totalMasPropina, personas)}
            =============================================""")
            opcion = int(input("\t¿Deseas calcular nuevamente? (1-S, 0-N): "))
            os.system('clear')
        except ValueError as e:
            print("\tUsuario los datos solicitados no son válidos, ingrese datos de tipo entero")
        except KeyboardInterrupt:
            print("`\n\tSeñor usuario no presionó Ctrl+C, termine la ejecución del programa y selecione una de las opciones disponibles")