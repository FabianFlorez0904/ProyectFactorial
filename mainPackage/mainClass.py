"""
    ProyectFactorial
    Author: Fabian Dario Florez Raigoso
    Emain: fabflorez@gmail.com
    Description: Este programa calcula el factorial
    de los 360° 
"""

import sys
sys.path.append("..")

from funcionesPackage.funcionClass import *

def main():
    f = Funcion()
    for i in range(361):
        print("{}° {}".format(i,f.fFactorial(i)))

main()