from Board import Board
from Field import Field
from Team import Team
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Queen import Queen
from pieces.Rook import Rook
from players.Human import Human
from players.Player import Player
from pieces.Piece import Piece
from Position import Position


class Game:

    def __init__(self, player1: Human, player2: Player) -> None:
        self.__board: Board = Board(8, 8)
        self.__player1 = player1
        self.__player2 = player2

    def get_possible_destinations(self, player: Player, source_field: Field, check_if_causes_check: bool = True) -> list[Field]:
        if source_field is None or source_field.get_piece() is None:
            return []

        if player.get_team() is not source_field.get_piece().get_team():
            return []

        return self.__get_possible_destinations(source_field, check_if_causes_check)

    def get_all_pieces(self, team: Team):
        return self.__board.get_pieces(team)

    def __get_possible_destinations(self, source_field: Field, check_if_causes_check: bool = True):
        board = self.__board.get_board()
        piece: Piece = source_field.get_piece()
        team = piece.get_team()
        enemy_team = Team.WHITE if team == Team.BLACK else Team.BLACK
        position: Position = source_field.get_position()
        row = position.get_x()
        col = position.get_y()

        check_if_does_not_move = False

        # whether causes check
        if check_if_causes_check and type(piece) is not King:
            source_field.set_piece(None)
            enemy_fields = list(self.get_all_pieces(enemy_team))
            for field in enemy_fields:
                if self.check(field, enemy_team) is not None:
                    check_if_does_not_move = True
                    break
            source_field.set_piece(piece)

        destinations = []
        # Pawn
        if type(piece) is Pawn:
            if team == Team.WHITE:
                # move forward 1 or 2
                if board[row + 1][col].get_piece() is None:
                    destinations.append(board[row + 1][col])
                    if row == 1 and board[row + 2][col].get_piece() is None:
                        destinations.append(board[row + 2][col])

                # takes diagonaly right
                if col < 7 and board[row + 1][col + 1].get_piece() is not None:
                    piece_to_take = board[row + 1][col + 1].get_piece()
                    if piece_to_take.get_team() == Team.BLACK:
                        destinations.append(board[row + 1][col + 1])

                # takes diagonaly left
                if col > 0 and board[row + 1][col - 1].get_piece() is not None:
                    piece_to_take = board[row + 1][col - 1].get_piece()
                    if piece_to_take.get_team() == Team.BLACK:
                        destinations.append(board[row + 1][col - 1])
            else:
                # moves down 1 or 2
                if board[row - 1][col].get_piece() is None:
                    destinations.append(board[row - 1][col])
                    if row == 6 and board[row - 2][col].get_piece() is None:
                        destinations.append(board[row - 2][col])

                # takes diagonaly right
                if col < 7 and board[row - 1][col + 1].get_piece() is not None:
                    piece_to_take = board[row - 1][col + 1].get_piece()
                    if piece_to_take.get_team() == Team.WHITE:
                        destinations.append(board[row - 1][col + 1])

                # takes diagonaly left
                if col > 0 and board[row - 1][col - 1].get_piece() is not None:
                    piece_to_take = board[row - 1][col - 1].get_piece()
                    if piece_to_take.get_team() == Team.WHITE:
                        destinations.append(board[row - 1][col - 1])

        elif type(piece) is Bishop:
            destinations.extend(self.__get_bishop_moves(row, col, team))

        elif type(piece) is Knight:
            only_once = True
            # left up L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x + 1), (y - 2)), only_once))

            # left down L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x - 1), (y - 2)), only_once))

            # right up L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x + 1), (y + 2)), only_once))

            # right down L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x - 1), (y + 2)), only_once))

            # up left L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x + 2), (y - 1)), only_once))

            # up right L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x + 2), (y + 1)), only_once))

            # down left L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x - 2), (y - 1)), only_once))

            # down right L
            destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x - 2), (y + 1)), only_once))

        elif type(piece) is Rook:
            destinations.extend(self.__get_rook_moves(row, col, team))

        elif type(piece) is Queen:
            destinations.extend(self.__get_bishop_moves(row, col, team))
            destinations.extend(self.__get_rook_moves(row, col, team))

        elif type(piece) is King:
            moves = self.__get_bishop_moves(row, col, team, True)
            moves += self.__get_rook_moves(row, col, team, True)
            destinations.extend(moves)

        illegal_moves = []

        if check_if_causes_check:
            source_field.set_piece(None)
            enemy_fields = list(self.get_all_pieces(enemy_team))
            for move in destinations:
                dest_piece = move.get_piece()
                move.set_piece(piece)

                for field in enemy_fields:
                    if self.check(field, enemy_team) is not None:
                        illegal_moves.append(move)
                        continue

                move.set_piece(dest_piece)
            source_field.set_piece(piece)

        return list(destination for destination in destinations if destination not in illegal_moves)

    def __get_rook_moves(self, row, col, team, only_once=False):
        destinations = []

        # up
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x + 1), y), only_once))

        # down
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x - 1), y), only_once))

        # right
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: (x, (y + 1)), only_once))

        # left
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: (x, (y - 1)), only_once))

        return destinations

    def __get_bishop_moves(self, row, col, team, only_once=False):
        destinations = []

        # left up
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x + 1), (y - 1)), only_once))

        # left down
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x - 1), (y - 1)), only_once))

        # right up
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x + 1), (y + 1)), only_once))

        # right down
        destinations.extend(self.__get_moves_for_function(row, col, team, lambda x, y: ((x - 1), (y + 1)), only_once))

        return destinations

    def __get_moves_for_function(self, row, col, team, func, only_once=False):
        destinations = []

        coords = func(row, col)
        row = coords[0]
        col = coords[1]

        while row in range(self.__board.get_height()) and col in range(self.__board.get_length()):
            dest_field = self.__board.get_board()[row][col]
            if dest_field.get_piece() is None:
                destinations.append(dest_field)
            else:
                if dest_field.get_piece().get_team() != team:
                    destinations.append(dest_field)
                break

            if only_once:
                break

            coords = func(row, col)
            row = coords[0]
            col = coords[1]

        return destinations

    def mate(self, king_field: Field):
        if king_field is None or king_field.get_piece() is None or type(king_field.get_piece()) is not King:
            return False

        team = king_field.get_piece().get_team()
        all_fields = self.get_all_pieces(team)
        moves = []
        for field in all_fields:
            moves.extend(self.get_possible_destinations(Human(team), field))

        return moves == []

    def check(self, source: Field, team: Team) -> Field:
        if source is None or source.get_piece() is None or team is None:
            return None

        destinations = self.get_possible_destinations(Human(team), source, False)
        for destination in destinations:
            dest_piece = destination.get_piece()
            if dest_piece is None:
                continue
            elif dest_piece.get_team() != team and dest_piece.get_short_name() == "K":
                return destination

        return None

    def make_move(self, player: Player, source: Field, destination: Field) -> str:
        if source is None or source.get_piece() is None or destination is None:
            return None

        piece: Piece = source.get_piece()
        short_piece_name = piece.get_short_name()
        destination_position: Position = destination.get_position()

        if destination in self.get_possible_destinations(player, source):
            destination_piece = destination.get_piece()
            destination.set_piece(piece)
            source.set_piece(None)

            # takes
            if destination_piece is not None:
                player.takes(destination_piece)

                if short_piece_name == '':
                    short_piece_name = source.get_position().get_name()[:1]
                return short_piece_name + source.get_position().get_name() + 'x' + destination_position.get_name()
            # does not take
            else:
                destination.set_piece(piece)
                source.set_piece(None)
            return short_piece_name + source.get_position().get_name() + '->' + destination_position.get_name()

    def get_player1(self):
        return self.__player1

    def get_player2(self):
        return self.__player2

    def get_field(self, name: str) -> Field:
        board = self.__board.get_board()
        # ascii 97 = a
        column = ord(name[:1]) - 97
        row = int(name[1:]) - 1

        return board[row][column]
