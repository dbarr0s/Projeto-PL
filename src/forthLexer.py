import ply.lex as lex

# Lista de tokens
tokens = [
    'FUNCTION',
    'STRING',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'NOT',
    'INF',
    'SUP',
    'INFEQ',
    'SUPEQ',
    'EXCLAMATION',
    'AT',
    'DOT',
    'COLON',
    'SEMICOLON',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'STDOUT',
    'CHAR',
    'COMMENT_LINE',
    'COMMENT_BLOCK',
    'NEWLINE',
    'IF',
    'ELSE',
    'THEN',
    'WHILE',
    'DO',
    'LOOP',
    'BEGIN',
    'REPEAT',
    'EXIT',
    'DROP',
    'SWAP',
    'ROT',
    'OVER',
    'CONCAT',
    'DUP',
    'EMIT',
    'CR',
    'KEY',
    'SPACE',
    'SPACES',
    '2DUP',
    'FUNCTION_CALL',
    'FUNC_BODY',
    'VARIABLE_DEFENITION',
    'VARIABLE_ASSIGNMENT',
    'VARIABLE_FETCH',
    'VARIABLE_PRINT'
    ] 

# Expressões Aritméticas
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'

# Expressões Relacionais
t_NOT = r'\='
t_INF = r'<'
t_SUP = r'>'
t_INFEQ = r'<='
t_SUPEQ = r'>='

# Símbolos
t_EXCLAMATION = r'!'
t_AT = r'@'
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'

# Expressões de Controlo de Fluxo
t_DO = r'[Dd][Oo]'
t_LOOP = r'[Ll][Oo][Oo][Pp]'
t_BEGIN = r'[Bb][Ee][Gg][Ii][Nn]'
t_WHILE = r'[Ww][Hh][Ii][Ll][Ee]'
t_REPEAT = r'[Rr][Ee][Pp][Ee][Aa][Tt]'
t_EXIT = r'[Ee][Xx][Ii][Tt]'

def t_IF(t):
    r'[Ii][Ff]'
    return t

def t_ELSE(t):
    r'[Ee][Ll][Ss][Ee]'
    return t

def t_THEN(t):
    r'[Tt][Hh][Ee][Nn]'
    return t

# Expressões de Variáveis
def t_VARIABLE_DEFENITION(t):
    R'VARIABLE\s+[^\s]+'
    t.value = t.value[9:]
    return t

def t_VARIABLE_ASSIGNMENT(t):
    r'\w+\s[A-Z]+\s!'
    parts = t.value.split()
    if parts[0].isdigit():
        t.value = (int(parts[0]), parts[1])
    elif parts[0].isfloat():
        t.value = (float(parts[0]), parts[1])
    else:
        t.value = (parts[0], parts[1])
    return t

def t_VARIABLE_FETCH(t):
    r'[A-Z]+\s@'
    parts = t.value.split()
    if isinstance(parts[0], str):
        t.value = str(parts[0])
    elif isinstance(parts[0], int):
        t.value = int(parts[0])
    elif isinstance(parts[0], float):
        t.value = float(parts[0])
    return t

def t_VARIABLE_PRINT(t):
    r'[A-Z]+\s\?'
    parts = t.value.split()
    t.value = parts[0]
    return t

# Expressões de Funções
def t_2DUP(t):
    r'[2][Dd][Uu][Pp]'
    return t

def t_SPACES(t):
    r'\d+\s+SPACES'
    t.value = int(t.value.split()[0])
    return t

def t_KEY(t):
    r'[Kk][Ee][Yy]'
    return t

def t_CHAR(t):
    r'CHAR\s+.'
    t.value = str(f'{t.value[5]}')
    return t

def t_EMIT(t):
    r'\d*\s*EMIT'
    parts = t.value.split()
    if parts[0].isdigit():
        t.value = int(parts[0])
    else:
        t.value = None
    return t

def t_CR(t):
    r'[Cc][Rr]'
    return t

def t_CONCAT(t):
    r'[Cc][Oo][Nn][Cc][Aa][Tt]'
    return t

def t_OVER(t):
    r'[Oo][Vv][Ee][Rr]'
    return t

def t_ROT(t):
    r'[Rr][Oo][Tt]'
    return t

def t_SWAP(t):
    r'[Ss][Ww][Aa][Pp]'
    return t

def t_DROP(t):
    r'[Dd][Rr][Oo][Pp]'
    return t

def t_DUP(t):
    r'[Dd][Uu][Pp]'
    return t

def t_SPACE(t):
    r'[Ss][Pp][Aa][Cc][Ee]'
    t.value = str(" ")
    return t

def t_FUNCTION(t):
    r'[a-zA-Z_][a-zA-Z0-9_-]*'
    t.value = str(t.value)
    return t

def t_FUNCTION_CALL(t):
    r'([0-9]+\s+)*[a-zA-Z_][a-zA-Z0-9_-]*'
    numbers_and_function = t.value.split()
    t.value = numbers_and_function 
    return t

def t_FUNC_BODY(t):
    r':\s*(\w+)\s*(.*?)\s*;'
    t.value = t.value   
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'"([^"]|\s)*"'
    t.value = str(t.value)
    return t

# É o token que representa a função de saída de dados (".")
def t_STDOUT(t):
    r'\.\s*"([^"]*)"\s*'
    t.value = t.value[3:-1]
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t\n'

def t_COMMENT_LINE(t):
    r'\\.*'
    return t

def t_COMMENT_BLOCK(t):
    r'\(.*?\)'
    return t

# Contagem de novas linhas
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro
def t_error(t):
    print("Caractere inválido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()