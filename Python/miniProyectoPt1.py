import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'PROGRAM',
    'ID',
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'LESS',
    'GREATER',
    'COMMA',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_STRING',
    'LBRACKET',
    'RBRACKET',
    'DO',
    'WHILE',
    'IF',
    'ELSE',
    'COUT',
    'NOTEQUAL',
    'END',
    'VAR',
    'COLON',
    'EOL'
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'\='
t_LESS = r'\<'
t_GREATER = r'\>'
t_COMMA = r'\,'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_NOTEQUAL = r'\!='
t_COLON = r'\:'
t_EOL = r'\;'

t_ignore = r' '

def t_CTE_FLOAT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_CTE_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    global tokens
    if t.value.upper() in tokens:
        t.type = t.value.upper();
    return t;

def t_CTE_STRING(t):
    r'\"(.+?)\"'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

def p_programa(p):
    '''
    programa : PROGRAM ID EOL programa1
    '''
    print('Code compiled without errors')

def p_programa1(p):
    '''
    programa1 : body END
                | vars body END
    '''

def p_vars(p):
    '''
    vars : VAR ID vars1
    '''

def p_vars1(p):
    '''
    vars1 : COMMA ID vars1
            | COLON type EOL vars3
    '''

def p_vars2(p):
    '''
    vars2 : ID vars1
    '''

def p_vars3(p):
    '''
    vars3 : vars2
        |
    '''

def p_type(p):
    '''
    type : INT
        | FLOAT
    '''

def p_body(p):
    '''
    body : LBRACKET body1 RBRACKET
    '''


def p_body1(p):
    '''
    body1 : statement body1
        |
    '''


def p_statement(p):
    '''
    statement : assign
                | condition
                | cycle
                | print
    '''

def p_print(p):
    '''
    print : COUT LPAREN print1
    '''


def p_print1(p):
    '''
    print1 : expression print2
        | CTE_STRING print2
    '''


def p_print2(p):
    '''
    print2 : COMMA print1
        | RPAREN EOL
    '''

def p_assign(p):
    '''
    assign : ID EQUAL expression EOL
    '''

def p_expression(p):
    '''
    expression : exp expression1
    '''

def p_expression1(p):
    '''
    expression1 : GREATER exp
                | LESS exp
                | NOTEQUAL exp
                |
    '''

def p_cycle(p):
    '''
    cycle : DO body WHILE LPAREN expression RPAREN EOL
    '''

def p_condition(p):
    '''
    condition : IF LPAREN expression RPAREN body condition1
    '''

def p_condition1(p):
    '''
    condition1 : ELSE body EOL
                | EOL
    '''

def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
            | PLUS factor1
            | MINUS factor1
            | factor1
    '''

def p_factor1(p):
    '''
    factor1 : ID
            | cte
    '''

def p_exp(p):
    '''
    exp : exp1
    '''

def p_exp1(p):
    '''
    exp1 : term PLUS exp1
        | term MINUS exp1
        | term
    '''

def p_term(p):
    '''
    term : term1
    '''

def p_term1(p):
    '''
    term1 : factor MULTIPLY term1
        | factor DIVIDE term1
        | factor
    '''

def p_cte(p):
    '''
    cte : CTE_INT
        | CTE_FLOAT
    '''

def p_error(p):
    print("Syntax error found")
    print(p)


parser = yacc.yacc()

# parser.parse('program case1; var i: int; { i = 0; i = ( i + 1; } end')

# parser.parse('program case2; var a, b, c, d : float; {} end')

# parser.parse('programaa case3; var noFuncionara : string; {} end')

# parser.parse('program case4; var a: int; { i = 0; if(i > 0) { cout("true"); } else { cout("false"); }; } end')

# parser.parse('program case5; var a: int; b: float; { a = 2.5; b = 3; } end')




