import pygame

IMAGEM_FUNDO = pygame.image.load('arquivos/FundoPronto.jpg')

IMAGEM_PEDRA = pygame.image.load('arquivos/jankenpon_pedra.png')

IMAGEM_PAPEL = pygame.image.load('arquivos/jankenpon_papel.png')

IMAGEM_TESOURA = pygame.image.load('arquivos/jankenpon_tesoura.png')

IMAGEM_X = pygame.image.load('arquivos/X_cental.png')
IMAGEM_NOME_JOGADOR = pygame.image.load('arquivos/jogador_texto.png')
IMAGEM_NOME_MAQUINA = pygame.image.load('arquivos/maquina_texto.png')
OUTRAS_IMG = pygame.image.load('arquivos/outras.png')

ESCOLHA = pygame.image.load('arquivos/escolhadojogador.png')
IMAGEM_FUNDO_Y = pygame.image.load('arquivos/barraver.png')
IMAGEM_FUNDO_X = pygame.image.load('arquivos/barrahor.png')

CONTROLA_ESCOLHA = 0

pontuacao1_img = pygame.image.load('arquivos/Imagem0.png')
pontuacao2_img = pygame.image.load('arquivos/Imagem0.png')
armazena_escolha = False
conta_vitoria = 0
conta_derrota = 0
maquina_escolheu = None

loop = True
