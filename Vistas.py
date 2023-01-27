import pygame
from AStar import AStar
from PIL import Image

from BFS import BFS
from DFS import DFS


def draw_rect(x, y, color, screen, blocksize, H):
    """Draws a cube of size blockize-1 in the grid"""
    screen.fill(color, (x * blocksize, H - y * blocksize, blocksize, blocksize))


def paint_grid(GRID, screen, blocksize, H):
    """Re-paints the pixels of the grid that have changed"""
    for y in range(len(GRID)):
        for x in range(len(GRID)):
            if GRID[y][x] == 0:
                draw_rect(y, x, (255, 255, 255), screen, blocksize, H)
            elif GRID[y][x] == 1:
                draw_rect(y, x, (0, 255, 0), screen, blocksize, H)
            elif GRID[y][x] == 2:
                draw_rect(y, x, (0, 0, 0), screen, blocksize, H)
            elif GRID[y][x] == 3:
                draw_rect(y, x, (255, 0, 0), screen, blocksize, H)
            elif GRID[y][x] == 5:
                draw_rect(y, x, (100, 50, 50), screen, blocksize, H)
            elif GRID[y][x] == 4:
                draw_rect(y, x, (255, 0, 255), screen, blocksize, H)


# ---- Main ----
def runAstar(Resultado: list[list[int]]) -> None:
    W, H = (600, 600)
    blocksize = int(600 / len(Resultado))
    GRID = Resultado

    A_instance = AStar(Resultado)
    A_instance.setHeuristic()

    pygame.display.set_caption("Resolución de laberinto")
    screen = pygame.display.set_mode((W, H))
    pygame.init()

    running = True

    paint_grid(GRID, screen, blocksize, H)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in [pygame.KEYDOWN]:
                if not A_instance.goalTests():
                    A_instance.action("")
                    GRID = A_instance.results("", "")
                paint_grid(GRID, screen, blocksize, H)
                pygame.display.update()
    # Save last frame as image:
    pygame.image.save(screen, "AStar.png")
    Image.open("AStar.png").show()


def runBFS(Resultado: list[list[int]]) -> None:
    W, H = (600, 600)
    blocksize = int(600 / len(Resultado))
    GRID = Resultado

    BFS_Instance = BFS(Resultado)

    pygame.display.set_caption("Resolución de laberinto")
    screen = pygame.display.set_mode((W, H))
    pygame.init()

    running = True

    paint_grid(GRID, screen, blocksize, H)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in [pygame.KEYDOWN]:
                if not BFS_Instance.goalTests():
                    BFS_Instance.action("")
                    GRID = BFS_Instance.results("", "")
                paint_grid(GRID, screen, blocksize, H)
                pygame.display.update()
    pygame.image.save(screen, "BFS.png")
    Image.open("BFS.png").show()


def runDFS(Resultado: list[list[int]]) -> None:
    W, H = (600, 600)
    blocksize = int(600 / len(Resultado))
    GRID = Resultado

    DFS_Instance = DFS(Resultado)

    pygame.display.set_caption("Resolución de laberinto")
    screen = pygame.display.set_mode((W, H))
    pygame.init()

    running = True

    paint_grid(GRID, screen, blocksize, H)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in [pygame.KEYDOWN]:
                if not DFS_Instance.goalTests():
                    DFS_Instance.action("")
                    GRID = DFS_Instance.results("", "")
                paint_grid(GRID, screen, blocksize, H)
                pygame.display.update()

    pygame.image.save(screen, "DFS.png")
    Image.open("DFS.png").show()
