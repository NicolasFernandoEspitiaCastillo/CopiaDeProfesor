import keyboard
def design():
    while True:
        try:
            keyboard.is_pressed('ctrl+c')
            print(f"""
            =============================================
                        OPTIONES DISPONIBLES
            =============================================
            1. Calcular propina
            2. Mostrar todas las propinas
            3. Buscar una propina
            4. Eliminar una propina
            5. Actualizar una propina
            6. Atras
            =============================================
            """)
            options = int(input("\t\tPor favor, elige una opción (1-6): "))
            if(options >= 1 and options <= 6):
                return options
            else:
                raise ValueError()
        except ValueError as e:
            print("\tUsuario elija una opción valida")
        except KeyboardInterrupt:
            print("\tUsuario elija una opción valida")