import sys

from Lexer import *
from Token import *

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python pinky.py <filename>")
    filename = sys.argv[1]

    with open(filename) as file:
        source = file.read()
        print("LEXER:")
        lexer = Lexer(source).tokenize()
        for token in lexer:
            print(token)
