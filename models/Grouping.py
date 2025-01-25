from models.Expression import Expression
from src.Lexer import Token


class Grouping(Expression):
    def __init__(self, value: Expression, line) -> None:
        assert isinstance(value, Expression), value
        self.__value = value
        self.__line = line

    def __repr__(self) -> str:
        return f"Grouping({self.__value})"
