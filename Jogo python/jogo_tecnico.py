import pygame
import random
from ppt_sistema import rodar_jogo

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
run = True

texto_resultado = 'Pedra, Papel, Tesoura'

resultado = 0
clicking = False
jogada = ''

while run:
    clock.tick(120)
    
    pygame.display.set_caption('Pedra, Papel, Tesoura.')
    
    fundo_img = pygame.transform.scale(pygame.image.load('imagens/pixilart-fundo.png').convert_alpha(), (800, 600))
    screen.blit(fundo_img, (0, 0))
    
    # Rect e texto do título
    fonte = pygame.font.SysFont('Monospace', 35, True, False)
    texto = fonte.render(texto_resultado, False, (0, 0, 0))
    screen.blit(texto,(150, 125))
    
    pedra_img = pygame.transform.scale(pygame.image.load('imagens/pixilart-pedra.png').convert_alpha(), (200, 200))
    butao1 = pygame.Rect(50, 400, 200, 100) 
    screen.blit(pedra_img, (50, 360))

    papel_img = pygame.transform.scale(pygame.image.load('imagens/pixilart-papel.png').convert_alpha(), (180, 160))
    butao2 = pygame.Rect(300, 400, 200, 100)
    screen.blit(papel_img, (300, 370))
    
    tesoura_img = pygame.transform.scale(pygame.image.load('imagens/pixilart-tesoura.png').convert_alpha(), (220, 220))
    butao3 = pygame.Rect(550, 400, 200, 100)
    screen.blit(tesoura_img, (550, 340))
    
    mouse_pos = pygame.mouse.get_pos()
    
    if clicking:
        if butao1.collidepoint(mouse_pos) and clicking:
            resultado = rodar_jogo(1)
            jogada = 'pedra'
            
        if butao2.collidepoint(mouse_pos) and clicking:
            resultado = rodar_jogo(2)
            jogada = 'papel'
        
        if butao3.collidepoint(mouse_pos) and clicking:
            resultado = rodar_jogo(3)
            jogada = 'tesoura'
            
        if resultado == 1:
            texto_resultado = f'Você jogou {jogada} e ganhou!'
        elif resultado == 2:
            texto_resultado = f'Você jogou {jogada} e perdeu!'
        elif resultado == 3:
            texto_resultado = f'Você jogou {jogada} e empatou!'
        else:
            texto_resultado = 'Pedra, Papel, Tesoura'
    
    clicking = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicking = True
            
    pygame.display.update()
    
pygame.quit()
    