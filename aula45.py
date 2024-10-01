# ============ Como o for funciona ============
'''
iterável => str, range, etc => chamase de iterável pois dentro dele temos um método chamado (__iter__)
iterador => aquele que irá intregar um valor por vez
next => irá entregar o próximo valor
inter => me entregue seu iterador
'''
#for letra in texto
texto = 'Sadak' # iterável
iterador = iter(texto) # iterator


'''
Isso é o que acontece por baixo dos panos, é exatamente a mesma coisa do for
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
'''

