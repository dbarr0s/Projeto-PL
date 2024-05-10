import ply.yacc as yacc
from forthLexer import tokens, lexer

# Definição da stack
stack = []
vm_code = ""
function_definitions = {}
variables = {}
current_if = 0
current_else = 0
current_loop = 0

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
               | creating_funcs
               | variable
               | flow_control'''
    
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
            vm_code += f'FADD\n'
        else: vm_code += f'ADD\n'
    elif op == '-':
        result = a - b
        stack.append(result)
        if isinstance(result, float):
            vm_code += f'FSUB\n'
        else: vm_code += f'SUB\n'
    elif op == '*':
        result = a * b
        stack.append(result)
        if isinstance(result, float):
            vm_code += f'FMUL\n'
        else: vm_code += f'MUL\n'
    elif op == '/':
        result = a / b
        stack.append(result)
        if isinstance(result, float):
            vm_code += f'FDIV\n'
        else: vm_code += f'DIV\n'
    elif op == '%':
        result = a % b
        stack.append(result)
        vm_code += f'MOD\n'

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

def p_flow_control(p):
    '''flow_control : if
                    | else
                    | then
                    | do
                    | loop'''
    p[0] =  p[1]

def p_if(p):
    '''if : IF'''
    global vm_code, current_else
    if len(stack) == 0:
        print("Error: Not enough members on the stack for IF operation")
        return
    vm_code += f'jz else{current_else}\n'

def p_else(p):
    '''else : ELSE'''
    global vm_code, current_else
    if len(stack) == 0:
        print("Error: Not enough members on the stack for ELSE operation")
        return
    vm_code += f'else{current_else}:\n'
    current_else += 1
    
def p_then(p):
    '''then : THEN'''
    global vm_code, current_if
    vm_code += f'jump endif{current_if}\n'
    vm_code += f'endif{current_if}:\n'
    current_if += 1

def p_do(p):
    '''do : DO'''
    global vm_code, current_loop, variables
    limit, index = p[1]
    variables[f'limit{current_loop}'] = limit
    var_len_1 = len(variables) - 1
    variables[f'index{current_loop}'] = index
    var_len_2 = len(variables) - 1

    vm_code += f'PUSHG {var_len_1}\n'
    vm_code += f'PUSHI {limit}\n'
    vm_code += f'STOREG {var_len_1}\n'

    vm_code += f'PUSHG {var_len_2}\n'
    vm_code += f'PUSHI {index}\n'
    vm_code += f'STOREG {var_len_2}\n'

    vm_code += f'WHILE{current_loop}:\n'
    vm_code += f'PUSHG {var_len_1}\n'
    vm_code += f'PUSHG {var_len_2}\n'
    vm_code += f'SUP\n'
    vm_code += f'jz ENDWHILE{current_loop}\n'
    current_loop += 1

def p_loop(p):
    '''loop : LOOP'''
    global vm_code, current_loop, variables
    limit_var_index = list(variables.keys()).index(f'limit{current_loop - 1}') + 1
    vm_code += f'PUSHG {limit_var_index}\n'
    vm_code += f'PUSHI 1\n'
    vm_code += f'ADD\n'
    vm_code += f'STOREG {limit_var_index}\n'
    vm_code += f'jump WHILE{current_loop - 1}\n'
    vm_code += f'ENDWHILE{current_loop - 1}:\n'
    
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
    top_value = stack.pop()
    if isinstance(top_value, int):
        vm_code += f'WRITEI\n'
    elif isinstance(top_value, float):
        vm_code += f'WRITEF\n'
    elif isinstance(top_value, str):
        vm_code += f'WRITES\n'
    p[0] = top_value
    
def p_SPACE(p):
    '''space : SPACE'''
    global vm_code
    space = " "
    vm_code += f'PUSHS "{space}"\nWRITES\n'
    stack.append(space)
    p[0] = " SPACE "

def p_DUP(p):
    '''dup : comando DUP'''
    if len(stack) == 0:
        print("Error: Not enough members in Stack for DUP")
        return
    global vm_code
    vm_code += f'DUP 1\n'
    stack.append(stack[-1])
    
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
    vm_code += f'WRITELN\n'
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
    
def p_variable(p):
    '''variable : variable_definition
                 | variable_assignment
                 | variable_fetch
                 | variable_print'''
    p[0] = p[1]

def p_variable_definition(p):
    '''variable_definition : VARIABLE_DEFENITION'''
    global vm_code, variables
    var = p[1]
    variables[var] = 0
    var_number = len(variables) - 1
    vm_code += f'PUSHG {var_number}\n'

def p_variable_assignment(p):
    '''variable_assignment : VARIABLE_ASSIGNMENT'''
    global vm_code, variables
    value, var = p[1]
    var_index = list(variables.keys()).index(var)
    if isinstance(value, int):
        vm_code += f'PUSHI {value}\n'
    elif isinstance(value, float):
        vm_code += f'PUSHF {value}\n'
    elif isinstance(value, str):
        vm_code += f'PUSHS {value}\n'
    variables[var] = value
    vm_code += f'STOREG {var_index}\n'

def p_variable_fetch(p):
    '''variable_fetch : VARIABLE_FETCH'''
    global vm_code, variables
    var = p[1]
    value = variables[var]
    stack.append(value)
    var_index = list(variables.keys()).index(var)
    vm_code += f'PUSHG {var_index}\n'

def p_variable_print(p):
    '''variable_print : VARIABLE_PRINT'''
    global vm_code, variables
    var = p[1]
    value = variables[var]
    var_index = list(variables.keys()).index(var)
    if isinstance(value, int):
        vm_code += f'PUSHG {var_index}\nWRITEI\n'
    elif isinstance(value, float):
        vm_code += f'PUSHG {var_index}\nWRITEF\n'
    elif isinstance(value, str):
        vm_code += f'PUSHG {var_index}\nWRITES\n'

def p_creating_funcs(p):
    '''creating_funcs : func_criada
                      | function
                      | creating_funcs function
                      | creating_funcs func_criada'''
    p[0] = p[1] 
    
def p_function(p):
    '''function : FUNCTION
                | FUNCTION_CALL'''
    global vm_code
    executable_parts = []
    if isinstance(p[1], str): 
        vm_code += f"PUSHA {p[1]}\nCALL\n\n"
        vm_code += f"{p[1]}:\n"
        for func_name, func_body in function_definitions.items():
            print(function_definitions)
            if func_name == p[1]:
                body_parts = func_body.split(" ")  # DIVIDE A STRING EM PARTES
                body_content = " ".join(body_parts[2:-1])  # JUNTA AS PARTES DA STRING, QUE DEVE SER EXECUTADO
                print(body_content)
                for part in body_content.split(" "): 
                    print(part)
                    if part in function_definitions:
                        vm_code += f"PUSHA {part}\nCALL\n\n"
                        vm_code += f"{part}:\n"
                        body = function_definitions[part]
                        body_parts1 = body.split(" ")  # DIVIDE A STRING EM PARTES
                        body_content1 = " ".join(body_parts1[2:-1])  # JUNTA AS PARTES DA STRING, QUE DEVE SER EXECUTADO
                        parse_input(body_content1)
                    elif part in tokens:
                        parse_input(part)  
                    else:
                        executable_parts.append(part)       
        full_body_content = " ".join(executable_parts)
        parse_input(full_body_content)
        p[0] = p[1]
            
def p_func_criada(p):
    '''func_criada : FUNC_BODY'''
    global vm_code 
    func_body = p[1]
    body_parts = func_body.split(" ")
    body_name = body_parts[1]
    function_definitions[body_name] = func_body

def p_error(p):
    if p:
        print("Syntax error:", p)
        parser.errok()

parser = yacc.yacc()

def parse_input(input_string):
    parser.parse(input_string)
    return vm_code