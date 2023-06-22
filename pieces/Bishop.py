import Position
from Team import Team
from pieces.Piece import Piece


class Bishop (Piece):

    def __init__(self, team: Team) -> None:
        super().__init__(3, "B", "Bishop", team, "images/bBIcon.png" if team == Team.BLACK else "images/wBIcon.png")
