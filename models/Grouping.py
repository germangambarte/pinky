from models.Expression import Expression
from src.Lexer import Token


class Grouping(Expression):
    def __init__(self, value: Expression) -> None:
        assert isinstance(value, Expression), value
        self.__value = value

    def __repr__(self) -> str:
        return f"Grouping({self.__value})"
