# ============ Aula sobre ID ============
'''
Flag (Bandeira) => Ele marca um local
None = não é um valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
''' 

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('não faça algo')

if passou_no_if is None:
    print('ele não passou no if')
if passou_no_if is not None:
    print('ele passou no if')


