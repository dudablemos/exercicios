#3
import random as rd

itens=int(input("insira quantos itens vocẽ quer na lista: "))
contador = 0
lista = []
while contador<itens:
    lista.append(rd.randrange(0,1000))
    contador+=1
print(lista)
print('o maior numero é:', max(lista))
print('o menor numero é:', min(lista))