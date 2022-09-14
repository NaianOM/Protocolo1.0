import os

a=0
print('''
Bienvenido al Creador de Protocolos :D
''')
def menu():
    print('''
_._._._._._._._._._._._._._._
    Opciones
    A.- Crear Protocolo
    B.- Agregar protocolo / subprotocolo
    C.- Borrar protoclo / subprotocolo
    D.- Ver Protocolo
_._._._._._._._._._._._._._._
''')
menu()
bandera=input("Desea realizar alguna de las opciones dadas? s/n \n")
if (bandera == "S" or bandera == "s"):

    while (bandera == "s" or bandera == "S"):
        opcion=str(input("¿Cual desea elegir? \n"))
        
        if opcion == "A":
            print("_._._._._._._._._._._")
            name=input("Escriba el nombre de su protocolo: \n")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
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
            print("Finalizamos el protocolo :D")
            protocolo.close()
            
        elif  opcion == "B":
            print("_._._._._._._._._._._")
            
            name=input("Escriba el nombre del protocolo que quiere agregar pasos: \n")
            protocolo = open(name + ".txt",'a')
            
            esc=input("¿Desea agregar una instrucion? s/n \n")
            while (esc == "s" or esc=="S"):

                print("_._._._._._._._._._._")
                instruccion=input("Escriba la instruccion: \n")
                protocolo.write(str(+a)+"-"+ instruccion + '''\n''')
                
                sub=input("¿Desea escribir una subinstruccion? s/n \n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escriba la subinstruccion: \n")
                    protocolo.write(str(+a)+".   -"+subinstruccion+'''\n''')
                    
                esc=input("¿Desea escribir la otra instrucion? s/n \n")
            print("Finalizo el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == "C":
            print("_._._._._._._._._._._")
            name=input("Escriba el nombre del protocolo que quiere borrar: \n")
            os.remove(name + ".txt")
            print("El fichero ha sido removido")
            
        elif  opcion == "D":
            print("_._._._._._._._._._._")
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