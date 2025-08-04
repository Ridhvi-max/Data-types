import pygame, random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Enemies")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
pygame.mixer.init()
collision_sound = pygame.mixer.Sound("collision.wav")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset_pos()
    def reset_pos(self):
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, HEIGHT - 30)

player = Player()
enemies = pygame.sprite.Group()
for _ in range(7):
    enemies.add(Enemy())

all_sprites = pygame.sprite.Group(player, *enemies)

running = True
while running:
    screen.blit(bg, (0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update(keys)
    collided = pygame.sprite.spritecollide(player, enemies, False)
    for enemy in collided:
        score += 1
        collision_sound.play()
        enemy.reset_pos()
    all_sprites.draw(screen)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
