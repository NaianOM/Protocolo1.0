
import os

a=0
print('''

Bienvenido al creador de protocolos
''')
def menu():
    print('''
-_-_-_-_-_-_-_-_-_-_
    Opciones que puede seleccionar
    1. Crear
    2. Agregar
    3. Borrar
    4. Mostrar protocolo completo
-_-_-_-_-_-_-_-_-_-_
''')

menu()
opcion=input("¿Desea realizar alguna de las opciones dadas? si/no ")

if (opcion == "N" or opcion == "n" or opcion == "S" or opcion == "s"):

    opcion2 = input(print("Teclee el numero corrspondiente a su acción "))
    while (opcion2 == "1" or opcion == "2" or opcion == "3" or opcion == "4"):
        
        if opcion2 == "1":
            print(" ")
            name=input("escriba el nombre de su protocolo: ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            esc=input("desea escribir las instruciones? s/n ")
            while (esc == "s" or esc=="S"):
                a=a+1

                print(" ")
                instruccion=input("escriba la "+str(a)+"° instruccion: ")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                sub=input("desea escribir una subinstruccion? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("escriba la subinstruccion: ")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("desea escribir la siguiente instrucion? s/n ")
            print("hemos terminado el protocolo")
            protocolo.close()
            
        elif  opcion2 == "B":
            print(" ")
            
            name=input("escriba el nombre del protocolo que quiere agregar pasos: ")
            protocolo = open(name + ".txt",'a')
            
            esc=input("desea agregar una instrucion? s/n ")
            while (esc == "s" or esc=="S"):

                print(" ")
                instruccion=input("escriba la instruccion: ")
                protocolo.write("-"+ instruccion + '''\n''')
                
                sub=input("desea escribir una subinstruccion? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("escriba la subinstruccion: ")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("desea escribir la otra instrucción? s/n ")
            print("hemos terminado el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion2 == "3":
            print(" \n")
            name=input("escriba el nombre del protocolo que quiere borrar: ")
            print(" \n")
            os.remove(name + ".txt")
            print("el fichero ha sido removido")
            
        elif  opcion2 == "4":
            print(" ")
            print(name)
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.colse()
                   
        bandera=input("desea realizar otra de las opciones dadas? s/n ")
        if (bandera=="s" or bandera=="S"):
            continue
        else:
            break
    print("gracias por usar el software :)")
    
else:
    print("La opción tecleada, desgraciadamente, no es válida. ")
