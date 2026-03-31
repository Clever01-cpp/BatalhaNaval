from src import constants
import pygame
from pygame.locals import *


def criar_matriz():
    linhas = 10 
    colunas = 10
    matriz = []
    for i in range(linhas):
        linha_percorrida = []
        for j in range(colunas):
            linha_percorrida.append(0)
        matriz.append(linha_percorrida)
    return matriz
def desenhar_matriz(screen, matriz):
    partes_sub = [constants.sub1_redim, constants.sub2_redim, constants.sub3_redim]

    for linha in range(len(matriz)):
        
        for coluna in range(len(matriz[0])):
           
            estado = matriz[linha][coluna]
            if estado == 0:
                x = constants.OFFSET_X + (coluna * constants.TAMANHO_CELULA)
                y = constants.OFFSET_Y + (linha * constants.TAMANHO_CELULA)
                screen.blit(constants.celula_redim, (x, y))
            if estado == 1 and (coluna == 0 or matriz[linha][coluna - 1] != 1):
                if coluna + 2 >= 10:
                    continue
                for i in range(3):  
                    x_sub = constants.OFFSET_X + ((coluna + i) * constants.TAMANHO_CELULA)
                    y_sub = constants.OFFSET_Y + ( linha * constants.TAMANHO_CELULA)
                    screen.blit(partes_sub[i], (x_sub, y_sub))
                    
                pygame.draw.rect(screen, constants.PRETO, (x, y, constants.TAMANHO_CELULA * 3, constants.TAMANHO_CELULA), 1)   
            
    
                                       
            
            

def posição_celula(pos_x, pos_y,):
    if (constants.OFFSET_X <= pos_x <= (constants.OFFSET_X + (constants.TAMANHO_CELULA * 10)) and 
        constants.OFFSET_Y <= pos_y <= (constants.OFFSET_Y + (constants.TAMANHO_CELULA * 10))):
        coluna = ((pos_x - constants.OFFSET_X)) // constants.TAMANHO_CELULA
        linha = (pos_y - constants.OFFSET_Y) // constants.TAMANHO_CELULA
        return int(linha), int(coluna)
    else:
        return None, None
def processar_clique(linha, coluna, matriz):
    if linha is None or coluna is None:
        return
    if coluna + 2 >= 10:
        print("Posição inválida para o navio. Tente novamente.")
        return
    if not sobreposição(linha, coluna, matriz):
        print("Sobreposição detectada. Tente novamente.")
        return
    estado_atual = matriz[linha][coluna]
    if linha is not None and coluna is not None and coluna + 2 <= 10:
        for i in range(3):
             matriz[linha][coluna + i] = 1    
def hover(hover_linha, hover_coluna, screen):
    if hover_linha is not None and hover_coluna is not None and hover_coluna + 2 < 10:
        cor =  constants.CINZA_CLARO
        for i in range(3):  
            x = constants.OFFSET_X + ((hover_coluna + i) * constants.TAMANHO_CELULA)
            y = constants.OFFSET_Y + (hover_linha * constants.TAMANHO_CELULA)
            pygame.draw.rect(screen, cor, (x, y, constants.TAMANHO_CELULA, constants.TAMANHO_CELULA))
            pygame.draw.rect(screen, constants.PRETO, (x, y, constants.TAMANHO_CELULA, constants.TAMANHO_CELULA), 1) 
def sobreposição(linha, coluna, matriz):
    for i in range(3):
        if matriz[linha][coluna + i] == 1:
            return False
    return True           
def texto(mensagem, fonte, cor):
    texto_renderizado = fonte.render(mensagem, True, cor)
    return texto_renderizado
def navios_restantes(matriz):
    navios_colocados = sum(row.count(1) for row in matriz) // 3
    navios_totais = constants.navios_jogador1
    return navios_totais - navios_colocados