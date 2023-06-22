import abc
from Team import Team


class Piece (metaclass=abc.ABCMeta):

    def __init__(self, value: int, short_name: str, name: str, team: Team, icon_path: str) -> None:
        super().__init__()
        self.__value = value
        self.__short_name = short_name
        self.__name = name
        self.__team = team
        self.__icon_path = icon_path


    def get_short_name(self):
        return self.__short_name

    def get_team(self):
        return self.__team

    def get_value(self):
        return self.__value

    def get_icon_path(self):
        return self.__icon_path

    def __str__(self) -> str:
        return f"Name:{self.__name}, short_name:{self.__short_name}, value:{self.__value}, team:{self.__team}"

    def __eq__(self, o: object) -> bool:
        if type(o) != Piece:
            return False

        return self.__name == o.__name \
            and self.__short_name == o.__short_name \
            and self.__value == o.__value \
            and self.__team == o.__team


