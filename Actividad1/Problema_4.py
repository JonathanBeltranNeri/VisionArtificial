class BankAccount:
    # Constructor de la clase BankAccount
    def __init__(self, nom, amount):
        self.nom = nom  # El nombre del titular de la cuenta
        self.amount = int(amount)  # El saldo inicial de la cuenta convertido a entero
        print(f"Bienvenid@: {self.nom}\nCuentas con un saldo de: {self.amount}.")

    # Método para realizar un depósito
    def deposit(self):
        new_deposit = int(input("Ingresa la cantidad que deseas agregar al saldo: "))  # Solicita al usuario la cantidad a depositar
        self.amount += new_deposit  # Aumenta el saldo de la cuenta con el depósito
        print(f"Has depositado {new_deposit}. El saldo actual es: {self.amount}.")  # Muestra el saldo actualizado después del depósito

    # Método para realizar un retiro
    def withdraw(self):
        withdraw_amount = int(input("Ingresa la cantidad que deseas retirar: "))  # Solicita al usuario la cantidad a retirar
        if self.amount - withdraw_amount >= 0:  # Verifica si hay suficiente saldo para el retiro
            self.amount -= withdraw_amount  # Resta el saldo de la cuenta con el monto retirado
            print(f"Has retirado {withdraw_amount}. El saldo actual es: {self.amount}.")  # Muestra el saldo actualizado después del retiro
        else:
            print("No tienes suficiente saldo para retirar esa cantidad.")  # Mensaje si no hay saldo suficiente

    # Método para obtener el saldo actual
    def get_balance(self):
        return self.amount  # Retorna el saldo actual de la cuenta


# Crear una instancia de BankAccount
P1 = BankAccount("Jonathan", 100)  # Crea una cuenta con el nombre "Jonathan" y un saldo inicial de 100

# Realizar operaciones (depositar y retirar)
P1.deposit()   # Llama al método deposit para agregar dinero a la cuenta
P1.withdraw()  # Llama al método withdraw para retirar dinero de la cuenta

# Ver el saldo final
print(f"El saldo final de {P1.nom} es: {P1.get_balance()}.")  # Muestra el saldo final de la cuenta
