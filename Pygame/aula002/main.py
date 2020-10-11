import pygame 


pygame.init()

# Inicializndo o pygame
display = pygame.display.set_mode([880,880])

# Criando a janela
pygame.display.set_caption("TESTE")

def draw(rgb):
    display.fill(rgb)

if __name__ == '__main__':

    # Atualizando a janela em tempo real
    gameloop = True
    while gameloop:
        # Fill o Display Com cores Padrão (RGB)
        draw([2, 230, 222])
        pygame.display.update()

