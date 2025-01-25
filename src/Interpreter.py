from models.BinaryOperator import BinaryOperator
from models.UnaryOperator import UnaryOperator
from models.Integer import Integer
from models.Float import Float
from models.Grouping import Grouping
from src.Token import *


class Interpreter:
    def __init__(self):
        pass

    def interpret(self, node):
        if isinstance(node, Integer):
            return float(node.get_value())
        elif isinstance(node, Float):
            return float(node.get_value())
        elif isinstance(node, Grouping):
            return self.interpret(node.get_value())
        elif isinstance(node, BinaryOperator):
            lvalue = self.interpret(node.get_lvalue())
            rvalue = self.interpret(node.get_rvalue())
            if node.get_op().get_token_type() == TOK_PLUS:
                return lvalue + rvalue
            elif node.get_op().get_token_type() == TOK_MINUS:
                return lvalue - rvalue
            elif node.get_op().get_token_type() == TOK_STAR:
                return lvalue * rvalue
            elif node.get_op().get_token_type() == TOK_SLASH:
                return lvalue / rvalue
        elif isinstance(node, UnaryOperator):
            operand = self.interpret(node.get_operand())
            if node.get_op().get_token_type() == TOK_PLUS:
                return +operand
            elif node.get_op().get_token_type() == TOK_MINUS:
                return -operand