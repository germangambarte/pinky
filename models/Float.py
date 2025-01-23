from models.Expression import Expression


class Float(Expression):
    def __init__(self, value) -> None:
        assert isinstance(value, float), value
        self.__value = value

    def __repr__(self) -> str:
        return f"Float({self.__value})"
