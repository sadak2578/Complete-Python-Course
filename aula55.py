
'''
round() em python: 


Quando o número de casas decimais do round for None ele exibe apenas 1

print(round(numero_3,None)) # citado no comentário acima
'''
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(round(numero_3,2))
