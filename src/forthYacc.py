import ply.yacc as yacc
from forthLexer import tokens
import re

# Definição da stack
stack = []
vm_code = ""
current_function = []
function_definitions = {}

def p_programa(p):
    '''programa : comandos'''
    p[0] = p[1]
    
def p_comandos(p):
    '''comandos : comando
                | comandos comando'''
    if len(p) == 2:
        p[0] = p[1]
        
    else:
        p[1][1].append(p[2])
        p[0] = p[1]
        
def p_comando(p):
    '''comando : exp_aritmeticas
               | exp_relacionais
               | functions
               | values
               | creating_funcs'''
               #| flow_control'''
    
    p[0] =  p[1]
    
def p_exp_aritmeticas(p):
    '''exp_aritmeticas : comando comando PLUS
                       | comando comando MINUS
                       | comando comando TIMES
                       | comando comando DIVIDE
                       | comando comando MOD'''
    global vm_code
    if len(stack) < 2:
        print("Error: Not enough members on the stack for arithmetic operation")
        return  
    b = stack.pop()
    a = stack.pop()
    op = p[3]
    if op == '+':
        result = a + b
        stack.append(result)
        if isinstance(result, float):
            vm_code += f'FADD\nPUSHF {result}\n'
        else: vm_code += f'ADD\nPUSHI {result}\n'
    elif op == '-':
        result = a - b
        stack.append(result)
        if isinstance(result, float):
            vm_code += f'FSUB\nPUSHF {result}\n'
        else: vm_code += f'SUB\nPUSHI {result}\n'
    elif op == '*':
        result = a * b
        stack.append(result)
        if isinstance(result, float):
            vm_code += f'FMUL\nPUSHF {result}\n'
        else: vm_code += f'MUL\nPUSHI {result}\n'
        
    elif op == '/':
        result = a / b
        stack.append(result)
        if isinstance(result, float):
            vm_code += f'FDIV\nPUSHF {result}\n'
        else: vm_code += f'DIV\nPUSHI {result}\n'
    elif op == '%':
        result = a % b
        stack.append(result)
        vm_code += f'MOD\nPUSHI {result}\n'

def p_exp_relacionais(p):
    '''exp_relacionais : comando comando NOT
                       | comando comando INF
                       | comando comando SUP
                       | comando comando INFEQ
                       | comando comando SUPEQ'''
    global vm_code
    if len(stack) < 2:
        print("Error: Not enough members on the stack for relational operation")
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
    
def p_values(p):
    '''values : NUMBER
              | STRING''' 
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
        vm_code += f"PUSHS {p[1]}\n"

#def p_flow_control(p):
#    '''flow_control : if_else_then_comando'''
                   #| while_do_loop_comando
                   #| begin_repeat_exit_comando'''
#    p[0] =  p[1]
   
#def if_else_then_comando(p):
    #'''if_else_then_comando : comandos IF comandos THEN
                            #| comandos IF comandos ELSE comandos THEN'''
    
def p_functions(p):
    '''functions : stdout
                 | dot
                 | space
                 | dup
                 | comment
                 | drop
                 | swap
                 | rot
                 | over
                 | concat
                 | cr
                 | emit
                 | char
                 | key
                 | spaces
                 | 2dup'''
    p[0] = p[1] 

def p_STDOUT(p):
    '''stdout : STDOUT'''
    global vm_code
    value = p[1]
    stack.append(value)
    vm_code += f'PUSHS "{value}"\nWRITES\n'
    
def p_DOT(p):
    '''dot : DOT'''
    global vm_code
    if len(stack) == 0:
        print("Error: Not enough members in Stack for DOT")
        return
    value = " "
    top_value = stack.pop()
    if isinstance(top_value, int):
        vm_code += f'WRITEI\nPUSHS "{value}"\nWRITES\nPUSHI {top_value}\n'
    elif isinstance(top_value, float):
        vm_code += f'WRITEF\nPUSHS "{value}"\nWRITES\nPUSHF {top_value}\n'
    elif isinstance(top_value, str):
        vm_code += f'WRITES\nPUSHS "{value}"\nWRITES\nPUSHS {top_value}\n'
    p[0] = top_value
    
def p_SPACE(p):
    '''space : SPACE'''
    global vm_code
    space = " "
    vm_code += f'PUSHS "{space}"\nWRITES\n'
    stack.append(space)
    p[0] = " SPACE "

def p_DUP(p):
    '''dup : DUP'''
    if len(stack) == 0:
        print("Error: Not enough members in Stack for DUP")
        return
    global vm_code
    top_value = stack[-1]
    if isinstance(top_value, int):
        vm_code += f"PUSHI {top_value}\n"
    elif isinstance(top_value, float):
        vm_code += f"PUSHF {top_value}\n"
    elif isinstance(top_value, str):
        vm_code += f"PUSHS {top_value}\n"
    stack.append(top_value)
    p[0] = top_value
    
def p_COMMENT(p):
    '''comment : COMMENT_LINE
               | COMMENT_BLOCK'''
    global vm_code
    comment = p[1]
    vm_code += f"// {comment}\n"
    
def p_DROP(p):
    '''drop : DROP'''
    p[0] = " DROP "
    if len(stack) == 0:
        print("Error: Not enough members on the stack for DROP operation")
        return
    global vm_code
    stack.pop()
    vm_code += "POP 1\n"
    
def p_SWAP(p):
    '''swap : SWAP'''
    if len(stack) < 2:
        print("Error: Not enough members on the stack for SWAP operation")
        return
    global vm_code
    a = stack.pop()
    b = stack.pop()
    vm_code += "SWAP\n"
    stack.append(a)
    stack.append(b)
    p[0] = " SWAP "

def p_ROT(p):
    '''rot : ROT'''
    if len(stack) < 3:
        print("Error: Not enough members on the stack for ROT operation")
        return
    a = stack.pop()  # 3 = c 
    b = stack.pop()  # 2 = b
    c = stack.pop()  # 1 = a 
    global vm_code
    vm_code += "POP 3\n"
    
    if isinstance(a, int):
        vm_code += f"PUSHI {a}\n"
    elif isinstance(a, float):
        vm_code += f"PUSHF {a}\n"
    elif isinstance(a, str):
        vm_code += f"PUSHS {a}\n"

    if isinstance(c, int):
        vm_code += f"PUSHI {c}\n"
    elif isinstance(c, float):
        vm_code += f"PUSHF {c}\n"
    elif isinstance(c, str):
        vm_code += f"PUSHS {c}\n"

    if isinstance(b, int):
        vm_code += f"PUSHI {b}\n"
    elif isinstance(b, float):
        vm_code += f"PUSHF {b}\n"
    elif isinstance(b, str):
        vm_code += f"PUSHS {b}\n"
        
    stack.append(b)
    stack.append(c)
    stack.append(a)
    p[0] = " ROT "
    
def p_OVER(p):
    '''over : OVER'''
    if len(stack) < 2:
        print("Error: Not enough members on the stack for OVER operation")
        return
    global vm_code
    a = stack.pop()
    b = stack.pop()
    
    if isinstance(b, int):
        vm_code += f"PUSHI {b}\n"
    elif isinstance(b, float):
        vm_code += f"PUSHF {b}\n"
    elif isinstance(b, str):
        vm_code += f"PUSHS {b}\n"
        
    if isinstance(a, int):
        vm_code += f"PUSHI {a}\n"
    elif isinstance(a, float):
        vm_code += f"PUSHF {a}\n"
    elif isinstance(a, str):
        vm_code += f"PUSHS {a}\n"
        
    if isinstance(b, int):
        vm_code += f"PUSHI {b}\n"
    elif isinstance(b, float):
        vm_code += f"PUSHF {b}\n"
    elif isinstance(b, str):
        vm_code += f"PUSHS {b}\n"
    p[0] = " OVER "
    
def p_CONCAT(p):
    '''concat : CONCAT'''
    global vm_code
    if len(stack) < 2:
        print("Error: Not enough members on the stack for CONCAT operation")
        return
    str2 = stack.pop()
    str1 = stack.pop()
    
    stack.append(str1 + str2)
    vm_code += "CONCAT\n"
    
def p_CR(p):
    '''cr : CR'''
    global vm_code
    par = "\n"
    vm_code += f'PUSHS "{par}"\nWRITES\n'
    p[0] = " CR "
    
def p_EMIT(p):
    '''emit : EMIT'''
    global vm_code
    ascii_value = p[1]
    if p[1] == None:
        vm_code += f"WRITECHR\n"
    else:
        vm_code += f"PUSHI {ascii_value}\nWRITECHR\n"
    stack.append(ascii_value)
    p[0] = " EMIT "
    
def p_CHAR(p):
    '''char : CHAR'''
    global vm_code
    ascii_value = ord(p[1])
    vm_code += f"PUSHI {ascii_value}\n"
    stack.append(ascii_value)
    p[0] = " CHAR "
    
def p_KEY(p):
    '''key : KEY'''
    global vm_code
    string = '"Introduza um caracter:"'
    vm_code += f"PUSHS {string}\nWRITES\nREAD\n"
    stack.append(string)
    p[0] = " KEY "
    
def p_SPACES(p):
    '''spaces : SPACES'''
    global vm_code
    space = " "
    while p[1] > 0:
        vm_code += f'PUSHS "{space}"\nWRITES\n'
        stack.append(space)
        p[1] -= 1
    p[0] = " SPACES "
    
def p_2DUP(p):
    '''2dup : 2DUP'''
    if len(stack) < 1:
        print("Error: Not enough members in Stack for 2DUP")
        return
    global vm_code
    a = stack[-2]
    b = stack[-1]
    if isinstance(a, int):
        vm_code += f"PUSHI {a}\n"
    elif isinstance(a, float):
        vm_code += f"PUSHF {a}\n"
    elif isinstance(a, str):
        vm_code += f"PUSHS {a}\n"
        
    if isinstance(b, int):
        vm_code += f"PUSHI {b}\n"
    elif isinstance(b, float):
        vm_code += f"PUSHF {b}\n"
    elif isinstance(b, str):
        vm_code += f"PUSHS {b}\n"
    stack.append(a)
    stack.append(b)
    p[0] = " 2DUP "

def p_creating_funcs(p):
    '''creating_funcs : func_criada
                      | function'''
    p[0] = p[1]          
    
def p_function(p):
    '''function : FUNCTION
                | FUNCTION_CALL'''
    global vm_code
    if isinstance(p[1], str): 
        for f in current_function:
            for func_name, func_body in function_definitions.items():
                if f == func_name:
                    vm_code += f"PUSHA {func_name}\nCALL\n\n"
                    vm_code += f"{func_name}:\n"
                    body_parts = func_body.split(" ")
                    body_content = " ".join(body_parts[2:-1])
                    
                    parser.parse(body_content)
        
    print(body_content)                    
    print(function_definitions)
        
def p_func_criada(p):
    '''func_criada : FUNC_BODY'''
    global vm_code 
    func_body = p[1]
    body_parts = func_body.split(" ")
    body_name = body_parts[1]
    function_definitions[body_name] = func_body
    current_function.append(body_name)

def p_error(p):
    if p:
        print("Syntax error:", p)
        parser.errok()

parser = yacc.yacc()

def parse_input(input_string):
    parser.parse(input_string)
    return vm_code