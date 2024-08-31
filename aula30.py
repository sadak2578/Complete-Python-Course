'''
CONSTANTE = "variáveis" são variáveis que nunca vão mudar

Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''
velocidade = 61 # velocidade em que o carro está
local_carro = 98 # local em que o carro está

RADAR1 = 60 # velocidade máxima do radar1
LOCAL1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 #a distância onde o radar 1 pega
velocidade_carro_passou_radar1 = velocidade > RADAR1
carro_passou_radar1 = local_carro >= (LOCAL1 - RADAR_RANGE) and    \
    local_carro <= (LOCAL1 + RADAR_RANGE) and velocidade_carro_passou_radar1
carro_multado_radar1 = carro_passou_radar1 and carro_passou_radar1

if velocidade_carro_passou_radar1:
    print('a velocidade do carro passou o radar 1')
if carro_passou_radar1:
    print('o carro passou do radar 1')
if carro_multado_radar1:
    print('O carro foi multado no radar 1')