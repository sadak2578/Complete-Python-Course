for i in range(10):
    if i == 0:
        print('seu i é igual a zero, pulando...')
        continue

    if i == 2:
        print(' i é igual a 2, pulando...')
        continue
    if i == 3:
        print('seu i é igual a três, pulando....')
        continue
    if i == 8:
        print('seu i é igual a 8, pulando....')
        continue
    if i == 9:
        print('Seu i é igual a 9, pulando para o final....')
        continue
    
    for  j in range(1,10):
        for k in range(1,10):
            print(i,j,k)


else:
    print('Laço FOR completo com sucesso...')