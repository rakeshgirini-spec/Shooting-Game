import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

clock = pygame.time.Clock()

player = pygame.Rect(50, 200, 40, 40)
bullets = []
enemies = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.x+40, player.y+20, 10, 5))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    for bullet in bullets[:]:
        bullet.x += 7
        if bullet.x > WIDTH:
            bullets.remove(bullet)

    if random.randint(1, 30) == 1:
        enemies.append(pygame.Rect(WIDTH, random.randint(0, HEIGHT-40), 40, 40))

    for enemy in enemies[:]:
        enemy.x -= 4
        if enemy.x < 0:
            enemies.remove(enemy)
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()
    clock.tick(60)
