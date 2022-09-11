
from ast import While
import os

a=0
print('''

Bienvenido al creador de protocolos dinámico
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
opcion=input("¿Desea realizar alguna de las opciones dadas? si/no \n")

while (opcion == "Si" or opcion == "si"):

    opcion2 = input(print("Teclee el numero corrspondiente a su acción \n"))
    while (opcion2 == "1" or opcion == "2" or opcion == "3" or opcion == "4"):
        
        if opcion2 == "1":
            print(" ")
            name=input("escriba el nombre de su protocolo: \n")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            esc=input("¿Desea escribir las instruciones? s/n \n")
            while (esc == "s" or esc=="S"):
                a=a+1

                print(" ")
                instruccion=input("escriba la "+str(a)+"° instruccion: \n")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                sub=input("desea escribir una subinstruccion? s/n \n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("escriba la subinstruccion: \n")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("desea escribir la siguiente instrucion? s/n \n")
            print("hemos terminado el protocolo")
            protocolo.close()
            
        elif  opcion2 == "2":
            print(" ")
            
            name=input("escriba el nombre del protocolo que quiere agregar pasos: \n")
            protocolo = open(name + ".txt",'a')
            
            esc=input("desea agregar una instrucion? s/n \n")
            while (esc == "s" or esc=="S"):

                print(" ")
                instruccion=input("escriba la instruccion: \n")
                protocolo.write("-"+ instruccion + '''\n''')
                
                sub=input("desea escribir una subinstrucción? s/n \n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escriba la subinstrucción: \n")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("Desea escribir la otra instrucción? s/n \n")
                if esc == "n":
                print("hemos terminado el cambio en el protocolo "+name)
                protocolo.close()
                break
            
            
        elif  opcion2 == "3":
            print(" \n")
            name=input("escriba el nombre del protocolo que quiere borrar: \n")
            print(" \n")
            os.remove(name + ".txt")
            print("El elemento ha sido removido ")
            
        elif  opcion2 == "4":
            print(" ")
            print(name)
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.colse()
                   
        bandera=input("desea realizar otra de las opciones dadas? si/no \n")
        if (bandera=="si" or bandera=="Si"):
            continue
        elif (bandera=="no" or bandera=="No"):
            print("Gracias por usar el creador de protocolos :))")
        else:  
            print("No es una opción válida. ")
else:
    if (opcion == "No" or opcion == "no" or opcion == "NO"):
        print("Gracias por usar el creador de protocolos :))")
    else:
        print("La opción tecleada, desgraciadamente, no es válida.")

