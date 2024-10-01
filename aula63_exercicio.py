# ============= Exercício3 final do primeiro módulo =============
import re
import sys 



entrada = input('CPF [746.824.890-70]: ')




cpf_enviado_usuário = re.sub(
    #vai substituir tudo que não for um número: 
    r'[^0-9]', '', 
    entrada
    
    
)
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('você enviou dados sequenciais')
    sys.exit()


nove_digitos_1 = cpf_enviado_usuário[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos_1:
    resultado_digito_1 += int(digito_1) * int(contador_regressivo_1)
    contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0


nove_digitos_2 = cpf_enviado_usuário[:9] + '7'
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito_2 in nove_digitos_2:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    
    contador_regressivo_2 -= 1
    
    
digito_2 = ((resultado_digito_2 * 10) % 11)
digito_2 = digito_2 if digito_2 > 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos_1}{digito_1}{digito_2}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuário:
    print(f'CPF [{cpf_enviado_usuário}]:  é válido')
else:
    print('CPF não é válido')
