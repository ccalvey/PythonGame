import random

import pygame
import time

pygame.init()


#SCREEN PROPERTIES
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Project!!!")

#PLAYER PROPERTIES
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
CHARACTER_X = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
CHARACTER_Y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
PLAYER_VEL = 5


#ENEMY PROPERTIES
enemies = []
BLOCK_ADD = 2000
BLOCK_COUNT = 0
BLOCK_WIDTH = 10
BLOCK_HEIGHT = 15
BLOCK_VEL = 3

#COLORS AND FONT
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 74)

def main():
    run = True
    clock = pygame.time.Clock()
    frame_count = 0
    block_spawn_time = 30
    character_x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
    character_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
    hit = False


    while run:

        clock.tick(60) #MAKES USER SLOWER OR FASTER
        frame_count += 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

         #MOVE CHARACTER AND SET PLAYER BOUNDARIES
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and character_x - PLAYER_VEL >= 0:
            character_x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and character_x + PLAYER_VEL + PLAYER_WIDTH <= SCREEN_WIDTH:
            character_x += PLAYER_VEL
        if keys[pygame.K_UP] and character_y - PLAYER_VEL >= 0:
            character_y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and character_y + PLAYER_VEL + PLAYER_WIDTH <= SCREEN_HEIGHT:
            character_y += PLAYER_VEL

        #SPAWN ENEMIES
        if frame_count % block_spawn_time == 0:
            enemy_x = random.randint(0, SCREEN_WIDTH - BLOCK_WIDTH)
            enemies.append([enemy_x, 0])

            # MOVES ENEMIES
        for enemy in enemies[:]:
            enemy[1] += BLOCK_VEL
            if enemy[1] > SCREEN_HEIGHT:
                enemies.remove(enemy)

            # DETECTS COLLISIONS
            if (
                character_x < enemy[0] + BLOCK_WIDTH and
                character_x + PLAYER_WIDTH > enemy[0] and
                character_y < enemy[1] + BLOCK_HEIGHT and
                character_y + PLAYER_HEIGHT > enemy[1]
            ):
                hit = True


        SCREEN.fill(BLACK)  # IMPORTANT CLEARS PREVIOUS SCREEN!!!
        pygame.draw.rect(SCREEN, RED, (character_x, character_y, PLAYER_WIDTH, PLAYER_HEIGHT))  # Draw the player
        for enemy in enemies:
            pygame.draw.rect(SCREEN, WHITE, (enemy[0], enemy[1], BLOCK_WIDTH, BLOCK_HEIGHT))  # Draw blocks

            #COLLISION
        if hit:
            game_over_text = font.render("Game Over!", True, RED)
            SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()


