from src import functions
#Configurações da tela
import pygame
from pygame.locals import *

LARGURA_TELA = 800
ALTURA_TELA = 650
TAMANHO_CELULA = 50 
OFFSET_X = 150
OFFSET_Y = 80

#cores (RGB)

BRANCO = (255,255,255)
PRETO = (0,0,0)
AMARELO = (255,255,0)
ROXO = (255,0,255)
CINZA_CLARO = (224,224,224)
AZUL_MARINHO = (51,51,255)
AZUL_CLARO = (51,255,255)
navios_jogador1 = 7
navios_jogador2 = 7
#estados do jogo
ESTADO_POSICIONANDO = 0 # tela de posicionamento de navios
ESTADO_JOGANDO = 1 # jogo acontecendo
ESTADO_FIM = 2 #Jogo encerrado, alguem ganhou


#estados da célula

AGUA = 0 #AGUA NÃO ATACADA
NAVIO = 1 #NAVIO NAO ATACADO
AGUA_ATACADA = 2 #TIRO NA AGUA
NAVIO_ATACADO = 3 #TIRO CERTO

# imagens do jogo
tela_jogo = pygame.image.load("assets/Tela_jogo.png")
redimensionada = pygame.transform.scale(tela_jogo, (LARGURA_TELA, ALTURA_TELA))
celula_agua = pygame.image.load("assets/celula_agua.png")  
celula_redim = pygame.transform.scale(celula_agua, (TAMANHO_CELULA, TAMANHO_CELULA))
sub_completo = pygame.image.load("assets/submarino_completo.png")
sub_completo_redim = pygame.transform.scale(sub_completo, (TAMANHO_CELULA * 3, TAMANHO_CELULA))
sub1 = pygame.image.load("assets/submarino_1.png")
sub1_redim = pygame.transform.scale(sub1, (TAMANHO_CELULA, TAMANHO_CELULA))
sub2 = pygame.image.load("assets/submarino_2.png")   
sub2_redim = pygame.transform.scale(sub2, (TAMANHO_CELULA, TAMANHO_CELULA))     
sub3 = pygame.image.load("assets/submarino_3.png")
sub3_redim = pygame.transform.scale(sub3, (TAMANHO_CELULA, TAMANHO_CELULA))


TURNO_PLAYER1 = True
TURNO_PLAYER2 = False
