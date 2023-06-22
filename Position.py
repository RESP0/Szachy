class Position:

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        self.__name = (chr(y + 97)) + str((x + 1))

    def get_name(self):
        return self.__name

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, other):
        if type(other) is str:
            return self.__name == other

        if type(other) is Position:
            return self.__name == other.__name and self.__x == other.__x and self.__y == other.__y

        return False

    def __str__(self) -> str:
        return f"X:{self.__x}, y:{self.__y}, name:{self.__name}"



