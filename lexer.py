import ply.lex as lex



stack = []
# Definição dos tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'POWER',
    'DUP',
    'DOT'
)

# Regras de regex para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_POWER = r'\^'
t_DUP = r'DUP'
t_DOT = r'\.'

#números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar whitespaces
t_ignore = ' \t'

# Tratamento de newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Tratamento de erro para caracteres inválidos
def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()