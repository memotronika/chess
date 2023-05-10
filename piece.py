import pygame
CELL_SIZE=60
class Piece:
    def __init__(self, color, pos, img):
        self.color = color
        self.pos = pos
        self.img = pygame.image.load(img)
        self.x, self.y = pos
    
    def draw(self, screen):
        screen.blit(self.img, (self.x*CELL_SIZE, self.y*CELL_SIZE))

class Pawn(Piece):
    def __init__(self, color, pos, img):
        super().__init__(color, pos, img)
        self.direction = -1 if self.color == 'black' else 1  # пешки белых ходят вверх, черных - вниз
        self.first_move = True  # флаг, указывающий, делала ли пешка первый ход

    def get_possible_moves(self, board):
        x, y = self.pos
        moves = []

        # Проверяем клетку перед пешкой
        if board[x][y + self.direction] is None:
            moves.append((x, y + self.direction))
            # Если это первый ход пешки, то она может пойти на две клетки вперед
            if self.first_move and board[x][y + 2 * self.direction] is None:
                moves.append((x, y + 2 * self.direction))

        # Проверяем бью ли пешка фигуру по диагонали
        if 0 <= x - 1 < 8 and board[x - 1][y + self.direction] is not None and board[x - 1][y + self.direction].color != self.color:
            moves.append((x - 1, y + self.direction))
        if 0 <= x + 1 < 8 and board[x + 1][y + self.direction] is not None and board[x + 1][y + self.direction].color != self.color:
            moves.append((x + 1, y + self.direction))

        return moves


class Rook(Piece):
    def __init__(self, color, pos, img):
        super().__init__(color, pos, img)
        self.has_moved = False

    def get_possible_moves(self, board):
        moves = []
        x, y = self.pos
        for i in range(x+1, 8):
            if board[i][y] is None:
                moves.append((i, y))
            else:
                if board[i][y].color != self.color:
                    moves.append((i, y))
                break
        for i in range(x-1, -1, -1):
            if board[i][y] is None:
                moves.append((i, y))
            else:
                if board[i][y].color != self.color:
                    moves.append((i, y))
                break
        for j in range(y+1, 8):
            if board[x][j] is None:
                moves.append((x, j))
            else:
                if board[x][j].color != self.color:
                    moves.append((x, j))
                break
        for j in range(y-1, -1, -1):
            if board[x][j] is None:
                moves.append((x, j))
            else:
                if board[x][j].color != self.color:
                    moves.append((x, j))
                break
        return moves

class Knight(Piece):
    def __init__(self, color, pos, img):
        super().__init__(color, pos, img)

    def get_possible_moves(self, board):
        moves = []
        x, y = self.pos
        for dx, dy in [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]:
            if 0 <= x+dx < 8 and 0 <= y+dy < 8 and (board[x+dx][y+dy] is None or board[x+dx][y+dy].color != self.color):
                moves.append((x+dx, y+dy))
        return moves

class Bishop(Piece):
    def __init__(self, color, pos, img):
        super().__init__(color, pos, img)

    def get_possible_moves(self, board):
        moves = []
        x, y = self.pos
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board[new_x][new_y] is None:
                        moves.append((new_x, new_y))
                    elif board[new_x][new_y].color != self.color:
                        moves.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break
        return moves

class Queen(Piece):
    def __init__(self, color, pos, img):
        super().__init__(color, pos, img)

    def get_possible_moves(self, board):
        moves = []
        rook = Rook(self.color, self.pos, self.img)
        bishop = Bishop(self.color, self.pos, self.img)
        moves += rook.get_possible_moves(board)
        moves += bishop.get_possible_moves(board)
        return moves

class King(Piece):
    def __init__(self, color, pos, img):
        super().__init__(color, pos, img)

    def get_possible_moves(self, board):
        moves = []
        x, y = self.pos
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board[new_x][new_y] is None or board[new_x][new_y].color != self.color:
                    moves.append((new_x, new_y))
        return moves
