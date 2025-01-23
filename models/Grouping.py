from models.Expression import Expression
from src.Lexer import Token


class UnaryOperator(Expression):
    def __init__(self, value: Expression) -> None:
        assert isinstance(value, Token), value
        self.__value = value

    def __repr__(self) -> str:
        return f"BinaryOperator({self.__value})"
