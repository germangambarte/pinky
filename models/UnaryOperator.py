from models.Expression import Expression
from src.Lexer import Token


class UnaryOperator(Expression):
    def __init__(self, op: Token, operand: Expression) -> None:
        assert isinstance(op, Token), op
        assert isinstance(operand, Expression), operand
        self.__op = op
        self.__operand = operand

    def __repr__(self) -> str:
        return f"UnaryOperator({self.__op.get_lexeme()!r}, {self.__operand})"
