import os.path
import sys

from src.Lexer import Lexer
from src.Parser import Parser

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python pinky.py <filename>")
    filename = sys.argv[1]
    # filename = os.path.join(os.path.dirname(__file__), 'scripts/script.pinky')

    with open(filename) as file:
        source = file.read()

        print("LEXER:")
        tokens = Lexer(source).tokenize()
        for token in tokens:
            print(token)

        print("PARSER:")
        ast = Parser(tokens).parse()
        print(ast)
