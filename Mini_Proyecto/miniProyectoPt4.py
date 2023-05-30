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

# JUMPS STRUCTURE

# IN PENDING JUMPS
# TYPE OF JUMP | EMPTY | EMPTY

# IN JUMPS
# TYPE OF JUMP | POSITION IN QUADRUPLES | EMPTY

# IN QUADRUPLES
# TYPE OF JUMP | CONDITION (OPTIONAL) | WHERE SHOULD IT JUMP

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    global tokens
    if t.value.upper() in tokens:
        t.type = t.value.upper()
    return t

def t_CTE_STRING(t):
    r'\"(.+?)\"'
    return t

def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


var_type_table = {}
var_value_table = {}
var_stack = []
var_line = []
rel_ops = {'>', '<', '!='}
ar_ops = {'+', '-', '*', '/'}
hierarchy_table = {'*': 1, '/': 1, '+': 2, '-': 2, '<': 3, '>': 3, '!=': 3, '=': 4}
temp_count = 0
env = {}
quadruple_array = []
operator_stack = []
operands_stack = []
pending_jumps = []
jumps = []
token_list = []
breadcrumb_stack = []

counter = 1

# JUMPS STRUCTURE

# IN JUMPS
# TYPE OF JUMP | POSITION IN QUADRUPLES | EMPTY

# IN QUADRUPLES
# TYPE OF JUMP | CONDITION (OPTIONAL) | WHERE SHOULD IT JUMP


def process_jump():
    jump = jumps.pop()
    quadruple_array[jump[1] - 1][2] = len(quadruple_array) + 1


def get_operation_result_type(a_type, b_type, operation):
    if operation in rel_ops:
        return 'int'
    return a_type if a_type == b_type else 'float'


def add_to_var_stack(step):
    if step is None or step.upper in tokens:
        return
    if step in var_stack:
        print("ERROR: VARIABLE '" + step + "' HAS MULTIPLE DECLARATIONS")
        exit()
    var_stack.append(step)


def process_var_stack():
    types = {'int', 'float'}
    while len(var_stack):
        step = var_stack.pop()
        if step in types:
            var_type = step
            for i in var_line:
                var_type_table[i] = var_type
            var_line.clear()
            continue
        else:
            var_line.append(step)


def process_operation():
    global temp_count
    if not len(operator_stack):
        return
    right_operand = operands_stack.pop()
    left_operand = operands_stack.pop()
    operator = operator_stack.pop()
    temp_count = temp_count + 1
    new_temp_var = 'T' + str(temp_count)
    if operator == '=':
        quadruple_array.append([operator, left_operand, right_operand])
    else:
        quadruple_array.append([operator, left_operand, right_operand, new_temp_var])
        operands_stack.append(new_temp_var)
        if isinstance(left_operand, str):
            left_operand_type = var_type_table[left_operand]
        else:
            left_operand_type = 'int' if isinstance(left_operand, int) else 'float'
        if isinstance(right_operand, str):
            right_operand_type = var_type_table[right_operand]
        else:
            right_operand_type = 'int' if isinstance(right_operand, int) else 'float'
        temp_var_type = get_operation_result_type(left_operand_type, right_operand_type, operator)
        var_type_table[new_temp_var] = temp_var_type


def print_quadruples():
    print('----- QUADRUPLES -----')
    for index, quadruple in enumerate(quadruple_array):
        print(index + 1, quadruple)
    print('----------------------')


def print_var_type_table():
    print('--- VAR TYPE TABLE ---')
    for key in var_type_table:
        print('var:', key, '| type:', var_type_table[key])
    print('----------------------')


def print_var_value_table():
    print('--- VAR VALUE TABLE ---')
    for key in var_value_table:
        print('var:', key, '| value:', var_value_table[key])
    print('----------------------')

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
    add_to_var_stack(p[2])
    process_var_stack()


def p_vars1(p):
    '''
    vars1 : COMMA ID vars1
            | COLON type
    '''
    if len(p) == 4:
        add_to_var_stack(p[2])

def p_vars2(p):
    '''
    vars2 : ID vars1
    '''
    add_to_var_stack(p[1])


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
    var_stack.append(p[1])

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
    quadruple_array.append(['COUT', operands_stack.pop()])

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
    operands_stack.append(p[1])
    operator_stack.append(p[2])
    process_operation()

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
    if len(p) > 2:
        operator_stack.append(p[1])
        process_operation()

def p_cycle(p):
    '''
    cycle : do_helper body WHILE LPAREN expression_cycle RPAREN EOL
    '''
    quadruple_array.append(['GoToT', operands_stack.pop(), breadcrumb_stack.pop()])


def p_do_helper(p):
    '''
    do_helper : DO
    '''
    breadcrumb_stack.append(len(quadruple_array) + 1)


def p_expression_cycle(p):
    '''
    expression_cycle : expression
    '''
    pending_jumps.append(['goToT', '', ''])


def p_condition(p):
    '''
    condition : IF LPAREN expression_condition RPAREN body condition1
    '''
    if len(jumps):
        process_jump()


def p_expression_condition(p):
    '''
    expression_condition : expression
    '''
    quadruple_array.append(['GoToF', operands_stack.pop(), ''])
    jumps.append(['GoToF', len(quadruple_array)])


def p_condition1(p):
    '''
    condition1 : else_helper body EOL
                | EOL
    '''


def p_else_helper(p):
    '''
    else_helper : ELSE
    '''
    quadruple_array.append(['goTo', '', ''])
    process_jump()
    jumps.append(['goTo', len(quadruple_array), ''])


def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
            | PLUS factor1
            | MINUS factor1
            | factor1
    '''
    if len(p) == 3:
        operator_stack(p[1])
        process_operation()

def p_factor1(p):
    '''
    factor1 : ID
            | cte
    '''
    if p[1] is not None:
        operands_stack.append(p[1])


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
    if len(p) == 4:
        operator_stack.append(p[2])
        process_operation()

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
    if len(p) == 4:
        operator_stack.append(p[2])
        process_operation()

def p_cte(p):
    '''
    cte : CTE_INT
        | CTE_FLOAT
    '''
    operands_stack.append(p[1])

def p_error(p):
    print("SYNTAX ERROR FOUND")
    print(p)
    exit()


def check_declared(variable):
    if variable not in var_type_table:
        print("ERROR: UNDECLARED VARIABLE '" + variable + "' used")
        exit()


def check_initialized(variable):
    if variable not in var_value_table:
        print("ERROR: VARIABLE '" + variable + "' WAS DECLARED BUT NEVER INITIALIZED")
        exit()


def check_type_match(left_variable, right_variable):
    if var_type_table[left_variable] != var_type_table[right_variable]:
        print("ERROR: TYPE MISSMATCH FOR VARIABLE '" + left_variable + "'")
        exit()


def boot_vm():
    pos = 0
    while pos < len(quadruple_array):
        quadruple = quadruple_array[pos]
        if quadruple[0] in rel_ops or quadruple[0] in ar_ops or quadruple[0] == '=':
            # We entered an operation
            operator = quadruple[0]
            if operator == '=':
                left_operand = quadruple[2]
                right_operand = quadruple[1]
                # Assign has a specific process with not much re-usability
                if isinstance(right_operand, str):
                    check_initialized(right_operand)
                    check_type_match(left_operand, right_operand)
                    var_value_table[left_operand] = var_value_table[right_operand]
                else:
                    var_value_table[left_operand] = right_operand
            else:
                # For every other case, we can factor out some of the process to reduce number of lines
                left_operand = quadruple[1]
                right_operand = quadruple[2]
                left_operand_value = left_operand
                right_operand_value = right_operand
                store_variable = quadruple[3]
                if isinstance(left_operand, str):
                    check_declared(left_operand)
                    check_initialized(left_operand)
                    left_operand_value = var_value_table[left_operand]
                if isinstance(right_operand, str):
                    check_declared(right_operand)
                    check_initialized(right_operand)
                    right_operand_value = var_value_table[right_operand]
                match operator:
                    case '+':
                        var_value_table[store_variable] = left_operand_value + right_operand_value
                    case '-':
                        var_value_table[store_variable] = left_operand_value - right_operand_value
                    case '*':
                        var_value_table[store_variable] = left_operand_value * right_operand_value
                    case '/':
                        var_value_table[store_variable] = left_operand_value / right_operand_value
                    case '>':
                        var_value_table[store_variable] = 1 if left_operand_value > right_operand_value else 0
                    case '<':
                        var_value_table[store_variable] = 1 if left_operand_value < right_operand_value else 0
                    case '!=':
                        var_value_table[store_variable] = 1 if left_operand_value != right_operand_value else 0
            pos += 1
        elif quadruple[0] == 'COUT':
            print('COUT >>', var_value_table[quadruple[1]])
            pos += 1
        else:
            # Remaining cases are all jumps
            match quadruple[0]:
                case 'GoToT':
                    # DO WHILE
                    var_condition = quadruple[1]
                    if var_value_table[var_condition] > 0:
                        pos = quadruple[2] - 1
                    else:
                        pos += 1
                case 'GoToF':
                    # IF
                    var_condition = quadruple[1]
                    if var_value_table[var_condition] <= 0:
                        pos = quadruple[2] - 1
                    else:
                        pos += 1
                case 'GoTo':
                    # ELSE
                    pos = quadruple[1] - 1
    print("----- SUCCESSFULLY FINISHED THE PROCESS -----")


lexer = lex.lex()
parser = yacc.yacc()

# n is the nth fibonacci number
fibonacci = '''program pt2; var n, a, b, c: int; { 
                        n = 5;
                        a = 0;
                        b = 1;
                        c = 0;
                        do {
                            cout(c);
                            c = a + b;
                            a = b;
                            b = c;
                            n = n - 1;
                        } while (n > 0);
                    } end'''

# n is the number whose factorial will be calculated
factorial = '''program pt2; var n, a, b, c: int; { 
                        n = 5;
                        a = 1;
                        do {
                            a = a * n;
                            n = n - 1;
                        } while (n > 0);
                        cout(a);
                    } end'''

parser.parse(factorial)
# print_quadruples()

boot_vm()






