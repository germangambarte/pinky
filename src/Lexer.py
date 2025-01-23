from src.Token import *


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
                continue
            elif ch == "\t":
                continue
            elif ch == "\r":
                continue
            elif ch == " ":
                continue
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
            elif ch == ",":
                self.add_new_token(TOK_COMMA)
            elif ch == "+":
                self.add_new_token(TOK_PLUS)
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
            elif ch == "=":
                self.add_new_token(TOK_EQEQ if self.nextcharis("=") else TOK_EQ)
            elif ch == "~":
                self.add_new_token(TOK_NEQ if self.nextcharis("=") else TOK_NOT)
            elif ch == "<":
                self.add_new_token(TOK_LEQ if self.nextcharis("=") else TOK_LT)
            elif ch == ">":
                self.add_new_token(TOK_GEQ if self.nextcharis("=") else TOK_GT)
            elif ch == ":":
                self.add_new_token(TOK_ASSIGN if self.nextcharis("=") else TOK_COLON)
            elif ch == "-":
                if self.nextcharis("-"):
                    while self.peek() != "\n" and not (
                        self.__current >= len(self.__source)
                    ):
                        self.advance()
                else:
                    self.add_new_token(TOK_MINUS)
            elif ch.isdigit():
                self.handle_numbers()
            elif ch == "'" or ch == '"':
                self.handle_string(ch)
            elif ch.isalpha() or ch == "_":
                self.handle_identifier()
            else:
                raise SyntaxError(
                    f"[Line {self.__line}] Error at {ch}: Unexpected character"
                )
        return self.__tokens

    def add_new_token(self, token_type):
        self.__tokens.append(
            Token(token_type, self.__source[self.__start : self.__current], self.__line)
        )

    def peek(self):
        if self.__current >= len(self.__source):
            return "\0"
        return self.__source[self.__current]

    def lookahead(self, n=1):
        if self.__current >= len(self.__source):
            return "\0"
        return self.__source[self.__current + n]

    def nextcharis(self, expected):
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

    def handle_numbers(self):
        while self.peek().isdigit():
            self.advance()
        if self.peek() == "." and self.lookahead().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
            self.add_new_token(TOK_FLOAT)
        else:
            self.add_new_token(TOK_INTEGER)

    def handle_string(self, ch):
        while self.peek() != ch and not (self.__current >= len(self.__source)):
            self.advance()
        if self.__current >= len(self.__source):
            raise SyntaxError(f"[Line {self.__line}] Unterminated string.")
        self.advance()
        self.add_new_token(TOK_STRING)

    def handle_identifier(self):
        while self.peek().isalnum() or self.peek() == "_":
            self.advance()
        identifier = self.__source[self.__start : self.__current]
        keyword = keywords.get(identifier)
        if keyword is None:
            self.add_new_token(TOK_IDENTIFIER)
        else:
            self.add_new_token(keyword)
