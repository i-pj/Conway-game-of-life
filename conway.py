import pygame
import random

WIDTH, HEIGHT = 800, 600

CELL_SIZE = 10

ALIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (0, 0, 0)

class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[random.choice([0, 1]) for _ in range(width // cell_size)] for _ in range(height // cell_size)]

    def draw_grid(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = ALIVE_COLOR if cell else DEAD_COLOR
                pygame.draw.rect(screen, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def count_neighbors(self, x, y):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbors += self.grid[(y + i) % len(self.grid)][(x + j) % len(self.grid[0])]
        return neighbors

    def next_generation(self):
        new_grid = [[0 for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                neighbors = self.count_neighbors(x, y)
                if cell and (neighbors < 2 or neighbors > 3):
                    new_grid[y][x] = 0
                elif cell and (neighbors == 2 or neighbors == 3):
                    new_grid[y][x] = 1
                elif not cell and neighbors == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
        self.grid = new_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = GameOfLife(WIDTH, HEIGHT, CELL_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(DEAD_COLOR)
        game.draw_grid(screen)
        game.next_generation()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
