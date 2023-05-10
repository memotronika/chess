import pygame
from piece import *



# определяем размер ячеек доски и размер шрифта для разметки
CELL_SIZE = 60
FONT_SIZE = 15

# инициализируем Pygame
pygame.init()

# создаем окно приложения
screen = pygame.display.set_mode((CELL_SIZE*8, CELL_SIZE*8))
pygame.display.set_caption('Chess')

# загружаем шрифт для разметки
font = pygame.font.SysFont('Arial', 16, bold=True)


# создаем функцию для рисования ячейки на доске
def draw_cell(x, y, color):
    rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

# создаем шахматную доску
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            draw_cell(i, j, (255, 255, 255))
        else:
            draw_cell(i, j, (128, 128, 128))



# загружаем изображения фигур
b_pawn_img = pygame.image.load('b_pawn.png')
w_pawn_img = pygame.image.load('w_pawn.png')
b_rook_img = pygame.image.load('b_rook.png')
w_rook_img = pygame.image.load('w_rook.png')
b_knight_img = pygame.image.load('b_knight.png')
w_knight_img = pygame.image.load('w_knight.png')
b_bishop_img = pygame.image.load('b_bishop.png')
w_bishop_img = pygame.image.load('w_bishop.png')
b_queen_img = pygame.image.load('b_queen.png')
w_queen_img = pygame.image.load('w_queen.png')
b_king_img = pygame.image.load('b_king.png')
w_king_img = pygame.image.load('w_king.png')

# создаем фигуры

pieces = [
Rook('black', (0, 0), 'b_rook.png'),
Knight('black', (1, 0), 'b_knight.png'),
Bishop('black', (2, 0), 'b_bishop.png'),
Queen('black', (3, 0), 'b_queen.png'),
King('black', (4, 0), 'b_king.png'),
Bishop('black', (5, 0), 'b_bishop.png'),
Knight('black', (6, 0), 'b_knight.png'),
Rook('black', (7, 0), 'b_rook.png'),
Pawn('black', (0, 1), 'b_pawn.png'),
Pawn('black', (1, 1), 'b_pawn.png'),
Pawn('black', (2, 1), 'b_pawn.png'),
Pawn('black', (3, 1), 'b_pawn.png'),
Pawn('black', (4, 1), 'b_pawn.png'),
Pawn('black', (5, 1), 'b_pawn.png'),
Pawn('black', (6, 1), 'b_pawn.png'),
Pawn('black', (7, 1), 'b_pawn.png'),
Rook('white', (0, 7), 'w_rook.png'),
Knight('white', (1, 7), 'w_knight.png'),
Bishop('white', (2, 7), 'w_bishop.png'),
Queen('white', (3, 7), 'w_queen.png'),
King('white', (4, 7), 'w_king.png'),
Bishop('white', (5, 7), 'w_bishop.png'),
Knight('white', (6, 7), 'w_knight.png'),
Rook('white', (7, 7), 'w_rook.png'),
Pawn('white', (0, 6), 'w_pawn.png'),
Pawn('white', (1, 6), 'w_pawn.png'),
Pawn('white', (2, 6), 'w_pawn.png'),
Pawn('white', (3, 6), 'w_pawn.png'),
Pawn('white', (4, 6), 'w_pawn.png'),
Pawn('white', (5, 6), 'w_pawn.png'),
Pawn('white', (6, 6), 'w_pawn.png'),
Pawn('white', (7, 6), 'w_pawn.png')
]


for piece in pieces:
    piece.draw(screen)

# добавляем шкалу разметки a-h
for i, letter in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
    text = font.render(letter, True, (0, 0, 0))
    text_rect = text.get_rect(center=((i+0.8)*CELL_SIZE, CELL_SIZE*8-FONT_SIZE/2))
    screen.blit(text, text_rect)

# добавляем шкалу разметки 1-8
for i in range(8):
    number = font.render(str(8-i), True, (0, 0, 0))
    number_rect = number.get_rect(center=(FONT_SIZE/2, (i+0.2)*CELL_SIZE))
    screen.blit(number, number_rect)

pygame.display.flip()


def get_piece_clicked(pieces, pos):
    for piece in pieces:
        if piece.rect.collidepoint(pos):
            return piece
    return None



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # определяем, в какую ячейку доски было сделано нажатие
            pos = pygame.mouse.get_pos()
            row, col = get_cell_clicked(pos)

            # если мы уже выбрали фигуру, то перемещаем ее на новую позицию
            if selected_piece:
                success = selected_piece.move(board, row, col)
                if success:
                    turn = 'black' if turn == 'white' else 'white'
                selected_piece = None

            # если фигура не выбрана, то пытаемся выбрать фигуру на этой позиции
            else:
                piece = get_piece_clicked(pieces, pos)
                if piece and piece.color == turn:
                    selected_piece = piece

    # отрисовываем доску и фигуры
    draw_board(screen)
    for piece in pieces:
        piece.draw(screen)

    pygame.display.update()

    # задаем FPS
    clock.tick(FPS)
