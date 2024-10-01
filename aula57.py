# ========= Lista dentro de Listas =========

salas = [
    ['Maria', 'Helena'], # índice 0
    ['Eliaine'], # índice 1
    ['Elliza', 'John', 'Eduarda'], # índice 2
]

'''
Para acessar o valor de uma sublista dentro de uma lista primeiro se coloca:

salas[1] o índice dela
salas[1][0] e em seguida seu valor
'''

# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é: {sala}')
    for aluno in sala:
        print(aluno)
