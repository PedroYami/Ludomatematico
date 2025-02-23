import pygame
from pygame import mixer
import random
import time
import random
from tkinter import *

pygame.init()
pygame.display.set_caption("Ludo")
screen = pygame.display.set_mode((680, 600))


tabuleiro = pygame.image.load('tabuleiro.jpg')
estrela = pygame.image.load('img/doutor-fran.jpg')
um = pygame.image.load('dado/1.png')
dois = pygame.image.load('dado/2.png')
tres = pygame.image.load('dado/3.png')
quatro = pygame.image.load('dado/4.png')
cinco = pygame.image.load('dado/5.png')
seis = pygame.image.load('dado/6.png')

vermelho = pygame.image.load('pecas/vermelha.png')
azul = pygame.image.load('pecas/azul.png')
verde = pygame.image.load('pecas/verde.png')
amarelo = pygame.image.load('pecas/amarela.png')

func_a = pygame.image.load('graficos/grafico.webp')
func_b = pygame.image.load('graficos/grafico2.webp')



DADO = [um, dois, tres, quatro, cinco, seis]
cor = [vermelho, verde, amarelo, azul]
graficos = [func_a, func_b]

class Pergunta:
    def __init__(self, pergunta, opcoes, correta, imagem):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.correta = correta
        self.imagem = pygame.image.load('graficos/grafico.webp')
        
perguntas =  [


    Pergunta("Qual é a forma geral de uma função afim?", ["a) y = ax² + b", "b) y = ax + b", "c) y = x² + a", "d) y = x – b"], 1, "grafico.webp"),
    Pergunta("O que é necessário para que f(x) = ax + b seja crescente?", ["a) O coeficiente angular (a) deve ser positivo.", "b) O coeficiente angular (a) deve ser negativo.", "c) O coeficiente linear (b) deve ser positivo.", "d) O coeficiente linear (b) deve ser negativo."], 0, "grafico.webp"),
    Pergunta("Qual é a equação de uma reta com inclinação 3 e interceptação no eixo y em 2?", ["a) y = 3x + 2", "b) y = 2x + 3", "c) y = 3x - 2", "d) y = 2x – 3"], 0, "grafico.webp"),
    Pergunta("O que representa o coeficiente angular em uma função afim?", ["a) O ponto onde a reta cruza o eixo y.", "b) A inclinação da reta.", "c) A inclinação do eixo x.", "d) O ponto onde a reta cruza o eixo x."], 1, "grafico.webp"),
    Pergunta("Qual é a forma geral de uma função quadrática?", ["a) y = ax + b", "b) y = ax² + b", "c) y = a²x + b", "d) y = ax² + bx + c"], 3, "grafico.webp"),
    Pergunta("O que é o vértice de uma parábola com concavidade voltada para cima?", ["a) O ponto onde a parábola cruza o eixo x.", "b) O ponto de mínimo da parábola.", "c) O ponto de interseção entre duas parábolas.", "d) O ponto mais alto da parábola."], 1, "grafico.webp"),
    Pergunta("O que é o vértice de uma parábola com concavidade voltada para baixo?", ["a) O ponto de máximo da parábola", "b) O ponto mais baixo da parábola.", "c) O ponto de interseção entre duas parábolas.", "d) O ponto onde a parábola cruza o eixo x."], 0, "grafico.webp"),
    Pergunta("Como determinar se a concavidade de uma parábola se abre para cima ou para baixo?", ["a) Pelo valor do coeficiente a na forma geral.", "b) Pelo valor de b na forma geral.", "c) Pelo valor de c na forma geral.", "d) Pelo valor de x na forma geral."], 0, "grafico.webp"),
    Pergunta("Quando a concavidade de uma parábola está voltada para cima?", ["a) Quando o coeficiente a for positivo.", "b) Quando o coeficiente b for positivo.", "c) Quando o coeficiente a for negativo.", "d) Quando o coeficiente b for negativo."], 0, "grafico2.webp"),
    Pergunta("Quando a concavidade de uma parábola está voltada para baixo?", ["a) Quando o coeficiente a for positivo.", "b) Quando o coeficiente b for positivo.", "c) Quando o coeficiente a for negativo.", "d) Quando o coeficiente b for negativo."], 2, "grafico2.webp"),
    Pergunta("Qual é o eixo de simetria de uma parábola?", ["a) A reta vertical que passa pelo vértice.", "b) A reta horizontal que passa pelo vértice.", "c) A reta diagonal que passa pelo vértice.", "d) A reta inclinada que passa pelo vértice."], 0, "grafico2.webp"),
    Pergunta("Como determinar graficamente as raízes (valores que tornam a função igual a zero, ƒ(x) = 0) de uma função quadrática?", ["a) Os pontos onde a parábola cruza o eixo y.", "b) Os pontos de interseção da parábola com o eixo x.", "c) Os pontos de interseção da parábola com o eixo y.", "d) Os pontos mais altos e mais baixos da parábola."], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 2x – 6:", ["a) x = 1", "b) x = 2", "c) x = 3", "d) x = 4"], 2, "grafico2.webp"),
    Pergunta(" Determine a raiz da função f(x) = 3x + 15:", ["a) x = -3", "b) x = 3", "c) x = 5", "d) x = -5"], 3, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 9x - 18:", ["a) x = 1", "b) x = 2", "c) x = -2", "d) x = 3"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = x - 10:", ["a) x = 10", "b) x = -5", "c) x = -10", "d) x = 5"], 0, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 2x + 22:", ["a) x = 11", "b) x = 9", "c) x = -11", "d) x = 9"], 2, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 4x - 16:", ["a) x = -2", "b) x = 2", "c) x = -4", "d) x = 4"], 3, "grafico2.webp"),
    Pergunta("Determine a raiz da função Y = 10x - 30:", ["a) x = 15", "b) x = -3", "c) x = 3", "d) x = 5"], 2, "grafico2.webp"),
    Pergunta(" Determine a raiz da função Y = 3x - 21:", ["a) x = 6", "b) x = 7", "c) x = 8", "d) x = 9"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = -20x - 40:", ["a) x = 10", "b) x = -2", "c) x = 20", "d) x = 4"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 5x - 40:", ["a) x = 10", "b) x = 5", "c) x = 8", "d) x = 4"], 2, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 5x - 80:", ["a) x = 10", "b) x = 16", "c) x = 20", "d) x = -16"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 20x - 80:", ["a) x = 10", "b) x = 2", "c) x = 20", "d) x = 4"], 3, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 30x - 90:", ["a) x = 10", "b) x = 3", "c) x = 20", "d) x = 4"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 20x - 400:", ["a) x = 10", "b) x = 20", "c) x = 40", "d) x = -20"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = -2x - 400:", ["a) x = 100", "b) x = -200", "c) x = 200", "d) x = 40"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 40x - 120:", ["a) x = 1", "b) x = 3", "c) x = 2", "d) x = 4"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 4x + 20:", ["a) x = -10", "b) x = -5", "c) x = 20", "d) x = 4"], 1, "grafico2.webp"),
    Pergunta("Determine a raiz da função f(x) = 6x + 36:", ["a) x = 6", "b) x = -6", "c) x = 3", "d) x = -3"], 1, "grafico2.webp"),
    Pergunta("Como você encontraria a interseção y (b) de uma função afim com o eixo y?", ["a) A interseção y (b) de uma função afim é encontrada multiplicando o coeficiente 'a' pela coordenada x do ponto de interseção com o eixo y.", "b) Para encontrar a interseção y (b) de uma função afim, você subtrai o valor de 'a' da coordenada y de qualquer ponto na reta.", "c) Definindo x = 0 na equação da função e resolvendo para y.", "d) A interseção y (b) de uma função afim é determinada somando o coeficiente 'a' com a coordenada y de qualquer ponto na reta."], 2, "grafico2.webp"),
    Pergunta("Qual é a equação da Reta que passa pelos pontos (3, 5) e (1, 7)?", ["a) A equação da reta que passa por esses pontos é y=2x+1.", "b) A equação da reta é y=-x+10.", "c) A equação da reta é y=5x+2.", "d) A equação da reta é y = -x + 8."], 3, "grafico2.webp"),
    Pergunta("O que determina a concavidade de uma parábola em uma função quadrática?", ["a) O coeficiente 'a' determina a concavidade.", "b) A distância entre os pontos de interceptação com o eixo x determina a concavidade.", "c) A média dos coeficientes da função quadrática determina a concavidade.", "d) O coeficiente 'b' determina a direção da abertura."], 0, "grafico2.webp"),
    Pergunta("Qual é a relação entre o coeficiente 'b' em uma função afim e o ponto onde a reta cruza o eixo y?", ["a) O coeficiente 'b' na função afim é igual à coordenada y do ponto de interseção com o eixo y.", "b) O coeficiente 'b' na função afim determina a inclinação da reta.", "c) O coeficiente 'b' na função afim não está relacionado ao ponto de interseção com o eixo y.", "d) O coeficiente 'b' na função afim é igual ao valor absoluto da coordenada y do ponto de interseção com o eixo y."], 0, "grafico2.webp"),



]


numero = 1
jogadorAtual = 0
peçaMorta = False
dadoRolado = False
classificaçãoVencedor = []

jogadores_responderam = [False, False, False, False]

fonte = pygame.font.Font('freesansbold.ttf', 11)
FONT = pygame.font.Font('freesansbold.ttf', 16)
textoJogadorAtual = fonte.render('Jogador Atual', True, (0, 0, 0))
linha = fonte.render('------------------------------------', True, (0, 0, 0))




def blit_tudo():
    for i in SEGURA[4:]:
        screen.blit(estrela, i)

    for i in range(len(posição)):
        for j in posição[i]:
            screen.blit(cor[i], j)

    screen.blit(DADO[numero-1], (605, 270))

    screen.blit(cor[jogadorAtual], (620, 28))
    screen.blit(textoJogadorAtual, (600, 10))
    screen.blit(linha, (592, 59))

    for i in range(len(classificaçãoVencedor)):
        rank = FONT.render(f'{i+1}.', True, (0, 0, 0))
        screen.blit(rank, (600, 85 + (40*i)))
        screen.blit(cor[classificaçãoVencedor[i]], (620, 75 + (40*i)))


def para_casa(x, y):
    #  R2
    if (posição[x][y][1] == 284 and posição[x][y][0] <= 202 and x == 0) \
            and (posição[x][y][0] + 38*numero > VENCEDOR[x][0]):
        return False
    #  Y2
    elif (posição[x][y][1] == 284 and 368 < posição[x][y][0] and x == 2) \
            and (posição[x][y][0] - 38*numero < VENCEDOR[x][0]):
        return False
    #  G2
    elif (posição[x][y][0] == 284 and posição[x][y][1] <= 202 and x == 1) \
            and (posição[x][y][1] + 38*numero > VENCEDOR[x][1]):
        return False
    #  B2
    elif (posição[x][y][0] == 284 and posição[x][y][1] >= 368 and x == 3) \
            and (posição[x][y][1] - 38*numero < VENCEDOR[x][1]):
        return False
    return True

CASA = [[(110, 58),  (61, 107),  (152, 107), (110, 152)],  # Vermelho
        [(466, 58),  (418, 107), (509, 107), (466, 153)],  # Verde
        [(466, 415), (418, 464), (509, 464), (466, 510)],  # Amarelo
        [(110, 415), (61, 464),  (152, 464), (110, 510)]]  # Azul

SEGURA = [(50, 240), (328, 50), (520, 328), (240, 520),
          (88, 328), (240, 88), (482, 240), (328, 482)]

posição = [[[110, 58],  [61, 107],  [152, 107], [110, 152]],  # Vermelho
            [[466, 58],  [418, 107], [509, 107], [466, 153]],  # Verde
            [[466, 415], [418, 464], [509, 464], [466, 510]],  # Amarelo
            [[110, 415], [61, 464],  [152, 464], [110, 510]]]  # Azul

pulo = {(202, 240): (240, 202),  # R1 -> G3
        (328, 202): (368, 240),  # G1 -> Y3
        (368, 328): (328, 368),  # Y1 -> B3
        (240, 368): (202, 328)}  # B1 -> R3

VENCEDOR = [[240, 284], [284, 240], [330, 284], [284, 330]]

def mostrar_peça(x, y):
    screen.fill((255, 255, 255))
    screen.blit(tabuleiro, (0, 0))

    for i in SEGURA[4:]:
        screen.blit(estrela, i)

    for i in range(len(posição)):
        for j in posição[i]:
            screen.blit(cor[i], j)

    screen.blit(DADO[numero-1], (605, 270))
    

    

    screen.blit(cor[jogadorAtual], (620, 28))
    screen.blit(textoJogadorAtual, (600, 10))
    screen.blit(linha, (592, 59))

    for i in range(len(classificaçãoVencedor)):
        rank = FONT.render(f'{i+1}.', True, (0, 0, 0))
        screen.blit(rank, (600, 85 + (40*i)))
        screen.blit(cor[classificaçãoVencedor[i]], (620, 75 + (40*i)))

    pygame.display.update()
    time.sleep(0.5)



def mover_peça(x, y):
    global jogadorAtual, dadoRolado

    if tuple(posição[x][y]) in CASA[jogadorAtual] and numero == 6:
        posição[x][y] = list(SEGURA[jogadorAtual])
        dadoRolado = False


    elif tuple(posição[x][y]) not in CASA[jogadorAtual]:
        dadoRolado = False
        if not numero == 6:
            jogadorAtual = (jogadorAtual+1) % 4

        
        if (posição[x][y][1] == 284 and posição[x][y][0] <= 202 and x == 0) \
                and (posição[x][y][0] + 38*numero <= VENCEDOR[x][0]):
            for i in range(numero):
                posição[x][y][0] += 38
                mostrar_peça(x, y)

        #  Y2
        elif (posição[x][y][1] == 284 and 368 < posição[x][y][0] and x == 2) \
                and (posição[x][y][0] - 38*numero >= VENCEDOR[x][0]):
            for i in range(numero):
                posição[x][y][0] -= 38
                mostrar_peça(x, y)

        #  G2
        elif (posição[x][y][0] == 284 and posição[x][y][1] <= 202 and x == 1) \
                and (posição[x][y][1] + 38*numero <= VENCEDOR[x][1]):
            for i in range(numero):
                posição[x][y][1] += 38
                mostrar_peça(x, y)
        #  B2
        elif (posição[x][y][0] == 284 and posição[x][y][1] >= 368 and x == 3) \
                and (posição[x][y][1] - 38*numero <= VENCEDOR[x][1]):
            for i in range(numero):
                posição[x][y][1] -= 38
                mostrar_peça(x, y)

        else:
            for _ in range(numero):
                #  R1, Y3
                if (posição[x][y][1] == 240 and posição[x][y][0] < 202) \
                        or (posição[x][y][1] == 240 and 368 <= posição[x][y][0] < 558):
                    posição[x][y][0] += 38
                # R3 -> R2 -> R1
                elif (posição[x][y][0] == 12 and posição[x][y][1] > 240):
                    posição[x][y][1] -= 44

                #  R3, Y1
                elif (posição[x][y][1] == 328 and 12 < posição[x][y][0] <= 202) \
                        or (posição[x][y][1] == 328 and 368 < posição[x][y][0]):
                    posição[x][y][0] -= 38
                #  Y3 -> Y2 -> Y1
                elif (posição[x][y][0] == 558 and posição[x][y][1] < 328):
                    posição[x][y][1] += 44

                #  G3, B1
                elif (posição[x][y][0] == 240 and 12 < posição[x][y][1] <= 202) \
                        or (posição[x][y][0] == 240 and 368 < posição[x][y][1]):
                    posição[x][y][1] -= 38
                # G3 -> G2 -> G1
                elif (posição[x][y][1] == 12 and 240 <= posição[x][y][0] < 328):
                    posição[x][y][0] += 44

                #  B3, G1
                elif (posição[x][y][0] == 328 and posição[x][y][1] < 202) \
                        or (posição[x][y][0] == 328 and 368 <= posição[x][y][1] < 558):
                    posição[x][y][1] += 38
                #  B3 -> B2 -> B1
                elif (posição[x][y][1] == 558 and posição[x][y][0] > 240):
                    posição[x][y][0] -= 44

                else:
                    for i in pulo:
                        if posição[x][y] == list(i):
                            posição[x][y] = list(pulo[i])
                            break

                mostrar_peça(x, y)

        if tuple(posição[x][y]) not in SEGURA:
            for i in range(len(posição)):
                for j in range(len(posição[i])):
                    if posição[i][j] == posição[x][y] and i != x:
                        posição[i][j] = list(CASA[i][j])
                
                        jogadorAtual = (jogadorAtual+3) % 4
                        

def verificar_vencedor():
    global jogadorAtual
    if jogadorAtual not in classificaçãoVencedor:
        for i in posição[jogadorAtual]:
            if i not in VENCEDOR:
                return
        classificaçãoVencedor.append(jogadorAtual)
    else:
        jogadorAtual = (jogadorAtual + 1) % 4

pergunta_atual = None
escolha_do_jogador = None
dadoRolado = False

executando = True
while(executando):
    screen.fill((255, 255, 255))
    screen.blit(tabuleiro, (0, 0))  

    verificar_vencedor()
    
    
    coordenada = None
    

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.MOUSEBUTTONUP:
            coordenada = pygame.mouse.get_pos()

            if not dadoRolado and (605 <= coordenada[0] <= 669) and (270 <= coordenada[1] <= 334):
                numero = random.randint(1, 6)
                
                if numero == 6 or jogadores_responderam[jogadorAtual] == True:
                    pergunta_atual = random.choice(perguntas)
                    escolha_do_jogador = None
                    cor_atual = cor[jogadorAtual]

                flag = True
                for i in range(len(posição[jogadorAtual])):
                    if tuple(posição[jogadorAtual][i]) not in CASA[jogadorAtual] and para_casa(jogadorAtual, i):
                        flag = False
                if (flag and numero == 6) or not flag:
                    dadoRolado = True
                    
                else:
                    jogadorAtual = (jogadorAtual+1) % 4
                    
            if escolha_do_jogador is None and pergunta_atual is not None:
                for i, opcao in enumerate(pergunta_atual.opcoes):
                    opcao_x = 50
                    opcao_y = 430 + i * 30
                    opcao_rect = pygame.Rect(opcao_x, opcao_y, 50, 50)

                    if opcao_rect.collidepoint(coordenada):
                        escolha_do_jogador = i  
            
            if escolha_do_jogador is not None and pergunta_atual is not None:
                if escolha_do_jogador == pergunta_atual.correta:
                    pergunta_atual = None
                    dadoRolado = True
                    jogadores_responderam[jogadorAtual] = True
                else:
                    jogadorAtual = (jogadorAtual + 1) % 4
                    pergunta_atual = None
                    dadoRolado = False

    if pergunta_atual is not None:
        texto_pergunta = fonte.render(pergunta_atual.pergunta, True, (0, 0, 0))
        screen.blit(texto_pergunta, (50, 400))

        for i, opcao in enumerate(pergunta_atual.opcoes):
            texto_opcao = fonte.render(f"{i+1}. {opcao}", True, (0, 0, 0))
            screen.blit(texto_opcao, (50, 430 + i * 30))

    if dadoRolado and coordenada is not None and escolha_do_jogador != -1 and pergunta_atual is None:
        for j in range(len(posição[jogadorAtual])):
            if posição[jogadorAtual][j][0] <= coordenada[0] <= posição[jogadorAtual][j][0]+31 \
                    and posição[jogadorAtual][j][1] <= coordenada[1] <= posição[jogadorAtual][j][1]+31:
                mover_peça(jogadorAtual, j)
                break

    

    blit_tudo()
    
    pygame.display.flip()