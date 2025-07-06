import pygame
import random

# Initialize pygame
pygame.init()

# Screen
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player
player_width, player_height = 50, 30
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - 50
player_speed = 5

# Bullet
bullet_width, bullet_height = 5, 10
bullet_speed = 7
bullets = []

# Enemies
enemy_width, enemy_height = 40, 30
enemy_speed = 2
enemies = []
for i in range(5):  # start with 5 enemies
    x = random.randint(0, screen_width - enemy_width)
    y = random.randint(50, 150)
    enemies.append([x, y])


score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # FPS
    screen.fill((0, 0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # limit bullets on screen
            bullets.append([player_x + player_width//2, player_y])

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed
    bullets = [b for b in bullets if b[1] > 0]

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemy[1] = random.randint(-100, -40)
            enemy[0] = random.randint(0, screen_width - enemy_width)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, GREEN, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Check for collisions
    for bullet in bullets:
        bx, by = bullet
        for enemy in enemies:
            ex, ey = enemy
            if (bx > ex and bx < ex + enemy_width) and (by > ey and by < ey + enemy_height):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                # Spawn a new enemy
                x = random.randint(0, screen_width - enemy_width)
                y = random.randint(-100, -40)
                enemies.append([x, y])
                break

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
