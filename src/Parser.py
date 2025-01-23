from models import *
from src.Token import *


class Parser:
    def __init__(self, tokens) -> None:
        self.__tokens = tokens
        self.__current = 0

    def parse(self):
        ast = self.expression()

    def expression(self):
        pass

    def term(self):
        pass

    def unary(self):
        pass

    def factor(self):
        pass
