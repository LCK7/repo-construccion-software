"""Calculadora de MCD y MCM con POO"""

import math
class Calculadora:
    """Calculadora"""
    def __init__(self):
        """Inicia el constructor"""
        self._numeros = []  # Atributo privado

    # Getter para los números
    @property
    def numeros(self):
        """Accede a los números"""
        return self._numeros

    # Setter para los números con validación simple
    @numeros.setter
    def numeros(self, valores):
        """valida la entrada de numeros"""
        if not valores:
            print("Error: La lista no puede estar vacía")
            return
        try:
            self._numeros = [int(num) for num in valores]
        except ValueError:
            print("Error: Solo se permiten números enteros")
            self._numeros = []

    def calcular_mcd(self):
        """Calcula el maximo comun divisor"""
        if not self._numeros:
            return 0

        resultado = self._numeros[0]
        for num in self._numeros[1:]:
            resultado = math.gcd(resultado, num)
        return resultado

    def calcular_mcm(self):
        """Calcula el minimo comun multiplo"""
        if not self._numeros:
            return 0

        resultado = self._numeros[0]
        for num in self._numeros[1:]:
            if resultado == 0 or num == 0:
                return 0
            resultado = resultado * num // math.gcd(resultado, num)
        return resultado

def main():
    """Principal"""
    print("CALCULADORA MCD/MCM CON POO")
    print("--------------------------")
    calc = Calculadora()

    while True:
        # Pedir números
        entrada = input("\nIngresa números separados por espacios: ").strip()

        # Usar el setter para asignar números
        calc.numeros = entrada.split()  # Esto llama automáticamente al setter

        # Si la lista quedó vacía por error, volver a pedir
        if not calc.numeros:  # Esto llama al getter
            continue

        # Calcular y mostrar (usando los getters)
        print(f"\nNúmeros ingresados: {calc.numeros}")
        print(f"MCD: {calc.calcular_mcd()}")
        print(f"MCM: {calc.calcular_mcm()}")

        # Preguntar por otra operación
        if input("\n¿Calcular otros números? (s/n): ").lower() != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
