# ======== Calculadora com While ========

while True:
    
    #definindo as variáveis
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+,-, /, *):  ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    resultado_num = 0
    
    #define os erros gerados
    try:
        # Converte os inputs em floats
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        #verifica se os números válidos são verdadeiros
        numeros_validos = True
    except:
        #aqui é caso os números não forem válidos
        numeros_validos = None
        
    #caso os números não sejam válidos e sejam None, cai aqui e o programa apenas continua
    if numeros_validos is None:
        print('Os caracteres digitados não são válidos') 
        continue
    
    #esse define os caracteres que são permitidos, e não são todos
    operadores_permitidos = '+-/*'
    
    #Este define o número de caracteres que serão usados
    if len(operador) > 1:
        print('digite apenas um operador')
        continue
    #aqui utiliza dos caracteres que não estão entre os permitidos
    #para ver os que não estão entre utiliza-se o not in
    if operador not in operadores_permitidos:
        print('Os operadores ou um dos operadores permitidos não é permitido')
        continue
    
    #calculos feitos pela calculadora
    if operador == '+':
        resultado_num = num_1_float + num_2_float 
        print(f'A soma entre: {num_1_float:.0f} + {num_2_float:.0f} = {resultado_num:.0f}')
    elif operador == '-':
        resultado_num = num_1_float - num_2_float 
        print(f'A subtração entre: {num_1_float:.0f} - {num_2_float:.0f} = {resultado_num:.0f}')
    elif operador == '/':
        resultado_num = num_1_float / num_2_float 
        print(f'A divisão entre: {num_1_float:.0f} / {num_2_float:.0f} = {resultado_num:.0f}')
    elif operador == '*':
        resultado_num = num_1_float * num_2_float 
        print(f'A multiplicação entre: {num_1_float:.0f} x {num_2_float:.0f} = {resultado_num:.0f}')
    else:
        print('este código não deve cehgar aqui')
    
    #parte de sair
    sair = input('Quer sair?: [s/n] ').lower().startswith('s')
    
    #parte final do código :D
    if sair is True:
        break
