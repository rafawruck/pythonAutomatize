# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:32:12 2024

@author: Rafael Wruck
GitHub rafawruck
"""

name = input("Informe seu nome: ")
age = int(input("Informe sua idade: "))

if name == "Alice":
    print ("Oi, Alice.")
elif (age < 12):
    print ("Você não é Alice, garota")
elif (age < 100):
    print ("Você não é Alice, vovó")
elif (age > 2000):
    print ("Ao contrário de você, Alice não é uma vampira imortal e morta-viva ")

spam = 0
while (spam < 5):
    print ("Olá, mundo!")
    spam +=1
