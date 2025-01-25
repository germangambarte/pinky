import os.path
import sys

from src.Interpreter import Interpreter
from src.Lexer import Lexer
from src.Parser import Parser
from utils.utils import pretty_print

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python pinky.py <filename>")
    filename = sys.argv[1]

    with (open(filename) as file):
        print("*********************************")
        print("            SOURCE")
        print("*********************************\n")
        source = file.read()
        print(source)

        print("\n*********************************")
        print("            LEXER")
        print("*********************************\n")
        tokens = Lexer(source).tokenize()
        for token in tokens:
            print(token)

        print("\n*********************************")
        print("            PARSER")
        print("*********************************\n")
        ast = Parser(tokens).parse()
        pretty_print(ast)

        print("\n*********************************")
        print("          INTERPRETER")
        print("*********************************\n")
        interpreter = Interpreter()
        result = interpreter.interpret(ast)
        print(result)
