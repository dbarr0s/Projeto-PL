import ply.yacc as yacc
from lexer import tokens

stack = []

def p_expression(p):
    '''expression : expression expression operacao
                  | expression DUP
                  | NUMBER
                  | DOT
    '''
    if len(p) > 2:
        b = stack.pop()
        a = stack.pop()
        if isinstance(p[3], str):
            if p[3]=='+': #SUM
                stack.append(a + b)
            elif p[3] == '-': #MINUS
                stack.append(a - b)
            elif p[3] == '*': #TIMES
                stack.append(a * b)
            elif p[3] == '/': #DIVIDE
                if b!= 0:
                    stack.append(a / b)
                else:
                    print("Div p/ zero")
            elif p[3] == '%': #MOD
                stack.append(a % b)
            elif p[3] == '^': #POWER
                stack.append(a ** b) 
    elif p[1] == 'DUP': #DUP 
        if len(stack) > 0:
            stack.append(stack[-1])
        else:
            print("")
    elif p[1] == '.':
        if len(stack) > 0:
            print(stack.pop())
    else:
        stack.append(p[1])  

def p_operacao(p):
    '''operacao : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD
                | POWER   
    '''
    p[0] = p[1]  

#Tratar erros
def p_error(p):
    print("Erro de sintaxe.")

# Build parser
parser = yacc.yacc()
