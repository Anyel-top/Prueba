def suma():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")

if __name__ == "__main__":
    suma()
