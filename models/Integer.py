from models.Expression import Expression


class Integer(Expression):
    def __init__(self, value) -> None:
        assert isinstance(value, int), value
        self.__value = value

    def __repr__(self) -> str:
        return f"Integer({self.__value})"
