# Diccionario de amigos y sus edades
Amigos_inf = {
    "Pedro": 23,
    "Pablo": 20,
    "Joel": 21,
    "Alan": 20
}

# Imprimir los amigos y sus edades
print("Mis amigos son:\n")
for clave, valor in Amigos_inf.items():
    print(f"{clave} y su edad es: {valor}")

# Preguntar al usuario si desea actualizar la edad
new_edad = input("¿Quieres actualizar la edad de uno de tus amigos? (Sí o No): ")

if new_edad.lower() == "si":  # Convertimos a minúsculas para no tener problemas con mayúsculas
    nombre_amigo = input("Ingresa el nombre de tu amigo: ")
    
    if nombre_amigo in Amigos_inf:
        nueva_edad = int(input(f"¿Cuál es la nueva edad de {nombre_amigo}? "))
        Amigos_inf[nombre_amigo] = nueva_edad
        print(f"La edad de {nombre_amigo} ha sido actualizada a {nueva_edad}.")
    else:
        print(f"No tienes un amigo llamado {nombre_amigo}.")
else:
    print("No se actualizará ninguna edad.")

# Imprimir los amigos y sus nuevas edades
print("\nLista actualizada de amigos:")
for clave, valor in Amigos_inf.items():
    print(f"{clave} y su edad es: {valor}")
