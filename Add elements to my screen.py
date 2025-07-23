import pygame, sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game Screen")
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to the Game!", True, (255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 102, 204))
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 100))
    pygame.draw.rect(screen, (0, 255, 0), (400, 300, 150, 200))
    screen.blit(text, (250, 20))
    pygame.display.flip()
pygame.quit()
sys.exit()
