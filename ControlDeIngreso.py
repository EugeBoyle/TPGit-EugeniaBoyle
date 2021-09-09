#Ralizar un programa que permita tener un control del ingreso


list = []

menuPrincipal = int(input("Presione una opcion\n  1_ Ingresar nuevo\n  2_ Listar\n  Opción: "))

while menuPrincipal == 1:

        nombre = input ("Escriba su nombre: ")
        
        list.append(nombre) 
        

        menuPrincipal = int(input("Presione una opción\n 1_ Ingresar nuevo \n 2_ Listar\n Opción: "))   


for i in list:
    print(i)
        
input()  

        
        