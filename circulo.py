class Circulo:
    PI = 3.1416
    def __init__(self,radio):
        self.radio = radio

def circunferencia(self):
    return 2*self.PI*self.radio 

if __name__ == "__main__":
    instancia_circulo = Circulo()
    print(f"La circunferencia es: {instancia_circulo.circunferencia}")