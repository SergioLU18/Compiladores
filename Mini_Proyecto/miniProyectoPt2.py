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


var_table = {}
step_stack = []
var_line = []
lexer = lex.lex()


def get_operation_result_type(a_type, b_type, operation):
    global rel_ops
    if operation in rel_ops:
        return 'int'
    return a_type if a_type == b_type else 'float'


def add_to_step_stack(step):
    global step_stack, tokens
    if step is None or step.upper in tokens:
        return
    step_stack.append(step)


def process_step_stack():
    global step_stack, var_table, var_line
    types = {'int', 'float'}
    while len(step_stack):
        step = step_stack.pop()
        if step in types:
            var_type = step
            for i in var_line:
                var_table[i] = var_type
            var_line = []
            continue
        else:
            if step in var_table or step in var_line:
                print("ERROR: VARIABLE '" + step + "' WAS PREVIOUSLY DECLARED")
                return
            else:
                var_line.append(step)
    print(var_table)
    print('Code compiled without errors')


def generate_operation_quadruple(operands_stack, operator_stack, quadruple_array):
    global temp_count
    right_operand = operands_stack.pop()
    left_operand = operands_stack.pop()
    operator = operator_stack.pop()
    temp_count = temp_count + 1
    new_temp_var = 'T' + str(temp_count)
    quadruple_array.append([operator, right_operand, left_operand, new_temp_var])
    operands_stack.append(new_temp_var)


rel_ops = {'>', '<', '!='}
ar_ops = {'+', '-', '*', '/'}
hierarchy_table = {'+': 2, '-': 2, '*': 1, '/': 1}
temp_count = 0

def process_expression(expression):
    global rel_ops, ar_ops, hierarchy_table, temp_count
    operator_stack = []
    operands_stack = []
    quadruple_array = []
    steps = expression.split()
    for index, step in enumerate(steps):
        if step in rel_ops or step in ar_ops:
            # Before introducing a new operator, we always have to check what the last operator's hierarchy
            if len(operator_stack) == 0:
                # If there are no operands, we just continue
                operator_stack.append(step)
                continue
            if hierarchy_table[step] == hierarchy_table[operator_stack[-1]]:
                # If both have the same hierarchy, then we can solve the last operator
                generate_operation_quadruple(operands_stack, operator_stack, quadruple_array)
            elif hierarchy_table[step] == 2:
                # If new operator has lower hierarchy, then we solve the last operator
                generate_operation_quadruple(operands_stack, operator_stack, quadruple_array)
            operator_stack.append(step)
        else:
            operands_stack.append(step)
            while index == len(steps) - 1 and len(operator_stack):
                generate_operation_quadruple(operands_stack, operator_stack, quadruple_array)
    for quadruple in quadruple_array:
        print(quadruple)
    print('Result is: ' + str(operands_stack.pop()))



def p_programa(p):
    '''
    programa : PROGRAM ID EOL programa1
    '''

def p_programa1(p):
    '''
    programa1 : body END
                | vars body END
    '''

def p_vars(p):
    '''
    vars : VAR ID vars1
    '''
    add_to_step_stack(p[2])

def p_vars1(p):
    '''
    vars1 : COMMA ID vars1
            | COLON type
    '''
    add_to_step_stack(p[2])

def p_vars2(p):
    '''
    vars2 : ID vars1
    '''
    add_to_step_stack(p[1])

def p_vars3(p):
    '''
    vars3 : vars2
        |
    '''

def p_type(p):
    '''
    type : INT EOL vars3
        | FLOAT EOL vars3
    '''
    add_to_step_stack(p[1])

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
# parser.parse('program pt2; var i: int; j : float; {} end')
# process_step_stack()
process_expression('A / B + C + D + E * F')



