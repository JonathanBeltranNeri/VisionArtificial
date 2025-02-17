##Jonathan Beltran Neri 22310188
##Tuplas
##Problema_3

# Definir la tupla de países favoritos
paises_fav_v = ("Japon", "Singapur", "EUA")

# Imprimir la tupla completa
print("Países que quiero visitar:", paises_fav_v)

# Ingresar un nuevo país
new_pais = input("Ingresa un país que quieras visitar: ")

# Verificar si el país ingresado está en la tupla
if new_pais in paises_fav_v:
    print(f"Genial, ¡también quieres visitar ",new_pais,"!")
else:
    print(f"Oh, quieres visitar ",new_pais," un país diferente.") 