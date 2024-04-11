from forthLexer import lexer
from forthYacc import parser

# Definição da classe ForthNode para representar um nó na árvore de análise sintática
class ForthNode:
    def __init__(self, value, children=None):
        """
        Inicializa um nó na árvore de análise sintática de Forth.

        Args:
            value (str): O valor do nó.
            children (list, opcional): Uma lista dos nós filhos. Pode ser None se não houver filhos.
        """
        self.value = value
        self.children = children if children else []

# Definição da subclasse ForthExpressionNode para representar um nó de expressão na árvore de análise sintática
class ForthExpressionNode(ForthNode):
    def __init__(self, operator, operands):
        """
        Inicializa um nó na árvore de análise sintática de Forth para representar uma expressão.

        Args:
            operator (str): O operador da expressão.
            operands (list): Uma lista dos operandos da expressão.
        """
        super().__init__(operator, operands)

# Definição da subclasse ForthInstructionNode para representar um nó de instrução na árvore de análise sintática
class ForthInstructionNode(ForthNode):
    def __init__(self, instruction):
        """
        Inicializa um nó na árvore de análise sintática de Forth para representar uma instrução.

        Args:
            instruction (str): A instrução Forth.
        """
        super().__init__(instruction)

def generate_forth_code(node):
    """
    Gera código Forth a partir de uma árvore de análise sintática.

    Args:
        node (ForthNode): O nó raiz da árvore de análise sintática.

    Returns:
        str: O código Forth gerado.
    """
    forth_code = ""
    if isinstance(node, ForthExpressionNode):
        forth_code += generate_forth_code(node.children[0])
        forth_code += generate_forth_code(node.children[1])
        forth_code += node.value + " "
    elif isinstance(node, ForthInstructionNode):
        forth_code += node.value + " "
    else:
        forth_code += str(node) + " "
    return forth_code

# Inicialização da pilha do interpretador Forth
forth_stack = []

def push_to_stack(value):
    """
    Empilha um valor na pilha do interpretador Forth.

    Args:
        value: O valor a ser empilhado.
    """
    forth_stack.append(value)

def pop_from_stack():
    """
    Desempilha um valor da pilha do interpretador Forth.

    Returns:
        O valor desempilhado.
    """
    return forth_stack.pop()

if __name__ == "__main__":
    # Leitura do código Forth a partir de um arquivo
    with open('input.txt', 'r') as file:
        code = file.read()

    # Análise léxica do código Forth
    lexer.input(code)
    for token in lexer:
        print(token)

    # Análise sintática do código Forth e geração de código
    result = parser.parse(code)
    print(result)
    forth_code = generate_forth_code(result)
    print(forth_code)