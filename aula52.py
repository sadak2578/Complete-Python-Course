# ========================== Tuplas em python ==========================
'''
o que é um tupla? 
em python tupla é uma lista imutável
'''
'''
exemplo de tupla:
_,nome2, *_ = ['Sadak', 'Millena', 'Robert', 'Carl']

 print(nome2)

'''


nomes = ['Maria','Helena',' Luiz']
nomes = tuple(nomes) #converte listas em tuplas
print(nomes[-1])
print(nomes, type(nomes), sep='|')

if nomes is not False: #inverso do anterior
    nomes = list(nomes) #converte listas em tuplas
    print(nomes[-2])
    print(nomes, type(nomes), sep='|')




    