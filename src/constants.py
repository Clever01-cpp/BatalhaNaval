from src import functions
#Configurações da tela

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


#turnos

TURNO_PLAYER1 = True
TURNO_PLAYER2 = False
