from Team import Team
from pieces.Piece import Piece


class Knight (Piece):

    def __init__(self, team: Team) -> None:
        super().__init__(3, "N", "Knight", team, "images/bNIcon.png" if team == Team.BLACK else "images/wNIcon.png")
