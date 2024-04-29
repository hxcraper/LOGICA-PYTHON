'''
ESTRUCTURA DE DATOS
'''

''' 
LISTAS
'''
my_list = ["Enrique", "Black", "Wolfy", "Visionos"]
print(my_list)

my_list.append('Brian') # inserción

print(my_list)

my_list.remove('Enrique') # eliminación

print(my_list)

print(my_list[2]) # acceso

my_list[1] = "Enrique" # actualización

print(my_list)

my_list.sort() # ordena alfabeticamente
print(my_list)

'''
TUPLAS (inmutable)
'''

my_tuple: tuple = ('enrique','burotto', 'kike', '30' )
print(my_tuple[0]) # acceso
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # ordenación
print(my_tuple)
print(type(my_tuple))

'''
SETS ( Estructura no ordernada, que no muestra duplicados)
''' 
# sirve en caso de querer buscar datos precisos y rapidamente

my_set = {'enrique','burotto', 'kike', '30' }
print(my_set) # acceso
my_set.add("hxcraper@gmail.com") # inserción
my_set.add("hxcraper@gmail.com") 
print(my_set) # no va a mostrar el duplicador colocado
print(type(my_set))
my_set.remove('enrique')
print(my_set)
my_set = set(sorted(my_set)) # da igual si lo queremos ordenar, no tiene orden
print(my_set)

'''
DICCIONARIO (solo son ordenados en python)
'''

"""
# es clave, valor
my_dict = {
    'name' : 'kike',
    'email' : 'hxcraper@gmail.com',
    'age' : '30'
}

# my_dict['age'] = '20' # actualización
# del my_dict['email'] # eliminar
# my_dict['age'] # acceso
# print(my_dict)
# print(type(my_dict))
my_dict = dict(sorted(my_dict.items())) # el items es para acceder a los items, y poder ordenarlos
print(my_dict)
print(type(my_dict))
"""



def my_agenda():

    def agree_contact():
        phone = input('Introduce el numero de contacto: ')
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 9:
            agenda[name] = phone
            print('Contacto actualizado correctamente !!!')
        else:
            print('Debes introducir un numero menor a 9 digitos')

    agenda = {}

    while True:

        print("")
        print("1.- Buscar contacto")
        print("2.- Insertar contacto")
        print("3.- Actualizar contacto")
        print("4.- Eliminar contacto")
        print("5.- Salir")

        option = input(' \n Selecciona una opción a buscar: ')

        match option:
            case "1":
                name = input('Ingresa el nombre del contacto a buscar: ')
                if name in agenda:
                    print(f'El numero de telefono de {name} es: {agenda[name]}')
                else:
                    print(f'El contacto {name} no existe, favor de agregarlo')
            case "2":
                name = input('Introduce el nombre del contacto a agregar: ')
                agree_contact()
            case "3":
                name = input('Introduce el nombre de contacto a actualizar: ')
                if name in agenda:
                    agree_contact()
                else:
                    print('Debes introducir un numero menor a 9 digitos')
            case "4":
                name = input('Ingresa el contacto a eliminar: ')
                if name in agenda:
                    del agenda[name]
                    print('Contacto eliminado correctamente !!!')
                else:
                    print('El contacto ingresado no existe, favor verificar. ')
            case "5":
                print('Saliendo del programa. ')
                break
            case _:
                print('Opcion no valida, favor elije una opción entre 1 y 5 ')

my_agenda()









