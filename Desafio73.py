# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:58:31 2025

@author: 215511
"""
classificação = ["Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Vitória	", "Atlético-MG", "Fluminense", "Grêmio", "Juventude", "Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá	"]



while True:
    print ("-"*15)
    print ("{:^15}".format("MENU"))
    print ("-"*15)
    print (" {}".format("1 - Listar G +5."))
    print (" {}".format("2 - Listar G -4."))
    print (" {}".format("3 - Ordem alfabética."))
    print (" {}".format("4 - Posição por Time."))
    print (" {}\n".format("5 - Classificação atualizada."))
    print (" {}".format("99 - SAIR"))
    print ()
    
    opção = int(input("Insira a opção desejada: "))
    print ()
    if (opção == 1):
        print ("Você selecionou a opção 1")
        print ("Segue a listagem dos 05 primeiros colocados:")
        for i in range(5):
            print (f"{i+1}º - {classificação[i]}")
        
    elif (opção == 2):
        print ("Você selecionou a opção 2")
        print ("Segue a listagem dos 4 últimos colocados:")
        for i in range(16,20):
            print (f"{i+1}º - {classificação[i]}")
            
    elif (opção == 3):
        print ("Você selecionou a opção 3")
        print ("Segue a listagem em ordem alfabética:")
        for i in sorted(classificação):
            print (i)
        
    elif (opção == 4):
        print ("Você selecionou a opção 4")
        time = str(input("Digite o time solicitado: "))
        if time in classificação:
            print (f"O {time} está na classificação")
            for i in range(len(classificação)):
                if time == classificação[i]:
                    print ("O {} está na posição {}".format(time, i+1))
        else:
            print (f"O {time} não está na classificação")
    
    elif (opção == 5):
        print ("Você selecionou a opção 5")
        print ("Segue a Classificação atualizada:")
        for pos, times in enumerate(classificação):
            print (f"{pos} - {times}")
        
        
        
    elif (opção == 99):
        print ("Você selecionou a opção 99")
        print ("Script encerrando - bye!!!")
        break
    else:
        print ("Você selecionou uma oção invalida")
        