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
rel_ops = {'>', '<', '!=', '='}
ar_ops = {'+', '-', '*', '/'}
hierarchy_table = {'*': 1, '/': 1, '+': 2, '-': 2, '<': 3, '>': 3, '!=': 3, '=': 4}
temp_count = 0
env = {}
quadruple_array = []
operator_stack = []
operands_stack = []
pending_jumps = []
token_list = []
clear_syntax = True
counter = 1


def get_operation_result_type(a_type, b_type, operation):
    if operation in rel_ops:
        return 'int'
    return a_type if a_type == b_type else 'float'


def add_to_step_stack(step):
    if step is None or step.upper in tokens:
        return
    step_stack.append(step)


def process_step_stack():
    if not clear_syntax:
        return False
    types = {'int', 'float'}
    while len(step_stack):
        step = step_stack.pop()
        if step in types:
            var_type = step
            for i in var_line:
                var_table[i] = var_type
            var_line.clear()
            continue
        else:
            if step in var_table or step in var_line:
                print("ERROR: VARIABLE '" + step + "' WAS PREVIOUSLY DECLARED")
                return False
            else:
                var_line.append(step)
    return True




def solve_operation():
    global operator_stack, operands_stack, quadruple_array, temp_count, env
    right_operand = operands_stack.pop()
    left_operand = operands_stack.pop()
    operator = operator_stack.pop()
    temp_count = temp_count + 1
    new_temp_var = 'T' + str(temp_count)
    quadruple_array.append([operator, left_operand, right_operand, new_temp_var])
    operands_stack.append(new_temp_var)
    if operator == '=':
        env[left_operand] = right_operand


# JUMPS STRUCTURE

# IN PENDING JUMPS
# TYPE OF JUMP | POSITION IN QUADRUPLES | WHERE SHOULD IT JUMP

# IN QUADRUPLES
# TYPE OF JUMP | CONDITION (OPTIONAL) | WHERE SHOULD IT JUMP

def process_tokens():
    return
    for token in token_list:
        if token == '{':
            # If we enter a new level, that means we don't need our previous operands and operators
            operands_stack.clear()
            operator_stack.clear()
            continue
        elif token == 'if':
            # If we enter an if, we just need to add a pending jump for where we go in case condition is false
            pending_jumps.append(['goToF', '', ''])
            quadruple_array.append(['goToF', ])
        elif token == 'else':
            # We add a jump that tells the true condition to skip the else and update the previous jump
            pending_jump = pending_jumps.pop()
            pending_jumps
        elif token == 'while':
            # In this case, we need to check if there's a previous DO in the pending jumps, otherwise
            # we don't know where the while should go if true or if false
            if len(pending_jumps) and pending_jumps[-1][0] == 'goToV':
                print('found a do while')
        counter +=  1
    # if step == '(':
    #     operator_stack.append(step)
    # elif step in rel_ops:
    #     # Relation operators get immediately added to the stack. No operations needed yet
    #     operator_stack.append(step)
    # elif step in ar_ops:
    #     # Before introducing a new operator, we always have to check what the last operator's hierarchy
    #     if len(operator_stack) == 0 or operator_stack[-1] == '(':
    #         # If the operator stack is empty, or we entered a new section - we add the operator
    #         operator_stack.append(step)
    #     while len(operator_stack) and hierarchy_table[operator_stack[-1]] <= hierarchy_table[step]:
    #         # If last operator has higher or equal hierarchy, we need to solve
    #         solve_operation()
    #     operator_stack.append(step)
    # elif step == ')':
    #     # If we find a closing parenthesis, we need to clear everything inside
    #     while len(operator_stack) and operator_stack[-1] != '(':
    #         solve_operation()
    #     operator_stack.pop()
    # else:
    #     # If no other conditions were true, then we found an ID
    #     operands_stack.append(step)
    #     # global operator_stack
    #     # # After doing all the steps, we need to clear any remaining operations that were already ordered correctly
    #     # while len(operator_stack):
    #     #     solve_operation()


def flatten_list(items):
    flattened_list = []
    for item in items:
        if isinstance(item, list):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)
    return flattened_list

def print_quadruples():
    print('----- QUADRUPLE LIST -----')
    for quadruple in quadruple_array:
        print(quadruple)
    print('--------------------------')

def p_programa(p):
    '''
    programa : PROGRAM ID EOL programa1
    '''
    p[0] = p[4]
    token_list.extend(flatten_list(p[0]))


def p_programa1(p):
    '''
    programa1 : body END
                | vars body END
    '''
    if len(p) == 3:
        p[0] = [p[1], p[2]]
    else:
        p[0] = [p[2], p[3]]
    p[0] = flatten_list(p[0])

def p_vars(p):
    '''
    vars : VAR ID vars1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])

def p_vars1(p):
    '''
    vars1 : COMMA ID vars1
            | COLON type
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_vars2(p):
    '''
    vars2 : ID vars1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_vars3(p):
    '''
    vars3 : vars2
        |
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])

def p_type(p):
    '''
    type : INT EOL vars3
        | FLOAT EOL vars3
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])

def p_body(p):
    '''
    body : LBRACKET body1 RBRACKET
    '''
    p[0] = p[2]
    p[0] = flatten_list(p[0])

def p_body1(p):
    '''
    body1 : statement body1
        |
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])

def p_statement(p):
    '''
    statement : assign
                | condition
                | cycle
                | print
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_print(p):
    '''
    print : COUT LPAREN print1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_print1(p):
    '''
    print1 : expression print2
        | CTE_STRING print2
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_print2(p):
    '''
    print2 : COMMA print1
        | RPAREN EOL
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_assign(p):
    '''
    assign : ID EQUAL expression EOL
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])

def p_expression(p):
    '''
    expression : exp expression1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_expression1(p):
    '''
    expression1 : GREATER exp
                | LESS exp
                | NOTEQUAL exp
                |
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_cycle(p):
    '''
    cycle : DO body WHILE LPAREN expression RPAREN EOL
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_condition(p):
    '''
    condition : IF LPAREN expression RPAREN body condition1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])

def p_condition1(p):
    '''
    condition1 : ELSE body EOL
                | EOL
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
            | PLUS factor1
            | MINUS factor1
            | factor1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_factor1(p):
    '''
    factor1 : ID
            | cte
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_exp(p):
    '''
    exp : exp1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_exp1(p):
    '''
    exp1 : term PLUS exp1
        | term MINUS exp1
        | term
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_term(p):
    '''
    term : term1
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_term1(p):
    '''
    term1 : factor MULTIPLY term1
        | factor DIVIDE term1
        | factor
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_cte(p):
    '''
    cte : CTE_INT
        | CTE_FLOAT
    '''
    p[0] = p[1:]
    p[0] = flatten_list(p[0])
def p_error(p):
    print("SYNTAX ERROR FOUND")
    print(p)



lexer = lex.lex()
parser = yacc.yacc()

program_string = 'program pt2; var i, j, c: int; j : float; {if(a>b){c=a*b;};} end'

compiled = parser.parse(program_string)

print(token_list)

process_tokens()






