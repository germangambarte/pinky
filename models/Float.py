from models.Expression import Expression


class Float(Expression):
    def __init__(self, value, line) -> None:
        assert isinstance(value, float), value
        self.__value = value
        self.__line = line

    def __repr__(self) -> str:
        return f"Float[{self.__value}]"
