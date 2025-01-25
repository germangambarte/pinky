from models.Expression import Expression
from src.Lexer import Token


class UnaryOperator(Expression):
    def __init__(self, op: Token, operand: Expression, line) -> None:
        assert isinstance(op, Token), op
        assert isinstance(operand, Expression), operand
        self.__op = op
        self.__operand = operand
        self.__line = line

    def __repr__(self) -> str:
        return f"UnaryOperator({self.__op.get_lexeme()!r}, {self.__operand})"

    def get_op(self):
        return self.__op

    def get_operand(self):
        return self.__operand
