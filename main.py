from enum import Enum
from dataclasses import dataclass
from math import floor


class Piece(str, Enum):
    PAWN = '♙'
    BISHOP = '♗'
    KNIGHT = '♘'
    ROOK = '♖'
    QUEEN = '♕'
    KING = '♔'
    EMPTY = ' '


class Alignment(Enum):
    WHITE = 0
    BLACK = 1


@dataclass
class Square:
    piece : Piece
    alignment : Alignment


    def __str__(self) -> str:
        if self.piece == Piece.EMPTY:
            return '.'
        
        if self.alignment == Alignment.BLACK:
            return chr(ord(self.piece.value[0]) + 6)
        
        return self.piece.value


class Board:
    def __init__(self) -> None:
        self._data = tuple(Square(Piece.EMPTY, Alignment.WHITE) for _ in range(8*8))

        for column in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            for row in (7, 8):
                self.get(column, row).alignment = Alignment.BLACK

        for column in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            for row in (2, 7):
                self.get(column, row).piece = Piece.PAWN

        for row in (1, 8):
            for column in ('a', 'h'):
                self.get(column, row).piece = Piece.ROOK
            
            for column in ('b', 'g'):
                self.get(column, row).piece = Piece.KNIGHT
            
            for column in ('c', 'f'):
                self.get(column, row).piece = Piece.BISHOP
            
            self.get('d', row).piece = Piece.QUEEN
            self.get('e', row).piece = Piece.KING

        self.turn = Alignment.WHITE


    def get(self, column : str, row : int) -> Square:
        column : int = 7 - int(ord(column[0]) - 97)
        return self._data[column + 8 * (row - 1)]


    def __str__(self) -> str:
        out = ''

        data = self._data if self.turn == Alignment.BLACK else reversed(self._data)

        for index, value in enumerate(data):
            if index % 8 == 0:
                if index != 0:
                    out += '\n'
                out += f'{8 - floor(index / 8):<2}' if self.turn == Alignment.WHITE else f'{floor(index / 8) + 1:<2}'
            out += f'{str(value):2}'

        out += f'\n{"":<2}'
        letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

        if self.turn == Alignment.BLACK:
            letters = reversed(letters)

        for value in letters:
            out += f'{value:2}'

        return out


def main():
    board = Board()
    
    while True:
        print(str(board))
        square_to_move_from = input(f'Select Piece: ')
        if square_to_move_from.lower() == 'q':
            break

        square_to_move_from = board.get(square_to_move_from[0], int(square_to_move_from[1]))

        square_to_move_to = input(f'Select Square to Move to: ')
        if square_to_move_to.lower() == 'q':
            break

        square_to_move_to = board.get(square_to_move_to[0], int(square_to_move_to[1]))

        square_to_move_to.piece = square_to_move_from.piece
        square_to_move_to.alignment = square_to_move_from.alignment
        square_to_move_from.piece = Piece.EMPTY

        board.turn = Alignment.BLACK if board.turn == Alignment.WHITE else Alignment.WHITE


if __name__ == '__main__':
    main()