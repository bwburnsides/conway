import random
from itertools import product
import pygame as pg

## CONFIG --------------------------
seed = 80085_1015  # must be int or None for random
size = width, height = 680, 520  # Window size [px]
cell_size = 20  # [px]
initial_alive = 300  # The initial number of alive cells
fps = 8  # slower is better so that you see the changes better
## ---------------------------------


def update_cells(universe, live_cells, neighbors):
    next_gen = set()
    for cell in universe:
        ct = sum(tuple(map(sum, zip(cell, neigh))) in live_cells for neigh in neighbors)
        if ct == 3 or (cell in live_cells and ct == 2):
            next_gen.add(cell)
    return next_gen


def draw_cells(surf, universe, live_cells):
    for cell in universe:
        pg.draw.rect(
            surf,
            pg.Color("black"),
            pg.Rect(cell[0] * cell_size, cell[1] * cell_size, cell_size, cell_size),
            width=0 if cell in live_cells else 1,
        )


def main(screen_size, initial_alive, seed):
    random.seed(seed)
    pg.init()
    pg.display.set_caption("BWB Conways Game of Life")
    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()

    universe = {
        pos for pos in product(range(width // cell_size), range(height // cell_size))
    }
    neighbors = {pos for pos in product((-1, 0, 1), repeat=2) if pos != (0, 0)}
    cells = set(random.sample(tuple(universe), min(initial_alive, len(universe))))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill(pg.Color("white"))

        cells = update_cells(universe, cells, neighbors)
        draw_cells(screen, universe, cells)

        pg.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main(size, initial_alive, seed)
