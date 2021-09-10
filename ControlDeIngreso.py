#Ralizar un programa que permita tener un control del ingreso


list = []

menuPrincipal = int(input("Presione una opcion\n 1_ Ingresar nuevo\n 2_ Eliminar\n 3_ Listar\n Opción: "))

while menuPrincipal != 3:
        if menuPrincipal == 1:
            nombre = input ("Escriba su nombre: ")
            
            list.append(nombre) 
        elif menuPrincipal == 2:
            for i in list:
                print(i)
            delete = input('A quien desea eliminar: ')
            for i in list:
                if delete == i:
                    list.remove(i)
                    print(i,'Eliminado')
                    
        menuPrincipal = int(input("Presione una opcion\n 1_ Ingresar nuevo\n 2_ Eliminar\n 3_ Listar\n Opción: "))  


for i in list:
    print(i)
        
input()  

        
        