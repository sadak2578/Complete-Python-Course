from time import sleep

qtd_linhas = 5
qtd_colunas = 5

linhas = 1

while linhas <= qtd_linhas:
    
    coluna = 1
    
    
    while coluna <= qtd_colunas:
        coluna += 1
        print(f'{linhas=} {coluna=}')



    
    
    linhas += 1


sleep(0.5)
print('Acabou!')