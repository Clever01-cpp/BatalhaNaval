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
            elif estado == 1 and (coluna == 0 or matriz[linha][coluna - 1] != 1):
                if coluna + 2 < 10:
                    for i in range(3):   
                        x_sub = constants.OFFSET_X + ((coluna + i) * constants.TAMANHO_CELULA)
                        y_sub = constants.OFFSET_Y + ( linha * constants.TAMANHO_CELULA)
                        screen.blit(partes_sub[i], (x_sub, y_sub))
                        
            elif estado == 2:
                x_tiro_sub = constants.OFFSET_X + (coluna * constants.TAMANHO_CELULA)
                y_tiro_sub = constants.OFFSET_Y + (linha * constants.TAMANHO_CELULA)
                screen.blit(constants.tiro_sub_redim, (x_tiro_sub, y_tiro_sub))
            elif estado == 3:
                x_tiro_agua = constants.OFFSET_X + (coluna * constants.TAMANHO_CELULA)
                y_tiro_agua = constants.OFFSET_Y + (linha * constants.TAMANHO_CELULA)
                screen.blit(constants.tiro_agua_redim, (x_tiro_agua, y_tiro_agua))                  
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
    elif coluna + 2 >= 10:
        msg = "Posição inválida para o navio. Tente novamente."
        constants.som_erro.play()
        return msg
    elif not sobreposição(linha, coluna, matriz):
        msg = "Navios não podem estar adjacentes ou sobrepostos."
        constants.som_erro.play()
        return msg
    elif coluna + 2 <= 10:
        constants.colocando_navio.play()
        for i in range(3):
             matriz[linha][coluna + i] = 1 
        return None   
def hover(hover_linha, hover_coluna, screen):
    if hover_linha is not None and hover_coluna is not None and hover_coluna + 2 < 10:
        x_hover = constants.OFFSET_X + ((hover_coluna) * constants.TAMANHO_CELULA)
        y_hover = constants.OFFSET_Y + (hover_linha * constants.TAMANHO_CELULA)
        screen.blit(constants.sub_completo_redim, (x_hover, y_hover))     
def sobreposição(linha, coluna, matriz):

    tamanho = len(matriz)
    for i in range(3):
        if coluna + i >= tamanho:
            return False
        if matriz[linha][coluna + i] != 0:
            return False
    for i in range(-1, 2):
        for j in range(-1, 4):

            nova_linha = linha + i
            nova_coluna = coluna + j

            if 0 <= nova_linha < tamanho and 0 <= nova_coluna < tamanho:

              
                if nova_linha == linha and coluna <= nova_coluna <= coluna + 2:
                    continue
                if matriz[nova_linha][nova_coluna] == 1:
                    return False
    return True 
def texto(mensagem, fonte, cor):
    texto_renderizado = fonte.render(mensagem, True, cor)
    return texto_renderizado
def navios_restantes(matriz):
    navios_colocados = sum(row.count(1) for row in matriz) // 3
    navios_totais = constants.navios_jogador1
    return navios_totais - navios_colocados
def turnos_jogadores(tela, matriz, matriz_jogador1, matriz_jogador2, matriz_ataque_j1, matriz_ataque_j2, jogador_atual, linha, coluna):
                
                if linha is None or coluna is None:
                    return jogador_atual, None, jogador_atual, False
                msg = None
                if tela == "jogador1_posicionando":
                    msg = processar_clique(linha, coluna, matriz_jogador1)
                if tela == "jogador2_posicionando":
                    msg = processar_clique(linha, coluna, matriz_jogador2)
                if tela == "jogando":
                    if jogador_atual == 1:
                        if matriz_ataque_j1[linha][coluna] != 0:
                            msg = "Você já atirou nessa posição. Tente novamente."
                            return jogador_atual, msg, jogador_atual, False
                        if matriz_jogador2[linha][coluna] == 1:
                            matriz_jogador2[linha][coluna] = 2
                            matriz_ataque_j1[linha][coluna] = 2
                            matriz[linha][coluna] = 2
                            msg = "Acertou! Continue atacando!"
                            constants.efeito_sonoro_tiro.play()
                            return jogador_atual, msg, jogador_atual, False
                        else:
                            matriz_ataque_j1[linha][coluna] = 3
                            matriz[linha][coluna] = 3
                            print("Errou o tiro!")
                            proximo_jogador = 2
                            msg = "Errou o tiro! Agora é a vez do jogador 2."
                            constants.efeito_sonoro_agua.play()
                            return jogador_atual, msg, proximo_jogador, True
                    elif jogador_atual == 2:
                        if matriz_ataque_j2[linha][coluna] != 0:
                            msg = "Você já atirou nessa posição. Tente novamente."
                            return jogador_atual, msg, jogador_atual, True
                        if matriz_jogador1[linha][coluna] == 1:
                            matriz_jogador1[linha][coluna] = 2
                            matriz_ataque_j2[linha][coluna] = 2
                            matriz[linha][coluna] = 2
                            msg = "Acertou! Continue atacando!"
                            constants.efeito_sonoro_tiro.play()
                            return jogador_atual, msg, jogador_atual, False
                        else:
                            matriz_ataque_j2[linha][coluna] = 3
                            matriz[linha][coluna] = 3
                            proximo_jogador = 1
                            msg = "Errou o tiro! Agora é a vez do jogador 1."
                            constants.efeito_sonoro_agua.play()
                            return jogador_atual, msg, proximo_jogador, True
                return jogador_atual, msg, jogador_atual, False
def posicionar_navios(matriz_jogador1, matriz_jogador2, tela, screen, fonte, x, y, jogador_atual, matriz_ataque_j1, matriz_ataque_j2, matriz,msg):
    
    if tela == "jogador1_posicionando":
        restante = navios_restantes(matriz_jogador1)
        if restante == 0:
            tela = "jogador2_posicionando"
    elif tela == "jogador2_posicionando":
        restante = navios_restantes(matriz_jogador2)
        if restante == 0:
            tela = "jogando"
    screen.fill(constants.BRANCO)
    screen.blit(constants.redimensionada, (0, 0))
    if tela == "jogador1_posicionando":
        desenhar_matriz(screen, matriz_jogador1)
        hover_linha, hover_coluna = posição_celula(x,y)
        hover(hover_linha, hover_coluna, screen)
        screen.blit(constants.caixa_dialogo_redim, (100, 20))
        mensagem = (f"Jogador 1, coloque seu navio. {restante} Restantes!")
        screen.blit(texto(mensagem, fonte, constants.BRANCO), (125, 30))
        if msg:
            screen.blit(constants.caixa_dialogo_redim2, (10, 587))
            screen.blit(texto(msg, fonte, constants.BRANCO), (50, 599))     
    elif tela == "jogador2_posicionando":
        desenhar_matriz(screen, matriz_jogador2)
        hover_linha, hover_coluna = posição_celula(x,y)
        hover(hover_linha, hover_coluna, screen)
        screen.blit(constants.caixa_dialogo_redim, (100, 20))
        mensagem = (f"Jogador 2, coloque seu navio. {restante} Restantes!")
        screen.blit(texto(mensagem,fonte, constants.BRANCO), (120, 30))
        if msg:
            screen.blit(constants.caixa_dialogo_redim2, (10, 587))
            screen.blit(texto(msg, fonte, constants.BRANCO), (50, 599)) 
    
    if tela == "jogando":
        if jogador_atual == 1:
            mensagem = "Jogador 1: sua vez de atacar!"
            desenhar_matriz(screen, matriz_ataque_j1)
            if msg:
                screen.blit(constants.caixa_dialogo_redim2, (10, 587))
                screen.blit(texto(msg, fonte, constants.BRANCO), (50, 599))
        else:
            mensagem = "Jogador 2: sua vez de atacar!"
            desenhar_matriz(screen, matriz_ataque_j2)
            if msg:
                screen.blit(constants.caixa_dialogo_redim2, (10, 587))
                screen.blit(texto(msg, fonte, constants.BRANCO), (50, 599))
        screen.blit(constants.caixa_dialogo_redim, (100, 20))
        screen.blit(texto(mensagem, fonte, constants.BRANCO), (constants.OFFSET_X, 30))
            
    return tela   
def main():

    pygame.init()

    screen = pygame.display.set_mode((constants.LARGURA_TELA, constants.ALTURA_TELA))
    fonte = pygame.font.Font("assets/fontes/Seven Segment.ttf", 30)
    pygame.display.set_caption("Batalha naval !")
    clock = pygame.time.Clock()
    mensagem = ""
    tela = "jogador1_posicionando"
    matriz = criar_matriz()
    matriz_ataque_j1 = criar_matriz()
    matriz_ataque_j2 = criar_matriz()
    matriz_jogador1 = criar_matriz()
    matriz_jogador2 = criar_matriz()
    jogador_atual = 1
    msg = None
    tempo_msg = 0
    duracao_msg = 2000
    esperando_turno = False
    tempo_espera = 0
    duração_espera = 2000
    proximo_jogador = jogador_atual

    print(matriz)

    while True:
        
        for event in pygame.event.get():
            x,y = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not esperando_turno:
                x,y = pygame.mouse.get_pos()
                linha, coluna = posição_celula(x, y)
                jogador_atual, nova_msg, prox_jogador, esperando = turnos_jogadores(tela, matriz, matriz_jogador1, matriz_jogador2, matriz_ataque_j1, matriz_ataque_j2, jogador_atual, linha, coluna)
            
                if nova_msg:
                    msg = nova_msg  
                    tempo_msg = pygame.time.get_ticks()
                if esperando:
                    esperando_turno = True
                    tempo_espera = pygame.time.get_ticks()
                    proximo_jogador = prox_jogador
                
        tempo_atual = pygame.time.get_ticks()
        if esperando_turno and tempo_atual - tempo_espera > duração_espera:
            jogador_atual = proximo_jogador
            esperando_turno = False  
        if msg and tempo_atual - tempo_msg >= duracao_msg:
            msg = None       
        tela = posicionar_navios(matriz_jogador1, matriz_jogador2, tela, screen, fonte, x, y, jogador_atual, matriz_ataque_j1, matriz_ataque_j2, matriz, msg)
        

    
        clock.tick(60)
        pygame.display.update()
       

        




