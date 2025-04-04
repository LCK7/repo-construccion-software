"""Aplicacion que calcula el inverso de un número"""
class ExceptionNumero0(Exception):
    """Excepcion de division entre 0"""
try:
    x = float(input("Numero: "))
    if x == 0:
        raise ExceptionNumero0
    inverso = 1/x
    print(f"El valorn inverso es: {inverso}")
except ValueError:
    print("Ingrese un numero valido!!!")
except ZeroDivisionError:
    print("Ingrese un valor diferente de 0!!!")
else:
    print("Se presentó un error")
finally:
    print("Fin de la aplicacion ^^")
