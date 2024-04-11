from lexer import lexer
from parser import parser

def main():
    while True:
        data = input("TESTE:Digite a expressão em Forth (ou digite 'bye' para sair): ")
        if data.lower() == 'bye':
            break
        
        lexer.input(data)
        for tok in lexer:
            print(tok)
        result = parser.parse(data, lexer=lexer)
        if result is not None:
            print("Resultado: ", stack.pop())
        if not data:
            break

if __name__ == "__main__":
    main()
