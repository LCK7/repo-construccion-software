import math
from functools import reduce
from typing import List

def calcular_mcd(a: int, b: int) -> int:
    """Calcula el MCD de dos números usando el algoritmo de Euclides."""
    return math.gcd(a, b)

def calcular_mcm(a: int, b: int) -> int:
    """Calcula el MCM de dos números usando la relación con el MCD."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // calcular_mcd(a, b)

def mcd_lista(numeros: List[int]) -> int:
    """Calcula el MCD para una lista de números."""
    return reduce(calcular_mcd, numeros)

def mcm_lista(numeros: List[int]) -> int:
    """Calcula el MCM para una lista de números."""
    return reduce(calcular_mcm, numeros)

def ingresar_numeros() -> List[int]:
    """Solicita al usuario ingresar números y los devuelve como lista de enteros."""
    while True:
        entrada = input("Ingrese números enteros separados por espacios: ").strip()
        if not entrada:
            print("No se ingresaron números. Intente nuevamente.")
            continue
            
        try:
            numeros = [int(num) for num in entrada.split()]
            if len(numeros) < 1:
                print("Debe ingresar al menos un número.")
                continue
            return numeros
        except ValueError:
            print("Error: Solo se permiten números enteros. Intente nuevamente.")

def main():
    print("Calculadora de MCD (Máximo Común Divisor) y MCM (Mínimo Común Múltiplo)")
    print("-----------------------------------------------------------------------")
    
    numeros = ingresar_numeros()
    
    # Calcular MCD
    resultado_mcd = mcd_lista(numeros)
    
    # Calcular MCM (solo si todos los números son diferentes de cero)
    if all(num != 0 for num in numeros):
        resultado_mcm = mcm_lista(numeros)
    else:
        resultado_mcm = 0  # El MCM es cero si algún número es cero
    
    print(f"\nPara los números {numeros}:")
    print(f"- MCD (Máximo Común Divisor): {resultado_mcd}")
    print(f"- MCM (Mínimo Común Múltiplo): {resultado_mcm}")

if __name__ == "__main__":
    main()