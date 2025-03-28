#EJERCICIO: DETERMINA EL MAYOR DE 3 NÚMEROS INGRESADOS POR EL TECLADO

class ordenadorNumeros:
    
    def __init__(self,numero1=0,numero2=0,numero3=0):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3
    
    def intercambio1(self,numero1,numero2):
        temporal = numero1
        numero1 = numero2
        numero2 = temporal
        return(numero1,numero2)
    
    def ingresarnum(self):
        self.numero1 = int(input("Ingresa el primer numero: "))
        self.numero2 = int(input("Ingresa el segundo numero: "))
        self.numero3 = int(input("Ingresa el tercer numero: "))
    
    def ordenarnum(self):
        if self.numero1 > self.numero2:
            self.numero1,self.numero2 = self.intercambio1(self.numero1,self.numero2)

        if self.numero2 > self.numero3:
            self.numero2,self.numero3 = self.intercambio1(self.numero2,self.numero3)
            
        if self.numero1 > self.numero2:
            self.numero1,self.numero2 = self.intercambio1(self.numero1,self.numero2)
    
    def imprimirnum(self):
        print(f"Numeros ordenados {self.numero1,self.numero2,self.numero3}")
        print(f"El mayor es: {self.numero3}")
        
if __name__ =="__main__":
    
    ordenador = ordenadorNumeros()
    
    ordenador.ingresarnum()
    ordenador.ordenarnum()
    ordenador.imprimirnum()
    
    
    