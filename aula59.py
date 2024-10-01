# ============ Aula 59 ============

#Desempacotamento em chamadas
#Métodos e funções

'''
no desempacotamento podemos usar o for, mas a maneira mais simples que não gasta muitas linhas
é colocar um "*" na frente do valor que queremos imprimir
'''

string = 'ABCD'
lista = ['Mary','Hellena', 1,2 ,9,'Jones', 'Mark']
tupla = 'Python', 'é', 'Legal'

# a,b, *_ , c, d= lista
# print(a,c,sep=', ')

salas = [
    ['Maria', 'Helena'], # índice 0
    ['Eliaine'], # índice 1
    ['Elliza', 'John', 'Eduarda'], # índice 2
]

print(*salas, sep='\n')

