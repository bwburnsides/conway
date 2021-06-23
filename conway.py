import random
from itertools import product
import pygame as pg

## CONFIG --------------------------
seed = 80085_1015  # must be int
size = width, height = 680, 520  # Window size [px]
cell_size = 20  # [px]
starting_cells = 300  # The initial number of alive cells
fps = 8  # slower is better so that you see the changes better
## ---------------------------------

universe = {
    pos for pos in product(range(0, width // cell_size), range(0, height // cell_size))
}
neighbors = {pos for pos in product([-1, 0, 1], repeat=2) if pos != (0, 0)}


def update_cells(live_cells):
    new_cells = set()
    for cell in universe:
        ct = sum(
            (cell[0] + neighbor[0], cell[1] + neighbor[1]) in live_cells
            for neighbor in neighbors
        )
        if ct == 3 or (cell in live_cells and ct == 2):
            new_cells.add(cell)
    return new_cells


def draw_cells(cells):
    for cell in universe:
        width = 0 if cell in cells else 1

        pg.draw.rect(
            screen,
            pg.Color("black"),
            pg.Rect(cell[0] * cell_size, cell[1] * cell_size, cell_size, cell_size),
            width=width,
        )


def main():
    cells = set(random.sample(tuple(universe), starting_cells))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill(pg.Color("white"))

        cells = update_cells(cells)
        draw_cells(cells)

        pg.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    random.seed(seed)
    pg.init()
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    pg.display.set_caption("BWB Conways Game of Life")
    main()
