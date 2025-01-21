import sys
from Token import *
from Lexer import *

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python pinky.py <filename>")
    filename = sys.argv[1]

    with open(filename) as file:
        source = file.read()
