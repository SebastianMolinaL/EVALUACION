import random
lista_multa = []
opcion = 0
lista_tipo = []
lista_patente = []
lista_marca = []
lista_precio = []
lista_fecha_registro = []
lista_dueño = []
lista_certif = []
opcion_multa = ''
contador = 0
fecha = ''


while True:
    print('''

------------------------------------------------------------------------------------

                        AUTOMOTORA AUTO SEGURO 


1) Grabar vehículo    2) Buscar vehículo por patente    3) Imprimir certificados
                      
                             4) Salir

-----------------------------------------------------------------------------------                             

        ''')
    opcion = input("Ingrese el número de la opción que desea ejecutar: ")
    while not opcion.isnumeric():
        print('El valor ingresado no es valido, vuelva a intentarlo')
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
    if int(opcion) == 1:
        print('''
 ------------------------------------------------------------------------------------

                         AUTOMOTORA AUTO SEGURO 


    INGRESE SU PLACA PANTENE:                    

-----------------------------------------------------------------------------------
    ''')
        patente = input("Ingrese la patente del vehículo: ")
        while not patente.isalnum():
            print('Ingrese una opcion valida')
            patente = input("Ingrese la patente del vehículo: ")
        contador = lista_patente.count(patente.upper())
        if contador == 1:
            print(f'Actualmente existe el vehiculo patente: {patente.upper()}')
            contador = 0
            input('Precione enter para continuar')
        elif contador == 0:
            lista_patente.append(patente.upper())
            print(lista_patente)
            print(f'''
-----------------------------------------------------------------------------------
                  
                                                         AUTOMOTORA AUTO SEGURO 
                  
                        Tipo Vehiculo

        1) SUV   2) MOTOCICLETAS  3) FURGON  4) PICKUP               PLACA PATENTE    
                                                                       {patente}
                          
-----------------------------------------------------------------------------------
                    ''')
            tipo = input("Ingrese el tipo de vehículo: ")
            while not tipo.isnumeric():
                print('Ingrese una opcion valida')
                tipo = input("Ingrese el tipo de vehículo: ")
            if int(tipo) == 1:
                lista_tipo.append('SUV')
            elif int(tipo) == 2:
                lista_tipo.append('MOTOCICLETA')
            elif int(tipo) == 3:
                lista_tipo.append('FURGON')
            elif int(tipo) == 4:
                lista_tipo.append('PICKUP')  
            print(f'''
-----------------------------------------------------------------------------------
                  
                                                       AUTOMOTORA AUTO SEGURO
                  
                        
     INGRESE LA MARCA DE SU VEHICULO:                    PLACA PATENTE    
                                                           {patente}

-----------------------------------------------------------------------------------
            ''')  
            marca = input("Ingrese la marca del vehículo: ")
            while not marca.isalpha():
                print('Ingrese una opcion valida')
                marca = input("Ingrese la marca del vehículo: ")
            while len(marca) <= 2 or len(marca) >= 15:
                print('La marca debe contener entre 2 a 15 caracteres.')
                marca = input("Ingrese la marca del vehículo: ")
            lista_marca.append(marca.upper())
            precio = input("Ingrese el precio del vehículo: ")
            while not precio.isnumeric():
                print('Ingrese una opcion valida')
                precio = input("Ingrese el precio del vehículo: ")
            while int(precio) < 5000000:
                print('El precio del vehiculo debe ser mayor que 5.000.000$')
                precio = input("Ingrese el precio del vehículo: ")
            lista_precio.append(precio)

            print('''

------------------------------------------------------------------------------

                                                         AUTOMOTORA AUTO SEGURO

            ¿Posee multas el vehículo?

        1) Si                         2) No
            
-------------------------------------------------------------------------------
            ''')
            opcion_multa = input('Ingrese una opcion')
            while not opcion_multa.isnumeric():
                print('Ingrese una opcion valida')
                opcion_multa = input('Ingrese una opcion')
            if int(opcion_multa) == 1:
                monto = random.randint(1500, 3500)
                fecha = input("Ingrese la fecha de la multa: ")
                lista_multa.append([1, monto, fecha]) 
            elif int(opcion_multa) == 2:
                lista_multa.append(0)
            print(f'''
------------------------------------------------------------------------------

                                                    AUTOMOTORA AUTO SEGURO
              
          INGRESE LA FECHA DE HOY: 
                                                        PLACA PATENTE    
                                                           {patente}

-------------------------------------------------------------------------------
            
            
            ''')
            fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
            lista_fecha_registro.append(fecha_registro)
            print(f'''
------------------------------------------------------------------------------

                                                    AUTOMOTORA AUTO SEGURO
                     
          INGRESE EL NOMBRE DEL PROPIETARIO
                   DEL VEHICULO: 
                                                        PLACA PATENTE    
                                                           {patente}

-------------------------------------------------------------------------------
            
            
            
            ''')
            dueño = input("Ingrese el nombre del dueño del vehículo: ")
            while not dueño.isalpha():
                print('Ingrese una opcion valida')
                dueño = input("Ingrese el nombre del dueño del vehículo: ")
            lista_dueño.append(dueño)

                
    
        
    elif int(opcion) == 2:
        print('''
 ------------------------------------------------------------------------------------

                         AUTOMOTORA AUTO SEGURO 


    INGRESE SU PLACA PANTENE:                    

-----------------------------------------------------------------------------------
    ''')
        patente = input("Ingrese la patente del vehículo: ")
        while not patente.isalnum():
            print('Ingrese una opcion valida')
            patente = input("Ingrese la patente del vehículo: ")
        contador = lista_patente.count(patente.upper())
        if contador == 1:
            for i in range(len(lista_patente)):
                if patente.upper() == lista_patente[i]:
                    mos_list = lista_multa[i][0]
                    print(f'''
        
            1) PATENTE: {lista_patente[i]}
            2) TIPO: {lista_tipo[i]}
            3) MARCA: {lista_marca[i]}
            4) PRECIO: {lista_precio[i]}
            5) MULTA: {mos_list}
            6) FECHA INGRESO:{lista_fecha_registro[i]}
            7) DUEÑO: {lista_dueño[i]}

     ''')
                    input('Presione enter para continuar')
        else:
            print(f'No existe la patente {patente} ')

    elif int(opcion) == 3:
        while True:
            print('''
------------------------------------------------------------------------

                    AUTOMOTORA AUTO SEGURO 

           1) MULTAS                         2) Salir

------------------------------------------------------------------------
    ''')
            opcion = input('Que documento desea emitir?: ')
            while not opcion.isnumeric():
                print('Ingrese una opcion valida')
                opcion = input('Que documento desea emitir?: ')
            if int(opcion) == 1:
                print('''
 ------------------------------------------------------------------------------------

                         AUTOMOTORA AUTO SEGURO 


    INGRESE SU PLACA PANTENE:                    

-----------------------------------------------------------------------------------
    ''')
                patente = input("Ingrese la patente del vehículo: ")
                while not patente.isalnum():
                    print('Ingrese una opcion valida')
                    patente = input("Ingrese la patente del vehículo: ")
                contador = lista_patente.count(patente.upper())
                if contador == 1:
                    for i in range(len(lista_patente)):
                        if patente.upper() == lista_patente[i]:
                            print(f'''
         
           EMISION DE CONTAMINANTES      
        -----------------------------------------------------------------------------  
            PLACA PATENTE                    DUEÑO DEL VEHICULO   
           {lista_patente[i]}                         {lista_dueño[i]}       

           VALOR: {lista_multa[i][1]} FECHA DE LA MULTA: {lista_multa[i][2]}
           
                                   ''')
                            break
                else:
                    print(f'No existe la patente {patente} ')
                    break

            elif int(opcion) == 2:
                break
                
    elif int(opcion) == 4:
        print('Muchas gracias, hasta pronto')
        break

