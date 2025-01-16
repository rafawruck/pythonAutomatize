# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:45:00 2025

@author: 215511
"""
import random
tupla = False

while True:
    print ("-"*15)
    print ("{:^15}".format("MENU"))
    print ("-"*15)
    print (" {}".format("1 - Gere os números."))
    print (" {}".format("2 - Mostrar os números."))
    print (" {}\n".format("3 - Menor e Maior número."))
    print (" {}".format("99 - SAIR"))
    print ()
    
    opção = int(input("Insira a opção desejada: "))
    print ()
    
    if opção == 1:
        print ("Você selecionou a opção 1")
        tuplaGerada = ((random.randint(1,100)), (random.randint(1,100)), (random.randint(1,100)), (random.randint(1,100)), (random.randint(1,100)))
        print ("Tupla gerada")
        tupla=True
        
    elif opção == 2:
        print ("Você selecionou a opção 2")
        if tupla==True:
            print ("A tupla gerada é: {}".format(sorted(tuplaGerada)))
        else:
            print ("A tupla não foi gerada, impossível apresentar.")
            
    elif opção == 3:
        print ("Você selecionou a opção 3")
        if tupla==True:
            print (f"Na tupla {tuplaGerada}")
            maior = 0
            menor = 101
            for i in tuplaGerada:
                if i > maior:
                    maior = i
                if i < menor:
                    menor = i
            print (f"O menor número na tupla {sorted(tuplaGerada)} é {menor}.")
            print (f"O menor número na tupla {sorted(tuplaGerada)} é {maior}.")
        else:
            print ("A tupla não foi gerada, impossível apresentar.")
    
    elif (opção == 99):
        print ("Você selecionou a opção 99")
        print ("Script encerrando - bye!!!")
        break
    else:
        print ("Você selecionou uma oção invalida")