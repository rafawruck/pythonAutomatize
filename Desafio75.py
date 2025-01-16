# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:33:02 2025

@author: 215511
"""
tupla = False
while True:
    print ("-"*15)
    print ("{:^15}".format("MENU"))
    print ("-"*15)
    print (" {}".format("1 - Preencha a tupla."))
    print (" {}".format("2 - Número 9."))
    print (" {}".format("3 - Primeiro número 3."))
    print (" {}\n".format("4 - Quantidade de pares."))
    print (" {}".format("99 - SAIR"))
    print ()
    
    opção = int(input("Insira a opção desejada: "))
    print ()
    
    if opção == 1:
        print ("Você selecionou a opção 1")
        tuplaGerada = ((int(input("Insira um número entre 0 e 9: "))), 
                       (int(input("Insira um número entre 0 e 9: "))), 
                       (int(input("Insira um número entre 0 e 9: "))), 
                       (int(input("Insira um número entre 0 e 9: "))))
        print (f"Tupla gerada - a tupla gerada é {tuplaGerada}.")
        tupla = True
    
    
    elif opção == 2:
        print ("Você selecionou a opção 2")
        if tupla==True:
            nove = 0
            for i in tuplaGerada:
                if i == 9:
                    nove+=1
            print (f"Na tupla {sorted(tuplaGerada)} existe {nove} número(s) nove.")
        else:
            print ("A tupla não foi gerada, impossível apresentar.")
        
    
    elif opção == 3:
        print ("Você selecionou a opção 3")
        if tupla==True:
            pTres = 0
            if 3 in tuplaGerada:
                for i in range(len(tuplaGerada)):
                    if tuplaGerada[i] == 3:
                        pTres = i
                        break
                print (f"O primeiro número 3 está no posicão {pTres}")
                
            else:
                print (f"Na tupla {sorted(tuplaGerada)} não existe o número 3")
                
            
        else:
            print ("A tupla não foi gerada, impossível apresentar.")
    
    
    elif opção == 4:
        print ("Você selecionou a opção 4")
        if tupla==True:
            pares = 0
            for i in tuplaGerada:
                if i%2==0:
                    pares+=1
            print (f"Na tupla gerada {sorted(tuplaGerada)} existem {pares} número(s) pares")
        else:
            print ("A tupla não foi gerada, impossível apresentar.")
    
    
    elif (opção == 99):
        print ("Você selecionou a opção 99")
        print ("Script encerrando - bye!!!")
        break
    else:
        print ("Você selecionou uma oção invalida")