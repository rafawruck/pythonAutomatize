# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:28:54 2025

@author: Rafael Wruck
"""
def fim():
    global loop
    print ("Você selecionou a opção - 99")
    print ("Encerando o script")
    loop = False

def imprimir():
    global numeros
    if len(numeros) == 0:
        print ("Lista vazia, sem valores para imprimir")
    else:
        print ("Você selecionou a opção - 02")
        print ("Lista do numeros inseridos:")
        for c, v in enumerate(numeros):
            print (f"Na posicão {c} o número correspondente é: {v}")
        linha()
        print (f"Lista {numeros}")
    

def inserir():
    global numeros
    print ("Você selecionou a opção - 01")
    while True:
        num = int(input("Numero a ser inserido [0 para parar]: "))
        if num == 0:
            break
        elif num not in numeros:
            numeros.append(num)
            numeros.sort()


def opções():
    op = int(input("Digite a opção desejada: "))
    linha()
    if op == 1:
        inserir()
    elif op==2:
        imprimir()
    elif op==99:
        fim()
    else:
        print ("Opção não válida - tente novamente")
    

def linha():
    print ("*"*25)

def menu():
    linha()
    print ("{:^25}".format("MENU"))
    linha()
    print ("  {}".format("1 - Cadastrar números"))
    print ("  {}".format("2 - Imprimir números"))
    linha()
    print ("  {}".format("99 - SAIR"))
    print ()
    opções()
    
    
    
    
numeros = []
loop = True
while loop:
    menu()