"""
    ProyectFactorial
    Author: Fabian Dario Florez Raigoso
    Emain: fabflorez@gmail.com
    Description: Este programa calcula el factorial
    de los 360° 
"""

class Funcion():
    def fFactorial(self,n):
        resultado = 1
        for i in range(1,n+1,1):
            resultado *= i 
        return resultado