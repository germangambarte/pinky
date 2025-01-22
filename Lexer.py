from Token import *


class Lexer:
    def __init__(self, source) -> None:
        self.__source = source
        self.__start = 0
        self.__current = 0
        self.__line = 1
        self.__tokens = []

    def tokenize(self):
        while self.__current < len(self.__source):
            self.__start = self.__current
            ch = self.advance()
            if ch == "\n":
                self.__line += 1
            elif ch == "\t":
                pass
            elif ch == "\r":
                pass
            elif ch == " ":
                pass
            elif ch == "#":
                while self.peek() != "\n":
                    self.advance()
            elif ch == "(":
                self.add_new_token(TOK_LPAREN)
            elif ch == ")":
                self.add_new_token(TOK_RPAREN)
            elif ch == "{":
                self.add_new_token(TOK_LCURLY)
            elif ch == "}":
                self.add_new_token(TOK_RCURLY)
            elif ch == "[":
                self.add_new_token(TOK_LSQUAR)
            elif ch == "]":
                self.add_new_token(TOK_RSQUAR)
            elif ch == ".":
                self.add_new_token(TOK_DOT)
            if ch == ",":
                self.add_new_token(TOK_COMMA)
            elif ch == "+":
                self.add_new_token(TOK_PLUS)
            elif ch == "-":
                self.add_new_token(TOK_MINUS)
            elif ch == "*":
                self.add_new_token(TOK_STAR)
            elif ch == "^":
                self.add_new_token(TOK_CARET)
            elif ch == "/":
                self.add_new_token(TOK_SLASH)
            elif ch == ";":
                self.add_new_token(TOK_SEMICOLON)
            elif ch == "?":
                self.add_new_token(TOK_QUESTION)
            elif ch == "%":
                self.add_new_token(TOK_MOD)
        return self.__tokens

    def add_new_token(self, token_type):
        self.__tokens.append(
            Token(token_type, self.__source[self.__start : self.__current], self.__line)
        )

    def peek(self):
        return self.__source[self.__current]

    def lookahead(self, n=1):
        return self.__source[self.__current + n]

    def match(self, expected):
        if self.__current >= len(self.__source):
            return False
        if self.__source[self.__current] != expected:
            return False
        self.__current += 1
        return True

    def advance(self):
        ch = self.__source[self.__current]
        self.__current += 1
        return ch
