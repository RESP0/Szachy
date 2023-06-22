from Team import Team
from pieces.Piece import Piece


class Rook (Piece):

    def __init__(self, team: Team) -> None:
        super().__init__(5, "R", "Rook", team, "images/bRIcon.png" if team == Team.BLACK else "images/wRIcon.png")
