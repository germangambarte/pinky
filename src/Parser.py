from models.BinaryOperator import BinaryOperator
from models.UnaryOperator import UnaryOperator
from models.Grouping import Grouping
from models.Float import Float
from models.Integer import Integer

from src.Token import *


class Parser:
    def __init__(self, tokens) -> None:
        self.__tokens = tokens
        self.__current = 0

    def parse(self):
        ast = self.expression()
        return ast

    # <expr> ::= <term> (('+' | '-') <term>)*
    def expression(self):
        lvalue = self.term()
        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op = self.previous_token()
            rvalue = self.term()
            lvalue = BinaryOperator(op, lvalue, rvalue)
        return lvalue

    # <term> ::= <factor> (('*' | '/') <factor>)*
    def term(self):
        lvalue = self.factor()
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            rvalue = self.factor()
            lvalue = BinaryOperator(op, lvalue, rvalue)
        return lvalue

    # <factor> ::= <unary>
    def factor(self):
        return self.unary()

    # <unary> ::= ('+' | '-' | '~') <unary> | <primary>
    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_PLUS):
            op = self.previous_token()
            operand = self.unary()
            return UnaryOperator(op, operand)
        return self.primary()

    # <primary> ::= <integer> | <float> | '(' <expr> ')'
    def primary(self):
        if self.match(TOK_INTEGER):
            return Integer(int(self.previous_token().get_lexeme()))
        if self.match(TOK_FLOAT):
            return Float(float(self.previous_token().get_lexeme()))
        if self.match(TOK_LPAREN):
            expr = self.expression()
            if not self.match(TOK_RPAREN):
                raise SyntaxError('Error: ")" expected.')
            else:
                return Grouping(expr)

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
            raise SyntaxError(
                f"Found {self.previous_token().get_lexeme()!r} at the end od parsing."
            )
        elif self.peek().get_token_type() == expected_type:
            return self.advance()
        else:
            raise SyntaxError(
                f"Expected {expected_type}, found {self.peek().get_lexeme()!r}."
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
