import os

a=0
print('''
Bienvenido al Creador de Protocolos :D
''')
def menu():
    print('''
___________________________
____________ * ____________
    Opciones
    1. Crear Protocolo.
    2. Agregar uno paso.
    3. Borrar protoclo.
    4. Ver Protocolo.
---------------------------
''')
menu()
bandera=input("Desea realizar alguna de las opciones dadas? s/n \n")
if (bandera == "S" or bandera == "s"):

    while (bandera == "s" or bandera == "S"):
        opcion=str(input("¿Cual desea elegir? \n"))
        
        if opcion == "1":
            print("")
            name=input("Escriba el nombre de su protocolo: \n")
            protocolo = open(name + ".txt", 'w')
            protocolo.write('''___________________________
____________ \n'''+name+ '''* ____________  \n \n''')
            
            esc=input("¿Desea escribir las instruciones? s/n \n")
            while (esc == "s" or esc=="S"):
                a+=1

                print("_._._._._._._._._._._")
                instruccion=input("Escriba la "+str(a)+"° instruccion: \n")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                sub=input("¿Desea escribir una subinstruccion? s/n \n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escriba la subinstruccion: \n")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("¿Desea escribir la siguiente instrucion? s/n \n")
            print("Protocolo creado. ")
            protocolo.close()
            
        elif  opcion == "2":
            print("")
            
            name=input("Escriba el nombre del protocolo que quiere agregar pasos: \n")
            protocolo = open(name + ".txt",'a')
            
            esc=input("¿Desea agregar una instrucion? s/n \n")
            while (esc == "s" or esc=="S"):

                print("")
                instruccion=input("Escriba la instruccion: \n")
                protocolo.write(str(+a)+"-"+ instruccion + '''\n''')
                
                sub=input("¿Desea escribir una subinstruccion? s/n \n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escriba la subinstruccion: \n")
                    protocolo.write(str(+a)+".   -"+subinstruccion+'''\n''')
                    
                esc=input("¿Desea escribir la otra instrucion? s/n \n")
            print("Finalizo el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == "3":
            print("")
            name=input("Escriba el nombre del protocolo que quiere borrar: \n")
            os.remove(name + ".txt")
            print("El fichero ha sido removido")
            
        elif  opcion == "4":
            print("")
            name=input("Escriba el nombre del protocolo que quiere ver: \n")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.close()
                   
        bandera=input("¿Desea realizar otra de las opciones dadas? s/n \n")
        if (bandera=="s" or bandera=="S"):
            continue
        else:
            break
    print("Gracias por usar el software:)")
    
elif bandera == "N" or bandera == "n":
    print("Gracias por su preferencia :)")

else:
    print("Opcion Incorrecta")