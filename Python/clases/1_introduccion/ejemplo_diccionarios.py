#diccionarios:
print('-'*10)
dic = {'llave1': 1,'llave2':'string1'}
print('Diccionario:', dic)
#podemos acceder a los valores
#guardados en cada llave como sigue:
print('valor guardado en la llave1:', dic['llave1'])
print('valor guardado en la llave2:',dic['llave2'])

#imprimimos las llaves
print('llaves del diccionario:',dic.keys())
#imprimimos los valores:
print('valores del diccionario:', dic.values())
#añadimos entradas a un diccionario 
#con:
dic['llave3'] = -34
print('añadiendo pareja llave-valor al diccionario:',dic)
