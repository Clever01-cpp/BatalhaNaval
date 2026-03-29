import pygame
from pygame.locals import *
from src import constants
from src import functions
from sys import exit

#função principal do jogo, onde a maioria da lógica acontece, no caso, aqui ainda estou trabalhando alternancia de telas, cliques do jogador e etc, ainda estou trabalhando com isso, por enquanto estou apenas alternando as cores, mas posteriormente quero colocar uma imagem de submarinos
def main():

    pygame.init()

    screen = pygame.display.set_mode((constants.LARGURA_TELA, constants.ALTURA_TELA))
    pygame.display.set_caption("Batalha naval !")
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 30)
    mensagem = ""
    tela = "jogador1_posicionando"
    matriz_jogador1 = functions.criar_matriz()
    matriz_jogador2 = functions.criar_matriz()
    while True:

        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tela == "jogador1_posicionando":
                    x,y = pygame.mouse.get_pos()
                    linha, coluna = functions.posição_celula(x,y)
                    functions.processar_clique(linha, coluna, matriz_jogador1)
                if tela == "jogador2_posicionando":
                    x,y = pygame.mouse.get_pos()
                    linha, coluna = functions.posição_celula(x,y)
                    functions.processar_clique(linha, coluna, matriz_jogador2)
        if tela == "jogador1_posicionando":
            restante = functions.navios_restantes(matriz_jogador1)
            if restante == 0:
                tela = "jogador2_posicionando"
        elif tela == "jogador2_posicionando":
            restante = functions.navios_restantes(matriz_jogador2)
            if restante == 0:
                tela = "jogando"
        screen.fill(constants.BRANCO)
        if tela == "jogador1_posicionando":
            functions.desenhar_matriz(screen, matriz_jogador1)
            x,y = pygame.mouse.get_pos()
            hover_linha, hover_coluna = functions.posição_celula(x,y)
            functions.hover(hover_linha, hover_coluna, screen)
            mensagem = (f"Jogador 1, coloque seu navio. {restante} Restantes!")
            screen.blit(functions.texto(mensagem, fonte, constants.PRETO), (190, 30)) 
        elif tela == "jogador2_posicionando":
            functions.desenhar_matriz(screen, matriz_jogador2)
            x,y = pygame.mouse.get_pos()
            hover_linha, hover_coluna = functions.posição_celula(x,y)
            functions.hover(hover_linha, hover_coluna, screen)
            mensagem = (f"Jogador 2, coloque seu navio. {restante} Restantes!")
            screen.blit(functions.texto(mensagem, fonte, constants.PRETO), (190, 30))
            
                
        clock.tick(60)
        pygame.display.update()
       

        






if __name__ == "__main__":
    main()
    