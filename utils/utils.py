import sys


def pretty_print(ast):
    new_line = False
    i = 0
    for ch in str(ast):
        if ch == '(':
            if not new_line:
                print(end='')
            print(ch)
            i += 2
            new_line = True
        elif ch == ')':
            if not new_line:
                print()
            new_line = True
            i -= 2
            print(' ' * i + ch)
        else:
            if new_line:
                print(' ' * i, end='')
            print(ch, end='')
            new_line = False
def parse_error(message,line):
    print(f"{Colors.RED}[Line {line}] {message}{Colors.WHITE}")
    sys.exit(1)

def lexing_error(message,line):
    print(f"{Colors.RED}[Line {line}] {message}{Colors.WHITE}")
    sys.exit(1)

class Colors:
    WHITE = '\033[0m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
