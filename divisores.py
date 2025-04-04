"""Programa que calcule los divisores con excepciones"""
def calcular_divisores():
    """Funcion calcular divisores para reutilizar el codigo"""
    try:
        x = int(input("Ingrese un numero entero: "))
        if x > 0:
            print(f"Los divisores de {x} son: ")
            for i in range(1,x+1):
                if x % i == 0:
                    print(i)
        else:
            print("No tiene ningun divisor")
    except ValueError as ve:
        print(f"Ingrese un valor valido!! {ve}")
    finally:
        print("Operación completa, Gracias por usar el programa")
if __name__ == "__main__":
    calcular_divisores()
