import Position
from Team import Team
from pieces.Piece import Piece


class Queen (Piece):

    def __init__(self, team: Team) -> None:
        super().__init__(9, "Q", "Queen", team, "images/bQIcon.png" if team == Team.BLACK else "images/wQIcon.png")
