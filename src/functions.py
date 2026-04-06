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
def desenhar_matriz(screen, matriz, offset_x, offset_y):
    partes_sub = [constants.sub1_redim, constants.sub2_redim, constants.sub3_redim]

    for linha in range(len(matriz)):
        
        for coluna in range(len(matriz[0])):
           
            estado = matriz[linha][coluna]
            if estado == 0:
                x = offset_x + (coluna * constants.TAMANHO_CELULA)
                y = offset_y + (linha * constants.TAMANHO_CELULA)
                screen.blit(constants.celula_redim, (x, y))
            elif estado == 1 and (coluna == 0 or matriz[linha][coluna - 1] != 1):
                if coluna + 2 < 10:
                    for i in range(3):   
                        x_sub = offset_x + ((coluna + i) * constants.TAMANHO_CELULA)
                        y_sub = offset_y + ( linha * constants.TAMANHO_CELULA)
                        screen.blit(partes_sub[i], (x_sub, y_sub))
                        
            elif estado == 2:
                x_tiro_sub = offset_x + (coluna * constants.TAMANHO_CELULA)
                y_tiro_sub = offset_y + (linha * constants.TAMANHO_CELULA)
                screen.blit(constants.tiro_sub_redim, (x_tiro_sub, y_tiro_sub))
            elif estado == 3:
                x_tiro_agua = offset_x + (coluna * constants.TAMANHO_CELULA)
                y_tiro_agua = offset_y + (linha * constants.TAMANHO_CELULA)
                screen.blit(constants.tiro_agua_redim, (x_tiro_agua, y_tiro_agua))                  
def posição_celula(pos_x, pos_y, offset_x, offset_y):
    if (offset_x <= pos_x <= (offset_x + (constants.TAMANHO_CELULA * 10)) and 
        offset_y <= pos_y <= (offset_y + (constants.TAMANHO_CELULA * 10))):
        coluna = ((pos_x - offset_x)) // constants.TAMANHO_CELULA
        linha = (pos_y - offset_y) // constants.TAMANHO_CELULA
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
def texto(screen, mensagem, fonte, cor, x, y, centralizar=False):
    render = fonte.render(mensagem, True, cor)
    if centralizar:
        x -= render.get_width() // 2
    screen.blit(render, (x, y))
def desenhar_caixa(screen, msg, fonte, y):
    if msg:
        screen.blit(constants.caixa_dialogo_redim2, (10, y))
        texto(screen, msg, fonte, constants.BRANCO, 50, y + 10)
def navios_restantes(matriz):
    navios_colocados = sum(row.count(1) for row in matriz) // 3
    navios_totais = constants.navios_jogador1
    return navios_totais - navios_colocados
def partes_restantes(matriz):
    return sum(row.count(1) for row in matriz)
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
                            constants.som_erro.play()
                            return jogador_atual, msg, jogador_atual, False
                        if matriz_jogador2[linha][coluna] == 1:
                            matriz_jogador2[linha][coluna] = 2
                            matriz_ataque_j1[linha][coluna] = 2
                            matriz[linha][coluna] = 2
                            msg = "Acertou! Continue atacando!"
                            constants.efeito_sonoro_tiro.play()
                            if partes_restantes(matriz_jogador2) == 0:
                                msg = "Vencedor, esses são os seus acertos no inimigo"
                                pygame.mixer.music.stop()
                                constants.som_vitoria.play()
                                tela = "fim_de_jogo"
                                return jogador_atual, msg, jogador_atual, False
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
                            constants.som_erro.play()
                            return jogador_atual, msg, jogador_atual, True
                        if matriz_jogador1[linha][coluna] == 1:
                            matriz_jogador1[linha][coluna] = 2
                            matriz_ataque_j2[linha][coluna] = 2
                            matriz[linha][coluna] = 2
                            msg = "Acertou! Continue atacando!"
                            constants.efeito_sonoro_tiro.play()
                            if partes_restantes(matriz_jogador1) == 0:
                                msg = "Vencedor, esses são os seus acertos no inimigo"
                                pygame.mixer.music.stop()
                                constants.som_vitoria.play()
                                tela = "fim_de_jogo"
                                return jogador_atual, msg, jogador_atual, False
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
    screen.blit(constants.tela_jogo_redim, (0, 0))
    
    if tela == "inicio":
        screen.fill(constants.BRANCO)
        screen.blit(constants.tela_inicio_redim, (0, 0))
        if 218 < x < 588 and 415 < y < 525:
            sombra = pygame.Surface((370, 110), pygame.SRCALPHA)
            pygame.draw.rect(
            sombra,
            (0, 0, 0, 120),  
            (0, 0, 370, 110),
            border_radius=20
                            )
            screen.blit(sombra, (218, 415))  
    if tela == "jogador1_posicionando":
        desenhar_matriz(screen, matriz_jogador1, constants.OFFSET_X, constants.OFFSET_Y)
        hover_linha, hover_coluna = posição_celula(x,y, constants.OFFSET_X, constants.OFFSET_Y)
        hover(hover_linha, hover_coluna, screen)
        
        mensagem = (f"Jogador 1, coloque seu navio. {restante} Restantes!")
        desenhar_caixa(screen, mensagem, fonte, 20)
        if msg:
            desenhar_caixa(screen, msg, fonte, 587)     
    elif tela == "jogador2_posicionando":
        desenhar_matriz(screen, matriz_jogador2, constants.OFFSET_X, constants.OFFSET_Y)
        hover_linha, hover_coluna = posição_celula(x,y, constants.OFFSET_X, constants.OFFSET_Y)
        hover(hover_linha, hover_coluna, screen)
        
        mensagem = (f"Jogador 2, coloque seu navio. {restante} Restantes!")
        desenhar_caixa(screen, mensagem, fonte, 20)
        if msg:
            desenhar_caixa(screen, msg, fonte, 587) 
    elif tela == "jogando":
        if jogador_atual == 1:
            mensagem = "Jogador 1: sua vez de atacar!"
            desenhar_matriz(screen, matriz_ataque_j1, constants.OFFSET_X, constants.OFFSET_Y)
            if msg:
                desenhar_caixa(screen, msg, fonte, 587)
        else:
            mensagem = "Jogador 2: sua vez de atacar!"
            desenhar_matriz(screen, matriz_ataque_j2, constants.OFFSET_X, constants.OFFSET_Y)
            if msg:
                desenhar_caixa(screen, msg, fonte, 587)
        desenhar_caixa(screen, mensagem, fonte, 20)
    elif tela == "fim_de_jogo":
        screen.fill(constants.BRANCO)
        screen.blit(constants.tela_vitoria_redim, (0, 0))
        if jogador_atual == 1:
            if msg:
                desenhar_caixa(screen, msg, fonte, 590)
                desenhar_matriz(screen, matriz_ataque_j1, 100, constants.OFFSET_Y)
            msg_vitoria = "Parabéns, jogador 1! Você venceu a partida!"
            desenhar_caixa(screen, msg_vitoria, fonte, 20)
        else:
            if msg:
                desenhar_caixa(screen, msg, fonte, 590)
                desenhar_matriz(screen, matriz_ataque_j2, 100, constants.OFFSET_Y) 
            msg_vitoria = "Parabéns, jogador 2! Você venceu a partida!"
            desenhar_caixa(screen, msg_vitoria, fonte, 20)
        
        msg = "Pressione\nESC\npara sair\nou R\npara\nreiniciar."  
        x_centro = 700
        y_base = constants.ALTURA_TELA // 2
        x_caixa = x_centro - constants.caixa_quad.get_width() // 2
        screen.blit(constants.caixa_quad, (x_caixa, y_base))
        linhas = msg.split('\n')
        for i, linha in enumerate(linhas):
            texto(screen, linha, fonte, constants.BRANCO, x_centro, y_base + 30 + i * 30, centralizar=True)
        
    return tela  
def resetar_jogo():
    return (
    criar_matriz(), 
    criar_matriz(), 
    criar_matriz(), 
    criar_matriz(), 
    1, 
    "inicio", 
    None, 
    False
    )

def main():

    pygame.init()

    screen = pygame.display.set_mode((constants.LARGURA_TELA, constants.ALTURA_TELA))
    fonte = pygame.font.Font("assets/fontes/Seven Segment.ttf", 30)
    pygame.display.set_caption("Batalha naval !")
    clock = pygame.time.Clock()
    mensagem = ""
    tela = "inicio"
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
    fim_de_jogo = False

    

    while True:
        
        for event in pygame.event.get():
            x,y = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not esperando_turno and tela != "fim_de_jogo":
                x,y = pygame.mouse.get_pos()
                linha, coluna = posição_celula(x, y, constants.OFFSET_X, constants.OFFSET_Y)
                jogador_atual, nova_msg, prox_jogador, esperando = turnos_jogadores(tela, matriz, matriz_jogador1, matriz_jogador2, matriz_ataque_j1, matriz_ataque_j2, jogador_atual, linha, coluna)
                if 218 < x < 588 and 415 < y < 525:
                    if tela == "inicio":
                        tela = "jogador1_posicionando"
                if nova_msg:
                    msg = nova_msg  
                    tempo_msg = pygame.time.get_ticks()
                    if "Vencedor" in msg:
                        tela = "fim_de_jogo"
                        fim_de_jogo = True
                        continue
                if esperando:
                    esperando_turno = True
                    tempo_espera = pygame.time.get_ticks()
                    proximo_jogador = prox_jogador
            if event.type == pygame.KEYDOWN: 
                if tela == "fim_de_jogo":
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_r:
                        
                        matriz_jogador1, matriz_jogador2, matriz_ataque_j1, matriz_ataque_j2, jogador_atual, tela, msg, fim_de_jogo = resetar_jogo() 
                        
                                   
        tempo_atual = pygame.time.get_ticks()
        if esperando_turno and not fim_de_jogo and tempo_atual - tempo_espera > duração_espera:
            jogador_atual = proximo_jogador
            esperando_turno = False  
        if msg and tempo_atual - tempo_msg >= duracao_msg and not fim_de_jogo:
            msg = None
        
    
        tela = posicionar_navios(matriz_jogador1, matriz_jogador2, tela, screen, fonte, x, y, jogador_atual, matriz_ataque_j1, matriz_ataque_j2, matriz, msg)
        

    
        clock.tick(60)
        pygame.display.update()
       

        




