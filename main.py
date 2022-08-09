import pygame
import variaveis
import random
from time import sleep

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Jokenpow')
pygame.mixer.music.load('arquivos/jogou.wav')


def controla_escolha_do_jogador_e_maquina():

    if variaveis.armazena_escolha:
        escolha_maquina = random.randint(1, 3)
        variaveis.maquina_escolheu = escolha_maquina

        if escolha_maquina == 1 and variaveis.CONTROLA_ESCOLHA == 2:
            variaveis.conta_vitoria += 1
        elif escolha_maquina == 1 and variaveis.CONTROLA_ESCOLHA == 3:
            variaveis.conta_derrota += 1
        elif escolha_maquina == 2 and variaveis.CONTROLA_ESCOLHA == 1:
            variaveis.conta_derrota += 1
        elif escolha_maquina == 2 and variaveis.CONTROLA_ESCOLHA == 3:
            variaveis.conta_vitoria += 1
        elif escolha_maquina == 3 and variaveis.CONTROLA_ESCOLHA == 1:
            variaveis.conta_vitoria += 1
        elif escolha_maquina == 3 and variaveis.CONTROLA_ESCOLHA == 2:
            variaveis.conta_derrota += 1

        variaveis.armazena_escolha = False
    else:
        pass

def desenha_na_tela():

    tela.blit(variaveis.IMAGEM_FUNDO, (0, 0))
    tela.blit(variaveis.IMAGEM_FUNDO_Y, (490, 0))
    tela.blit(variaveis.IMAGEM_FUNDO_Y, (0, 0))
    tela.blit(variaveis.IMAGEM_FUNDO_X, (0, 390))
    tela.blit(variaveis.ESCOLHA, (30, 395))
    tela.blit(variaveis.pontuacao1_img, (95, 280))
    tela.blit(variaveis.pontuacao2_img, (330, 280))
    tela.blit(variaveis.IMAGEM_X, (190, 150))
    tela.blit(variaveis.IMAGEM_NOME_JOGADOR, (70, 55))
    tela.blit(variaveis.IMAGEM_NOME_MAQUINA, (320, 55))
    tela.blit(variaveis.OUTRAS_IMG, (130, 390))
    testa_desenho_e_escolhe()

def testa_desenho_e_escolhe():

    if variaveis.CONTROLA_ESCOLHA == 1:
        tela.blit(variaveis.IMAGEM_PEDRA, (20, 95))
    elif variaveis.CONTROLA_ESCOLHA == 2:
        tela.blit(variaveis.IMAGEM_PAPEL, (20, 82))
    elif variaveis.CONTROLA_ESCOLHA == 3:
        tela.blit(variaveis.IMAGEM_TESOURA, (20, 80))

    if variaveis.maquina_escolheu == 1:
        tela.blit(variaveis.IMAGEM_PEDRA, (280, 95))
    elif variaveis.maquina_escolheu == 2:
        tela.blit(variaveis.IMAGEM_PAPEL, (280, 82))
    elif variaveis.maquina_escolheu == 3:
        tela.blit(variaveis.IMAGEM_TESOURA, (280, 80))

    if variaveis.conta_vitoria > 9 or variaveis.conta_derrota > 9:
        variaveis.conta_vitoria = 0
        variaveis.conta_derrota = 0

    variaveis.pontuacao1_img = pygame.image.load("arquivos/imagem" + str(variaveis.conta_vitoria) + ".png")
    variaveis.pontuacao2_img = pygame.image.load("arquivos/imagem" + str(variaveis.conta_derrota) + ".png")


while variaveis.loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            variaveis.loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_1:
                pygame.mixer.music.play()
                sleep(1)
                variaveis.CONTROLA_ESCOLHA = 1
                variaveis.armazena_escolha = True
            elif events.key == pygame.K_2:
                pygame.mixer.music.play()
                sleep(1)
                variaveis.CONTROLA_ESCOLHA = 2
                variaveis.armazena_escolha = True
            elif events.key == pygame.K_3:
                pygame.mixer.music.play()
                sleep(1)
                variaveis.CONTROLA_ESCOLHA = 3
                variaveis.armazena_escolha = True

    controla_escolha_do_jogador_e_maquina()
    desenha_na_tela()
    pygame.display.update()
