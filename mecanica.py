import random
from visual import FAIXA_ESQUERDA, FAIXA_DIREITA, JANELA_ALTURA

VEICULO_ALTURA = 250

def alternar_faixa(carro_posicao, faixa):
  carro_posicao.center = (faixa, carro_posicao.center[1])

# Questão 5, item 1
def mover_adversario_aleatoriamente(carro_posicao, velocidade):
  carro_posicao[1] += velocidade  
  if carro_posicao[1] > JANELA_ALTURA:  
   carro_posicao[1] = -VEICULO_ALTURA
   faixa = random.randint(0, 1)
   if faixa == 1:
     alternar_faixa(carro_posicao, FAIXA_DIREITA)
    
   elif faixa == 0:
     alternar_faixa(carro_posicao, FAIXA_ESQUERDA)
     
  return carro_posicao
   #movimento = random.choice(['esquerda', 'direita'])
   #if movimento == 'esquerda':
   #     carro_posicao.centerx -= velocidade
   #elif movimento == 'direita':
       # carro_posicao.centerx += velocidade

  # Questão 5, itens 3, 4 e 5
pass # remova esse comando e escreva seu codigo
  

# Questão 7, item 1
def houve_colisao(carro_posicao, carro2_posicao):
  if carro_posicao[0] == carro2_posicao[0] and carro_posicao[1] -VEICULO_ALTURA <= carro2_posicao[1]:
    return True
  else:
    return False
 # pass  remova esse comando e escreva seu codigo

# Questão 8, item 1
def subir_nivel(velocidade):
  velocidade = velocidade + 0.5
  print("Subir nível - Velocidade:", velocidade)
  return velocidade
  pass # remova esse comando e escreva seu codigo