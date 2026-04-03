from src import functions
import pygame
from pygame.locals import *

LARGURA_TELA = 800
ALTURA_TELA = 650
TAMANHO_CELULA = 50 
OFFSET_X = 150
OFFSET_Y = 80



BRANCO = (255,255,255)
PRETO = (0,0,0)
navios_jogador1 = 7
navios_jogador2 = 7



redimensionada = pygame.transform.scale(pygame.image.load("assets/imagens/Tela_jogo.png"), (LARGURA_TELA, ALTURA_TELA))
celula_redim = pygame.transform.scale(pygame.image.load("assets/imagens/celula_agua.png"), (TAMANHO_CELULA, TAMANHO_CELULA))
sub_completo_redim = pygame.transform.scale(pygame.image.load("assets/imagens/submarino_completo.png"), (TAMANHO_CELULA * 3, TAMANHO_CELULA))
sub1_redim = pygame.transform.scale(pygame.image.load("assets/imagens/submarino_1.png"), (TAMANHO_CELULA, TAMANHO_CELULA))  
sub2_redim = pygame.transform.scale(pygame.image.load("assets/imagens/submarino_2.png") , (TAMANHO_CELULA, TAMANHO_CELULA))     
sub3_redim = pygame.transform.scale(pygame.image.load("assets/imagens/submarino_2.png") , (TAMANHO_CELULA, TAMANHO_CELULA))
tiro_sub_redim = pygame.transform.scale(pygame.image.load("assets/imagens/tiro_sub.png"), (TAMANHO_CELULA, TAMANHO_CELULA))
tiro_agua_redim = pygame.transform.scale(pygame.image.load("assets/imagens/tiro_agua.png"), (TAMANHO_CELULA, TAMANHO_CELULA))       
caixa_dialogo_redim = pygame.transform.scale(pygame.image.load("assets/imagens/caixa_dialogo_ret.png"), (600, 55))
caixa_dialogo_redim2 = pygame.transform.scale(pygame.image.load("assets/imagens/caixa_dialogo_ret.png"), (780, 55))


pygame.mixer.init()
efeito_sonoro_tiro = pygame.mixer.Sound("assets/sons_e_efeitos/efeito_tiro_navio.wav")
efeito_sonoro_agua = pygame.mixer.Sound("assets/sons_e_efeitos/efeito_tiro_agua.wav")
colocando_navio = pygame.mixer.Sound("assets/sons_e_efeitos/colocando_navio.wav")
som_erro = pygame.mixer.Sound("assets/sons_e_efeitos/som_erro.wav")
pygame.mixer.music.set_volume(0.5)  

 

