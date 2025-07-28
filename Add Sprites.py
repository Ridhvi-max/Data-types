import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("One Sprite Controlled")
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 100, 50, 50)
color1 = (255, 0, 0)
color2 = (0, 0, 255)
bg = (0, 0, 0)
speed = 5
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect1.x > 0: rect1.x -= speed
    if keys[pygame.K_RIGHT] and rect1.x < 800 - rect1.width: rect1.x += speed
    if keys[pygame.K_UP] and rect1.y > 0: rect1.y -= speed
    if keys[pygame.K_DOWN] and rect1.y < 600 - rect1.height: rect1.y += speed
    pygame.draw.rect(screen, color1, rect1)
    pygame.draw.rect(screen, color2, rect2)
    pygame.display.flip()
pygame.quit()

