import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()#Inicia pygame
pygame.mixer.music.set_volume(0.1)#Define volume da música de fundo
musica_de_fundo=pygame.mixer.music.load('fundo.mp3')#Carrega música de fundo
pygame.mixer.music.play(-1)#Toca música de fundo
barulho_colisao=pygame.mixer.Sound('smw_stomp.wav')#Define barulho da colisão
largura=640#largura da tela
altura=480#altura da tela
x_cobra=int(largura/2)#Posição x da cobra
y_cobra=int(altura/2)#Posição y da cobra
x_maca=randint(40, 600)#Posição x da maça
y_maca=randint(50, 430)#posição y da maça
pontos=0#Pontos do game
comprimento=5#Comprimento da cobra
velocidade=6#Velocidade da cobra
xControle=velocidade#Controle do movimento no eixo x da cobra
yControle=0#Controle do movimento no eixo y da cobra
fonte=pygame.font.SysFont('arial', 40, bold=True, italic=True)#Define fonte para texto
tela=pygame.display.set_mode((largura, altura))#Define tamanho da tela
pygame.display.set_caption('Cobrinha')#Define nome do jogo
relogio=pygame.time.Clock()#Define objeto referente ao tempo de atualizaçao do game
lista_cobra=[]#Define lista que representa a cobra
morreu=False
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))
def reiniciarJogo():
    global pontos, comprimento, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos=0
    comprimento=5
    x_cobra=int(largura/2)
    y_cobra=int(altura/2)
    lista_cobra=[]
    lista_cabeca=[]
    x_maca=randint(40, 600)
    y_maca=randint(50,430)
    morreu=False
while True:
    relogio.tick(60)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if(xControle==velocidade):
                    pass
                else:
                    xControle=-velocidade
                    yControle=0
            if event.key == K_d:
                if(xControle==-velocidade):
                    pass
                else:
                    xControle=velocidade
                    yControle=0
            if event.key == K_w:
                if(yControle==velocidade):
                    pass
                else:
                    xControle=0
                    yControle=-velocidade
            if event.key == K_s:
                if(yControle==-velocidade):
                    pass
                else:
                    xControle=0
                    yControle=velocidade
    x_cobra=x_cobra+xControle
    y_cobra=y_cobra+yControle
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    if(x_cobra>=largura):
        x_cobra=1
    if(x_cobra<=0):
        x_cobra=largura
    if(y_cobra>=altura):
        y_cobra=1
    if(y_cobra<=0):
        y_cobra=altura
    if cobra.colliderect(maca):
        x_maca=randint(40, 600)
        y_maca=randint(50, 430)
        pontos+=1
        comprimento+=4
        barulho_colisao.play()
    lista_cabeca=[]
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca)>1:
        morreu=True
        fonte2=pygame.font.SysFont('arial', 20, True, True)
        mensagem="Game over! Pressione a tecla \"R\" para jogar novamente"
        texto_formatado=fonte2.render(mensagem, True, (0,0,0))
        retTexto=texto_formatado.get_rect()
        while(morreu==True):
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                if event.type==KEYDOWN:
                    if event.key==K_r:
                        reiniciarJogo()
            retTexto.center=(largura//2, altura//2)
            tela.blit(texto_formatado, retTexto)
            pygame.display.update()
    if len(lista_cobra)>comprimento:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (450,40))
    pygame.display.update()