from forthLexer import lexer
from forthYacc import parse_input
import sys

def main(args):
    file_name = args[1][8:-4]

    with open(args[1], 'r') as file:
        code = file.read()

    # Análise léxica do código Forth
    lexer.input(code)

    # Análise sintática do código Forth e geração de código
    vm_code = parse_input(code)
    
    with open(f'../output/{file_name}.txt', 'w') as file:
        file.write(vm_code)

if __name__ == "__main__":
    main(sys.argv)