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
        for i in range(16):
            self._data[i + 8*0].alignment = Alignment.BLACK

        for i in range(8):
            self._data[i + 8*1].piece = Piece.PAWN
            self._data[i + 8*6].piece = Piece.PAWN

        for i in (0 + 8*0, 7 + 8*0, 0 + 8*7, 7 + 8*7):
            self._data[i].piece = Piece.ROOK
        for i in (1 + 8*0, 6 + 8*0, 1 + 8*7, 6 + 8*7):
            self._data[i].piece = Piece.KNIGHT
        for i in (2 + 8*0, 5 + 8*0, 2 + 8*7, 5 + 8*7):
            self._data[i].piece = Piece.BISHOP
            
        for i in (3 + 8*0, 3 + 8*7):
            self._data[i].piece = Piece.QUEEN
        for i in (4 + 8*0, 4 + 8*7):
            self._data[i].piece = Piece.KING

        self.turn = Alignment.WHITE
    

    def __str__(self) -> str:
        out = ''

        data = self._data if self.turn == Alignment.WHITE else reversed(self._data)

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
    print(str(board))
    


if __name__ == '__main__':
    main()