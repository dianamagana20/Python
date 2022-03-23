diccionaro = dict()
dic = {'edad':28,'nombre':'diana'}
print(dic.keys()) #imprime las claves
print(dic.values()) #imprime los valores

for k in dic.keys():
    print(dic[k]) #el ciclo imprime los valores

for k,i in dic.items (): #imprime la clave y el valor
    print(f'llave: {k} \n valor {i}')

#Aplicando Tuplas

for k in dic.items():
    print (f'llave: {k[0]} \n valor: {k[1]}')
