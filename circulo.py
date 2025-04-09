class Circulo:
    PI = 3.1416
    
    def __init__(self,radio):
        self.radio = radio

    def circunferencia(self):
        return 2*self.PI*self.radio

    def area(self):
        return self.PI * self.radio * self.radio

if __name__ == "__main__":
    circulo = Circulo(10)
    print(f"La circunferencia es: {circulo.circunferencia()}")
    print(f"El area del circulo es: {circulo.area()}")
    