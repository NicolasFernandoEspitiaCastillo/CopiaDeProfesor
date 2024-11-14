import keyboard
def design():
    while True:
        try:
            keyboard.is_pressed('ctrl+c')
            print(f"""
            =============================================
                        SIMULADOR DE PROPINA
            =============================================
            1. Calcular propina y total a pagar
            2. Calcular total a pagar divido entre varias personas
            3. Salir
            =============================================
            """)
            options = int(input("\t\tPor favor, elige una opción (1-3): "))
            if(options >= 1 and options <= 3):
                return options
            else:
                raise ValueError()
        except ValueError as e:
            print("\tUsuario elija una opción valida")
        except KeyboardInterrupt:
            print("\tUsuario elija una opción valida")