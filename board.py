import pygame
import random

height = 100
width = 100
screenSize = 500
density = 0.5
influence = 1

TILE_WATER = (20, 40, 120)
TILE_LAND = (50, 160, 80)
BG_COLOR = (10, 10, 20)

cell_size = screenSize // width

# creates a 2d array of 0s with dimensions width x height
map = [[0 for _ in range(height)] for _ in range(width)]


# Procedurally generates a map with random values between 0 and 1
def generate_map():
    for x in range(width):
        for y in range(height):
            map[x][y] = 1 if random.random() < density else 0

    for x in range(width):
        for y in range(height):
            count = 0
            for i in range(-influence, influence + 1):
                for j in range(-influence, influence + 1):
                    if 0 <= x + i < width and 0 <= y + j < height:
                        count += map[x + i][y + j]

            if map[x][y] == 1 and count <= 2:
                map[x][y] = 0
            elif map[x][y] == 0 and count >= 6:
                map[x][y] = 1


def draw_map(surface):
    surface.fill(BG_COLOR)
    for x in range(width):
        for y in range(height):
            color = TILE_LAND if map[x][y] == 1 else TILE_WATER
            pygame.draw.rect(
                surface,
                color,
                (x * cell_size, y * cell_size, cell_size, cell_size),
            )


def main():
    pygame.init()
    screen = pygame.display.set_mode((screenSize, screenSize))
    pygame.display.set_caption("Procedural Map")
    clock = pygame.time.Clock()

    generate_map()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_map()

        draw_map(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()