# ==================== Estruturas de Repetições ==================== 

'''

'''
from time import sleep
contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        continue

    
    sleep(1)
    print(f'{contador}....', end=' ')

    
    
    if contador == 12:
        break
   
sleep(1)
print('FIM DO PROGRAMA!!!! :D')
