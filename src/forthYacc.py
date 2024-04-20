import ply.yacc as yacc
from forthLexer import tokens

# Definição da stack
stack = []

vm_code = ""

#Esta função é responsável por definir a regra gramatical para o programa, que consiste em uma sequência de declarações (statements).
def p_program(p):
    '''program : statements'''
    p[0] = p[1]
    
#Esta função define a regra gramatical para uma sequência de declarações. Pode ser uma única declaração ou várias declarações em sequência.
def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = p[1]
        
    else:
        p[1][1].append(p[2])
        p[0] = p[1]

#Esta função define a regra gramatical para uma declaração, que pode ser uma expressão ou uma estrutura de controle de fluxo.
def p_statement(p):
    '''statement : expression
                 | flow_control'''
    
    p[0] = ('statement', p[1])

#Esta função define a regra gramatical para uma expressão, que pode ser um número, uma string, uma variável ou uma expressão especial.
def p_expression(p):    
    '''expression : NUMBER
                  | STRING
                  | VARIABLE
                  | special_expression
                  | reserved_word'''
    global vm_code
    p[0] = p[1]
    if isinstance(p[1], int):
        stack.append(p[1])
        vm_code += f"PUSHI {p[1]}\n"     
    elif isinstance(p[1], float):
        stack.append(p[1])
        vm_code += f"PUSHF {p[1]}\n"
    elif isinstance(p[1], str):
        stack.append(p[1])
        if p[1] in ['IF', 'ELSE', 'THEN', 'WHILE', 'DO', 'LOOP', 'BEGIN', 'REPEAT', 'EXIT', 'DROP', 'DUP', 'SWAP', 'ROT', 'OVER', 'CONCAT']:
            vm_code += f"{p[1]}\n"
        else:
            vm_code += f"PUSHS {p[1]}\n"
    else:
        print("Error: Invalid expression")

def p_dot(p):
    '''expression : DOT'''
    global vm_code
    top_value = stack.pop()
    if isinstance(top_value, int):
        vm_code += "WRITEI\n"
    elif isinstance(top_value, float):
        vm_code += "WRITEF\n"
    elif isinstance(top_value, str):
        vm_code += "WRITES\n"
    p[0] = top_value

#Esta função define a regra gramatical para uma expressão aritmética, que consiste em uma expressão seguida por um operador aritmético e outra expressão.
def p_expression_arithmetic(p):
    '''expression : expression expression arithmetic_op'''
    global vm_code
    if len(stack) < 2:
        print("Error: Not enough values on the stack for arithmetic operation")
        return  
    b = stack.pop()
    a = stack.pop()
    op = p[3]
    if op == '+':
        result = a + b
        stack.append(result)
        if isinstance(result, float):
            vm_code += "FADD\n"
        else: vm_code += "ADD\n"
    elif op == '-':
        result = a - b
        stack.append(result)
        if isinstance(result, float):
            vm_code += "FSUB\n"
        else: vm_code += "SUB\n"
    elif op == '*':
        result = a * b
        stack.append(result)
        if isinstance(result, float):
            vm_code += "FMUL\n"
        else: vm_code += "MUL\n"
    elif op == '/':
        result = a / b
        stack.append(result)
        if isinstance(result, float):
            vm_code += "FDIV\n"
        else: vm_code += "DIV\n"
    elif op == '%':
        result = a % b
        stack.append(result)
        vm_code += "MOD\n"

#Esta função define a regra gramatical para operadores aritméticos, como adição, subtração, multiplicação, divisão, módulo e potência.
def p_arithmetic_op(p):
    '''arithmetic_op : PLUS
                     | MINUS
                     | TIMES
                     | DIVIDE
                     | MOD'''
    p[0] = p[1]
    
#Esta função define a regra gramatical para expressões relacionais, que consistem em uma expressão seguida por um operador relacional e outra expressão.
def p_expression_relational(p):
    '''expression : expression expression relational_op'''
    global vm_code
    if len(stack) < 2:
        print("Error: Not enough values on the stack for relational operation")
        return
    b = stack.pop()
    a = stack.pop()
    result = 0
    op = p[3]
    if op == '<':
        stack.append(a < b)
        if isinstance(result, float):
            vm_code += "FINF\n"
        else: vm_code += "INF\n"
    elif op == '>':
        stack.append(a > b)
        if isinstance(result, float):
            vm_code += "FSUP\n"
        else: vm_code += "SUP\n"
    elif op == '<=':
        stack.append(a <= b)
        if isinstance(result,float):
            vm_code += "FINFEQ\n"
        else: vm_code += "INFEQ\n"
    elif op == '>=':
        stack.append(a >= b)
        if isinstance(result,float):
            vm_code += "FSUPEQ\n"
        else: vm_code += "SUPEQ\n"

#Esta função define a regra gramatical para operadores relacionais, como igualdade, menor que e maior que.
def p_relational_op(p):
    '''relational_op : NOT
                     | INF
                     | SUP
                     | INFEQ
                     | SUPEQ'''
    p[0] = p[1]

#Esta função define a regra gramatical para operações com strings, nomeadamente o CONCAT.
def p_string_operations(p):
    '''expression : expression expression string_op'''
    global vm_code
    if len(stack) < 2:
        print("Error: Not enough values on the stack for string operation")
        return
    m = stack.pop()
    n = stack.pop()
    op = p[3]
    if not (isinstance(m, str) and isinstance(n,str)): #Tratamento de Erro quando não são strings
        print("Error: CONCAT op requires the operands to be strings")
        return      
    result = n + m
    stack.append(result)


def p_string_op(p):
    '''string_op : CONCAT'''
    p[0] = p[1]
    global vm_code
    vm_code += f"{p[1]}"


#Esta função define a regra gramatical para expressões especiais, como exclamação, arroba, ponto, dois pontos, ponto e vírgula, parênteses esquerdo e direito.
def p_special_expression(p):
    '''special_expression : EXCLAMATION
                           | AT
                           | COLON
                           | SEMICOLON
                           | LEFT_PAREN
                           | RIGHT_PAREN'''
    p[0] = p[1]

#Esta função define a regra gramatical para estruturas de controle de fluxo, como declarações condicionais (if-else), loops (while e repeat) e declarações de saída.
def p_flow_control(p):
    '''flow_control : if_statement
                    | else_statement
                    | while_loop
                    | repeat_loop
                    | exit_statement
                    | drop_statement
                    | dup_statement
                    | swap_statement
                    | rot_statement
                    | over_statement'''
    p[0] = ('flow_control', p[1])

#Estas funções definem as regras gramaticais para cada tipo específico de estrutura de controle de fluxo.

def p_if_statement(p):
    '''if_statement : expression IF statements THEN'''
    p[0] = p[2] + " IF "

def p_else_statement(p):
    '''else_statement : ELSE'''
    p[0] = " ELSE "

def p_while_loop(p):
    '''while_loop : WHILE expression DO statements LOOP'''
    p[0] = " BEGIN " + p[2] + " WHILE " + p[4] + " REPEAT "

def p_repeat_loop(p):
    '''repeat_loop : BEGIN statements WHILE expression REPEAT'''
    p[0] = " BEGIN " + p[2] + " " + p[4] + " REPEAT "

def p_exit_statement(p):
    '''exit_statement : EXIT'''
    p[0] = " EXIT "

def p_drop_statement(p):
    '''drop_statement : DROP'''
    p[0] = " DROP "
    global vm_code
    vm_code += "POP 1\n"

def p_dup_statement(p):
    '''dup_statement : DUP'''
    if not stack:
        print("Error: Not enough values on the stack for DUP operation")
        return
    top_value = stack[-1]
    stack.append(top_value)
    p[0] = " DUP "
    global vm_code
    if isinstance(top_value, int):
        vm_code += f"PUSHI {top_value}\n"     
    elif isinstance(top_value, float):
        vm_code += f"PUSHF {top_value}\n"
    elif isinstance(top_value, str):
        vm_code += f"PUSHS {top_value}\n"
    else:
        print("Error: Invalid expression")

def p_swap_statement(p):
    '''swap_statement : SWAP'''
    if len(stack) < 2:
        print("Error: Not enough values on the stack for SWAP operation")
        return
    global vm_code
    a = stack.pop()
    b = stack.pop()
    vm_code += "SWAP\n"
    stack.append(a)
    stack.append(b)
    p[0] = " SWAP "

def p_rot_statement(p):
    '''rot_statement : ROT'''
    if len(stack) < 3:
        print("Error: Not enough values on the stack for ROT operation")
        return
    a = stack.pop()
    b = stack.pop()
    c = stack.pop()
    if isinstance(a, int):
        vm_code += f"PUSHI {b}\n"
    elif isinstance(a, float):
        vm_code += f"PUSHF {b}\n"
    elif isinstance(a, str):
        vm_code += f"PUSHS {b}\n"

    if isinstance(b, int):
        vm_code += f"PUSHI {a}\n"
    elif isinstance(b, float):
        vm_code += f"PUSHF {a}\n"
    elif isinstance(b, str):
        vm_code += f"PUSHS {a}\n"

    if isinstance(c, int):
        vm_code += f"PUSHI {c}\n"
    elif isinstance(c, float):
        vm_code += f"PUSHF {c}\n"
    elif isinstance(c, str):
        vm_code += f"PUSHS {c}\n"
        
    stack.append(b)
    stack.append(a)
    stack.append(c)
    p[0] = " ROT "

def p_over_statement(p):
    '''over_statement : OVER'''
    if len(stack) < 2:
        print("Error: Not enough values on the stack for OVER operation")
        return
        global vm_code
    a = stack[-2]
    stack.append(a)
    if isinstance(a, int):
        vm_code += f"PUSHI {a}\n"
    elif isinstance(a, float):
        vm_code += f"PUSHF {a}\n"
    elif isinstance(a, str):
        vm_code += f"PUSHS {a}\n"
    p[0] = " OVER "

#Esta função é chamada quando ocorre um erro durante o processo de análise sintática. Ela imprime uma mensagem de erro e termina o processo de análise.
def p_error(p):
    if p:
        print("Syntax error:", p)
        yacc.errok()

parser = yacc.yacc()

def parse_input(input_string):
    parser.parse(input_string)
    return vm_code