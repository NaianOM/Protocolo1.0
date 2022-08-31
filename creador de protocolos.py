
import os

a=0
print('''

Bienvenido a la maquina creadora de protocolos
ヽ(・∀・)ﾉ
''')
def menu():
    print('''
-------------------------
    Opciones
    1.-crear
    2.-agregar
    3.-borrar
    4.-ver
-------------------------
''')
menu()
bandera=input("desea realizar alguna de las opciones dadas? s/n ")
if (bandera == "N" or bandera == "s" or bandera == "S" or bandera == "n"):

    print("escriba el numero")
    while (bandera == "s" or bandera == "S"):
        opcion=int(input("cual desea elegir? "))
        
        if opcion == 1:
            print("-----------------")
            name=input("escriba el nombre de su protocolo: ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            esc=input("desea escribir las instruciones? s/n ")
            while (esc == "s" or esc=="S"):
                a=a+1

                print("-------------")
                instruccion=input("escriba la "+str(a)+"° instruccion: ")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                sub=input("desea escribir una subinstruccion? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("escriba la subinstruccion: ")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("desea escribir la siguiente instrucion? s/n ")
            print("hemos terminado el protocolo")
            protocolo.close()
            
        elif  opcion == 2:
            print("-----------------")
            
            name=input("escriba el nombre del protocolo que quiere agregar pasos: ")
            protocolo = open(name + ".txt",'a')
            
            esc=input("desea agregar una instrucion? s/n ")
            while (esc == "s" or esc=="S"):

                print("-------------")
                instruccion=input("escriba la instruccion: ")
                protocolo.write("-"+ instruccion + '''\n''')
                
                sub=input("desea escribir una subinstruccion? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("escriba la subinstruccion: ")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("desea escribir la otra instrucion? s/n ")
            print("hemos terminado el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == 3:
            print("-----------------")
            name=input("escriba el nombre del protocolo que quiere borrar: ")
            os.remove(name + ".txt")
            print("el fichero ha sido removido")
            
        elif  opcion == 4:
            print("-----------------")
            name=input("escriba el nombre del protocolo que quiere ver: ")
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
    print("gracias por usar el software :)")
