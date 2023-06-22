from Team import Team
from pieces.Piece import Piece


class Pawn (Piece):

    def __init__(self, team: Team) -> None:
        super().__init__(1, "p", "Pawn", team, "images/bpIcon.png" if team == Team.BLACK else "images/wpIcon.png")
