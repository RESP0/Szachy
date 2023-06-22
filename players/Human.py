from Team import Team
from players.Player import Player


class Human (Player):

    def __init__(self, team: Team) -> None:
        super().__init__(team)
