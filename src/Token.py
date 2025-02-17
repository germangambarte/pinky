TOK_LPAREN = "TOK_LPAREN"
TOK_RPAREN = "TOK_RPAREN"
TOK_LCURLY = "TOK_LCURLY"
TOK_RCURLY = "TOK_RCURLY"
TOK_LSQUAR = "TOK_LSQUAR"
TOK_RSQUAR = "TOK_RSQUAR"
TOK_COMMA = "TOK_COMMA"
TOK_DOT = "TOK_DOT"
TOK_PLUS = "TOK_PLUS"
TOK_MINUS = "TOK_MINUS"
TOK_STAR = "TOK_STAR"
TOK_SLASH = "TOK_SLASH"
TOK_CARET = "TOK_CARET"
TOK_MOD = "TOK_MOD"
TOK_COLON = "TOK_COLON"
TOK_SEMICOLON = "TOK_SEMICOLON"
TOK_QUESTION = "TOK_QUESTION"
TOK_NOT = "TOK_NOT"
TOK_GT = "TOK_GT"
TOK_LT = "TOK_LT"
TOK_GEQ = "TOK_GEQ"
TOK_LEQ = "TOK_LEQ"
TOK_NEQ = "TOK_NEQ"
TOK_EQ = "TOK_EQ"
TOK_EQEQ = "TOK_EQEQ"
TOK_ASSIGN = "TOK_ASSIGN"
TOK_GTGT = "TOK_GTGT"
TOK_LTLT = "TOK_LTLT"
TOK_IDENTIFIER = "TOK_IDENTIFIER"
TOK_STRING = "TOK_STRING"
TOK_INTEGER = "TOK_INTEGER"
TOK_FLOAT = "TOK_FLOAT"
TOK_IF = "TOK_IF"
TOK_THEN = "TOK_THEN"
TOK_ELSE = "TOK_ELSE"
TOK_TRUE = "TOK_TRUE"
TOK_FALSE = "TOK_FALSE"
TOK_AND = "TOK_AND"
TOK_OR = "TOK_OR"
TOK_WHILE = "TOK_WHILE"
TOK_DO = "TOK_DO"
TOK_FOR = "TOK_FOR"
TOK_FUNC = "TOK_FUNC"
TOK_NULL = "TOK_NULL"
TOK_END = "TOK_END"
TOK_PRINT = "TOK_PRINT"
TOK_PRINTLN = "TOK_PRINTLN"
TOK_RET = "TOK_RET"

keywords = {
    "if": TOK_IF,
    "then": TOK_THEN,
    "else": TOK_ELSE,
    "true": TOK_TRUE,
    "false": TOK_FALSE,
    "and": TOK_AND,
    "or": TOK_OR,
    "while": TOK_WHILE,
    "do": TOK_DO,
    "for": TOK_FOR,
    "func": TOK_FUNC,
    "null": TOK_NULL,
    "end": TOK_END,
    "print": TOK_PRINT,
    "println": TOK_PRINTLN,
    "ret": TOK_RET,
}


class Token:

    def __init__(self, token_type, lexeme, line) -> None:
        self.__token_type = token_type
        self.__lexeme = lexeme
        self.__line = line

    def __repr__(self):
        return f"({self.__token_type}, {self.__lexeme!r}, {self.__line})"

    def get_token_type(self):
        return self.__token_type

    def get_lexeme(self):
        return self.__lexeme

    def get_line(self):
        return self.__line
