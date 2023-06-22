import Position
from Team import Team
from players.Player import Player
import chess
import chess.engine


class AI (Player):

    def __init__(self, team: Team) -> None:
        super().__init__(team)
        self.__board = chess.Board()
        self.__board.castling_rights &= ~(chess.BB_H8 | chess.BB_A8)
        self.__engine = chess.engine.SimpleEngine.popen_uci('stockfish/stockfish_15.1_win_x64_popcnt/stockfish-windows-2022-x86-64-modern.exe')

    def update(self, source: str, dest: str):
        move = chess.Move.from_uci(source + dest)
        self.__board.push(move)

    def get_move(self):
        result = self.__engine.play(self.__board, chess.engine.Limit(time=2.0))
        self.__board.is_checkmate()
        move = result.move
        self.__board.push(move)

        return str(move)[:-2], str(move)[2:]


def convert_square(square: int):
    y = square // 8
    x = square - y * 8

    return Position.Position(x, y)
