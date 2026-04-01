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
tiro_sub = pygame.image.load("assets/tiro_sub.png")
tiro_sub_redim = pygame.transform.scale(tiro_sub, (TAMANHO_CELULA, TAMANHO_CELULA))
tiro_agua = pygame.image.load("assets/tiro_agua.png")   
tiro_agua_redim = pygame.transform.scale(tiro_agua, (TAMANHO_CELULA, TAMANHO_CELULA))       


pygame.mixer.init()
efeito_sonoro_tiro = pygame.mixer.Sound("assets/efeito_tiro_navio.wav")
efeito_sonoro_agua = pygame.mixer.Sound("assets/efeito_tiro_agua.wav")
colocando_navio = pygame.mixer.Sound("assets/colocando_navio.wav")
som_erro = pygame.mixer.Sound("assets/som_erro.wav")
pygame.mixer.music.set_volume(0.5)  

 

