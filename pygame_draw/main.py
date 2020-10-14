import pygame

pygame.init()

display = pygame.display.set_mode([880,880])
pygame.display.set_caption('AULA 004')

drawGrup = pygame.sprite.Group()

guy = pygame.sprite.Sprite(drawGrup)
guy.image = pygame.image.load("./imagem/cara_triste.png")
# Redimencionando a imagem (guy.image)
guy.image = pygame.transform.scale(guy.image, [100,100])
guy.rect = pygame.Rect(50,50,100,100)

if __name__ == '__main__':
    gameloop = True
    while gameloop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False   

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            guy.rect.y += 1
            print('Indo para cima')

        if keys[pygame.K_s]:
            guy.rect.y -= 1
            print('Indo para baixo')
        if keys[pygame.K_d]:
            guy.rect.x += 1
            print('andando')
        
        if keys[pygame.K_a]:
            guy.rect.x -= 1
            print("andando para tras")
        
        # draw               x   y     w   h 
        '''
        player = pygame.Rect(50 ,50 , 90, 100)
        player.center = [50,50]
        pygame.draw.rect(display,[22,44,90],player)
        '''
        pygame.display.update()
        display.fill([2, 230, 222])
        drawGrup.draw(display)
