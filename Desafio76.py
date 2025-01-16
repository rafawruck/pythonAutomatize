# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:04:48 2025

@author: 215511
"""
tuplaFinal = ()
while True:
    print ("-"*15)
    print ("{:^15}".format("MENU"))
    print ("-"*15)
    print (" {}".format("1 - Adicionar itens."))
    print (" {}\n".format("2 - Listar itens."))
    print (" {}".format("99 - SAIR"))
    print ()
    opção = int(input("Insira a opção desejada: "))
    print ()
    
    if opção == 1:
        print ("Você selecionou a opção 1")
        while True:
            adiciona = str(input("Quer adicionar um item [S/sim - N/não]:")).upper()
            if adiciona == "S":
                a = (str(input("Nome do produto: ")),float(input("Preço do produto R$ ")))
                print()
                tuplaFinal += a
            else:
                print ("Tupla finalizada.")
                break
    
    elif opção == 2:
        print ("Você selecionou a opção 2")
        print ("-"*30)
        print ("{:^30}".format("LISTAGEM DE PREÇO"))
        print ("-"*30)
        for i in range(0,len(tuplaFinal),2):
            print (f"{tuplaFinal[i]} ---- {tuplaFinal[i+1]}")
            
        
        
    
    
    
    
    
    
    
    
    elif (opção == 99):
        print ("Você selecionou a opção 99")
        print ("Script encerrando - bye!!!")
        break
    else:
        print ("Você selecionou uma oção invalida")