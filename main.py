# Questão 2, importações
import pygame
from pygame.locals import *
from mecanica import *
from visual import *
import visual
# 3 inicializações
janela = inicializar_jogo()
inicializar_musica()

carro = inicializar_carro('jogador')
carro2 = inicializar_carro('oponente')
carro_loc = posicionar_carro(carro, FAIXA_DIREITA, int(0.8 * JANELA_ALTURA))
carro2_loc = posicionar_carro(carro2, FAIXA_ESQUERDA, int(0.2 * JANELA_ALTURA))
contador = 0
velocidade = 1

esta_executando = True

# loop de jogo
while esta_executando:

  # Questão 5, item 
  
  carro2_loc =  mover_adversario_aleatoriamente(carro2_loc, velocidade)
 
 

  # esse trecho verifica se houve eventos de entrada (mouse, teclado)
  for event in pygame.event.get():
    if event.type == QUIT:
      esta_executando = False

    # Questão 6
    if event.type == KEYDOWN:
      if event.key == K_a or event.key == K_LEFT:
        alternar_faixa(carro_loc, FAIXA_ESQUERDA)
      if event.key == K_d or event.key == K_RIGHT:
        alternar_faixa(carro_loc, FAIXA_DIREITA)


  # redesenha elementos na janela
  visual.desenhar_estrada(janela)
  # Questão 4
  visual.desenhar_carros(janela, [[carro, carro_loc], [carro2, carro2_loc]])
  visual.atualizar_tela()
  
  # Questão 7, item 2
  bateu = houve_colisao(carro_loc, carro2_loc)
  if bateu:
    print("GAME OVER!")
    break
  
  # Questão 8, itens 2 e 3
  if contador == 5000:
    velocidade = subir_nivel(velocidade)
    contador = 0
  contador += 1

# Questão 9
encerrar_jogo()