# ============= Aula 60 de Python =============
'''
Operação ternária (condicional de uma linha)

<valor> if <condição> else <outro valor>
'''
# condição = 10 == 10
# variavel =  'Verdadeiro 10 é igual a 10' if condição else f'Falso, numero não verdeiro'
# print(variavel)

# digito = 9
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('Valor' if not True else 'Outro Valor' if  not True else 'Fim')