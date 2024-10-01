# ==================== while/else ====================

string = 'UmValorQualquer'

i = 0

while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break

    print(letra, end='')
    i += 1
else:
    print('\nNão encontrei um espaço na string') #é executado quando o while for executado completamente

print('Fora do while')
    
    