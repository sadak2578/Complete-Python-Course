# =============================== Operador OR =============================== 

'''
No OR, se tivermos um valor Verdadeiro e o outro valor for falso
ele irá avaliar somento o verdadeiro, já se tivermos inúmeros valores falsos e o último
for verdadeiro, ele irá avaliar somente o último valor, assim seria se tivessemos
4 valors, o primeiro sendo falso, o segundo verdadeiro e os outros dois ultimos sendo
falso, ele iria avaliar somente o segundo valor, e iria parar nele, despresando os valores falsos
''' 

# entrada = input('[E]ntrar ou [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('você entrou no programa')
# else:
#     print('você saiu do programa')


# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'

print(senha)
