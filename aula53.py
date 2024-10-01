# ====================== Aula 53 ======================

'''
Enumerate - enumerar itens de uma lista ou de uma tupla
'''
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')] 
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada, end=' ')

for indice, nome in enumerate(lista):
    print(indice,nome)
'''
 for tupla_enumerada in enumerate(lista):
    print('For da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

esse código é a mesma coisa que o código a cima, porém o código acima é mais fácil do q este código robusto
'''    


