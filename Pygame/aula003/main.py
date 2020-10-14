import pygame

pygame.init()

display = pygame.display.set_mode([880,880])

pygame.display.set_caption('Meu Jogo Aula 3')

def draw (rgb):
    display.fill(rgb)

isPressingw = False
if __name__ == '__main__':

    gameloop = True
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            
        keys= pygame.key.get_pressed()

        if keys[pygame.K_w]:
            print('pega')
            '''
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    isPressingw = True
                    print('indo Para frente')

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    isPressingw = False
                    print('Parou de andar')                        
            ''' 

        draw([2, 230, 222])
        pygame.display.update()
