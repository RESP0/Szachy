import abc
from Team import Team
from pieces.Piece import Piece


class Player (metaclass=abc.ABCMeta):

    def __init__(self, team: Team) -> None:
        self.__points: int = 0
        self.__team: Team = team
        self.__taken_pieces: list[Piece] = []

    def takes(self, piece: Piece) -> None | RuntimeError:
        if piece.get_team() is self.__team:
            return RuntimeError(f'Player {self} cannot take piece {piece}, because the piece is in his team')

        self.__points += piece.get_value()
        self.__taken_pieces.append(piece)

    def get_points(self):
        return self.__points

    def get_team(self):
        return self.__team

    def get_taken_pieces(self):
        return self.__taken_pieces
