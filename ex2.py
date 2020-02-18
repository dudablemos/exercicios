#2
dic={1:"domingo",2:"segunda",3:"terça",4:"quarta",5:"quinta",6:"sexta",7:"sabado"}
print(dic)
numero=int(input("Digite um numero: "))

if numero in dic.keys():
    print(dic[numero])
else:
    print ("numero invalido")