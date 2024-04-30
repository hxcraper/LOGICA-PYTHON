"""
OPERACIONES CON CADENAS
"""

s1= "Hola"
s2= "Python"

# Concatenación
print(s1 + " " + s2 + " ! ! !")

# Repetición
print (s1 + s1 + s1)
print(s1*3)

#Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

#Longitud de una cadena de texto
print(len(s2))

# Slicing(Porción)
print(s2[2:5])
print(s2[2:])
print(s2[:2])
print(s2[0:2])

# Busqueda
print("a" in s1)
print("i" in s1)

#Reemplazo
print(s1.replace("o", "a")) #Reemplazamos la o por el a en "Hola"

#División de caracteres
print(s2.split('t'))

# Mayusculas y Minusculas
print(s1.upper())
print(s2.lower())
print('enrique burotto'.title()) # Primera en mayusculas como titulo
print('enrique burotto'.capitalize()) # Primera en mayusculas

# Eliminzación de espacios al principio y final
print("             enrique burotto               ".strip()) 

# Busqueda al principio y final
print(s1.startswith('ho'))
print(s1.startswith('la'))
print(s2.endswith('thon'))
print(s2.endswith('py'))

# Busqueda por posición

s3= "Enrique Burotto @burottokikedev"

print(s3.find("Posición"))
print(s3.find("B"))
print(s3.find("Ó"))
print(s3.lower().find("o"))

#Busqueda de ocurrencias

print(s3.lower().count("burotto")) # me cuenta cuantas veces tengo burotto ya sea may o min

# Formateo
print("Saludo: {} , lenguaje: {}!".format(s1,s2))

# Interpolación
print(f"Saludo: {s1} , lenguaje: {s2}!")

# Transformación en lista de caracteres 
print(list(s3))

# Transformación de lista de cadena
li = [s1, " , ", s2, "!"]
print("".join(li))

# Transformación numerica
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "12354.123124"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
EXTRA
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

def check(word1: str, word2: str):

    # Palindromos
    print(f'¿{word1} es un palindromo?: {word1 == word1[::-1]}')
    print(f'¿{word2} es un palindromo?: {word2 == word2[::-1]}')

    # Anagramas
    print(f'¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}')


check("radar", "python")
check("amor", "roma")

