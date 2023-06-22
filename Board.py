from Field import Field
from Position import Position
from pieces.Rook import Rook
from pieces.Knight import Knight
from pieces.Bishop import Bishop
from pieces.Queen import Queen
from pieces.King import King
from pieces.Pawn import Pawn
from Team import Team


class Board:

    BOARD = "board"
    LENGTH = "length"
    HEIGHT = "height"

    def __init__(self, length: int, height: int) -> None:
        configuration = self.__get_configuration(length, height)
        self.__board: list[list[Field]] = configuration[Board.BOARD]
        self.__length = configuration[Board.LENGTH]
        self.__height = configuration[Board.HEIGHT]

    def __get_configuration(self, length: int, height: int) -> dict:
        return {
            Board.BOARD: self.__init_board(length, height),
            Board.LENGTH: length,
            Board.HEIGHT: height
        }

    def get_pieces(self, team: Team):
        all_fields = list(field for sublist in self.__board for field in sublist)
        all_fields = filter(lambda field: field.get_piece() is not None and field.get_piece().get_team() is team, all_fields)
        return all_fields

    def __init_board(self, length: int, height: int) -> list[list[Field]]:
        board: list[list[Field]] = [[None for _ in range(length)] for _ in range(height)]

        for row in range(height):
            team: Team = Team.WHITE if row <= 3 else Team.BLACK
            for column in range(length):
                letter: str = chr(97 + column)

                if row <= 1 or row >= 6:

                    if letter in ['a', 'h'] and row in [0, 7]:
                        board[row][column] = Field(Position(row, column),
                                                   Rook(team))

                    elif letter in ['b', 'g'] and row in [0, 7]:
                        board[row][column] = Field(Position(row, column),
                                                   Knight(team))

                    elif letter in ['c', 'f'] and row in [0, 7]:
                        board[row][column] = Field(Position(row, column),
                                                   Bishop(team))

                    elif letter == 'd' and row in [0, 7]:
                        board[row][column] = Field(Position(row, column),
                                                   Queen(team))

                    elif letter == 'e' and row in [0, 7]:
                        board[row][column] = Field(Position(row, column),
                                                   King(team))

                    else:
                        board[row][column] = Field(Position(row, column),
                                                   Pawn(team))

                else:
                    board[row][column] = Field(Position(row, column),
                                               None)
        return board

    def get_board(self):
        return self.__board

    def get_height(self):
        return self.__height

    def get_length(self):
        return self.__length
