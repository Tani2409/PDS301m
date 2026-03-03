import pygame
import random

# Kích thước màn hình
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Màu sắc
COLORS = [
    (0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255),
    (255, 255, 0), (255, 165, 0), (128, 0, 128)
]

# Hình dạng gạch
SHAPES = [
    [[1, 1, 1, 1]],  # Hình chữ I
    [[1, 1], [1, 1]],  # Hình vuông
    [[0, 1, 0], [1, 1, 1]],  # Hình chữ T
    [[1, 1, 0], [0, 1, 1]],  # Hình chữ Z
    [[0, 1, 1], [1, 1, 0]]  # Hình chữ S
]


class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS[1:])  # Tránh màu đen
        self.x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]


def draw_board(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != 0:
                pygame.draw.rect(screen, COLORS[board[y][x]],
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    piece = Piece()

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_board(board)

        # Vẽ gạch hiện tại
        for i, row in enumerate(piece.shape):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, piece.color,
                                     ((piece.x + j) * BLOCK_SIZE, (piece.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()