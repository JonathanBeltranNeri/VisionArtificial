##Jonathan Beltran Neri 22310188
##Listas
##Problema_1
# Lista inicial de libros
Fav_books = [ ]
# Agregar libros a la lista
Fav_books.append("Los Juegos del Hambre")
Fav_books.append("La quinta ola")
Fav_books.append("Narnia")
Fav_books.append("Jumper")
Fav_books.append("Maze Runner")
# Imprimir libros actuales
print("Mis libros favoritos:")
for libro in Fav_books:
    print(libro)

# Agregar un nuevo libro
new_books = input("Agrega tu libro favorito: ")
Fav_books.append(new_books)  # Agregar el libro a la lista

# Imprimir la lista después de agregar el nuevo libro
print("\nLista de libros después de agregar uno nuevo:")
for libro in Fav_books:
    print(libro)
