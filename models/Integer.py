from models.Expression import Expression


class Integer(Expression):
    def __init__(self, value, line) -> None:
        assert isinstance(value, int), value
        self.__value = value
        self.__line = line

    def __repr__(self) -> str:
        return f"Integer[{self.__value}]"

    def get_value(self):
        return self.__value
