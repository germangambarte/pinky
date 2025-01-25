from models.Expression import Expression
from src.Lexer import Token


class BinaryOperator(Expression):
    def __init__(self, op: Token, lvalue: Expression, rvalue: Expression, line) -> None:
        assert isinstance(op, Token), op
        assert isinstance(lvalue, Expression), lvalue
        assert isinstance(rvalue, Expression), rvalue
        self.__op = op
        self.__lvalue = lvalue
        self.__rvalue = rvalue
        self.__line = line

    def __repr__(self) -> str:
        return f"BinaryOperator({self.__op.get_lexeme()!r}, {self.__lvalue}, {self.__rvalue})"
