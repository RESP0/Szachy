import Position
from pieces.Piece import Piece


class Field:

    def __init__(self, position: Position, piece: Piece) -> None:
        self.__position = position
        self.__piece = piece

    def get_piece(self):
        return self.__piece

    def get_position(self):
        return self.__position

    def set_piece(self, piece: Piece):
        self.__piece = piece

    def __str__(self) -> str:
        return f"Position:{self.__position}, piece:{self.__piece}"

