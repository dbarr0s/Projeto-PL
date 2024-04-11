import ply.lex as lex

# Lista de tokens
tokens = (
    'VARIABLE',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'POWER',
    'EQUAL',
    'LESS_THAN',
    'GREATER_THAN',
    'EXCLAMATION',
    'AT',
    'DOT',
    'COLON',
    'SEMICOLON',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'IF',
    'ELSE',
    'THEN',
    'DO',
    'LOOP',
    'BEGIN',
    'WHILE',
    'REPEAT',
    'EXIT',
    'DROP',
    'DUP',
    'SWAP',
    'ROT',
    'OVER',
    'STRING'
)

# Expressões regulares para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_POWER = r'\^'
t_EQUAL = r'='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_EXCLAMATION = r'!'
t_AT = r'@'
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_IF = r'[Ii][Ff]'
t_ELSE = r'[Ee][Ll][Ss][Ee]'
t_THEN = r'[Tt][Hh][Ee][Nn]'
t_DO = r'[Dd][Oo]'
t_LOOP = r'[Ll][Oo][Oo][Pp]'
t_BEGIN = r'[Bb][Ee][Gg][Ii][Nn]'
t_WHILE = r'[Ww][Hh][Ii][Ll][Ee]'
t_REPEAT = r'[Rr][Ee][Pp][Ee][Aa][Tt]'
t_EXIT = r'[Ee][Xx][Ii][Tt]'
t_DROP = r'[Dd][Rr][Oo][Pp]'
t_DUP = r'[Dd][Uu][Pp]'
t_SWAP = r'[Ss][Ww][Aa][Pp]'
t_ROT = r'[Rr][Oo][Tt]'
t_OVER = r'[Oo][Vv][Ee][Rr]'
t_STRING = r'\"[^\"]*[\wáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛàèìòùÀÈÌÒÙ\s]*\"' #Strings com acentos
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Definição do token NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Ignorar comentários entre parênteses
def t_COMMENT(t):
    r'\(.*\)'
    pass

# Contagem de novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro
def t_error(t):
    print("Caractere inválido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()