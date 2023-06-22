import Position
from Team import Team
from pieces.Piece import Piece


class King (Piece):

    def __init__(self, team: Team) -> None:
        super().__init__(0, "K", "King", team, "images/bKIcon.png" if team == Team.BLACK else "images/wKIcon.png")
