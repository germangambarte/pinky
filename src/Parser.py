from models.BinaryOperator import BinaryOperator
from models.UnaryOperator import UnaryOperator
from models.Grouping import Grouping
from models.Float import Float
from models.Integer import Integer

from src.Token import *
from utils.utils import parse_error


class Parser:
    def __init__(self, tokens) -> None:
        self.__tokens = tokens
        self.__current = 0

    def parse(self):
        ast = self.add_or_sub()
        return ast

    def add_or_sub(self):
        lvalue = self.mult_or_div()
        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op = self.previous_token()
            rvalue = self.mult_or_div()
            lvalue = BinaryOperator(op, lvalue, rvalue, self.previous_token().get_line())
        return lvalue

    def mult_or_div(self):
        lvalue = self.unary()
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            rvalue = self.unary()
            lvalue = BinaryOperator(op, lvalue, rvalue, self.peek().get_line())
        return lvalue

    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_PLUS):
            op = self.previous_token()
            operand = self.unary()
            return UnaryOperator(op, operand, self.peek().get_line())
        return self.primary()

    def primary(self):
        if self.match(TOK_INTEGER):
            return Integer(int(self.previous_token().get_lexeme()), self.previous_token().get_line())
        if self.match(TOK_FLOAT):
            return Float(float(self.previous_token().get_lexeme()), self.previous_token().get_line())
        if self.match(TOK_LPAREN):
            expr = self.add_or_sub()
            if not self.match(TOK_RPAREN):
                raise parse_error('Error: ")" expected.', self.previous_token().get_line())
            else:
                return Grouping(expr, self.previous_token().get_line())

    def peek(self):
        return self.__tokens[self.__current]

    def advance(self):
        if self.__current >= len(self.__tokens):
            return False
        current_token = self.peek()
        self.__current += 1
        return current_token

    def is_next(self, expected_type):
        if self.__current >= len(self.__tokens):
            return False
        return self.__tokens[self.__current + 1].get_token_type() == expected_type

    def expect(self, expected_type):
        if self.__current >= len(self.__tokens):
            raise parse_error(
                f"Found {self.previous_token().get_lexeme()!r} at the end od parsing.",
                self.previous_token().get_line()
            )
        elif self.peek().get_token_type() == expected_type:
            return self.advance()
        else:
            raise parse_error(
                f"Expected {expected_type}, found {self.peek().get_lexeme()!r}.",
                self.peek().get_line()
            )

    def match(self, expected_type):
        if self.__current >= len(self.__tokens):
            return False
        if self.peek().get_token_type() != expected_type:
            return False
        self.__current += 1
        return True

    def previous_token(self):
        return self.__tokens[self.__current - 1]
