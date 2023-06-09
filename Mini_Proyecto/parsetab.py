
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA COUT CTE_FLOAT CTE_INT CTE_STRING DIVIDE DO ELSE END EOL EQUAL FLOAT GREATER ID IF INT LBRACKET LESS LPAREN MINUS MULTIPLY NOTEQUAL PLUS PROGRAM RBRACKET RPAREN VAR WHILE\n    programa : PROGRAM ID EOL programa1\n    \n    programa1 : body END\n                | vars body END\n    \n    vars : VAR ID vars1\n    \n    vars1 : COMMA ID vars1\n            | COLON type\n    \n    vars2 : ID vars1\n    \n    vars3 : vars2\n        |\n    \n    type : INT EOL vars3\n        | FLOAT EOL vars3\n    \n    body : LBRACKET body1 RBRACKET\n    \n    body1 : statement body1\n        |\n    \n    statement : assign\n                | condition\n                | cycle\n                | print\n    \n    print : COUT LPAREN print1\n    \n    print1 : expression_print print2\n        | CTE_STRING print2\n    \n    print2 : COMMA print1\n        | RPAREN EOL\n    \n    expression_print : expression\n    \n    assign : ID EQUAL expression EOL\n    \n    expression : exp expression1\n    \n    expression1 : GREATER exp\n                | LESS exp\n                | NOTEQUAL exp\n                |\n    \n    cycle : do_helper body WHILE LPAREN expression RPAREN EOL\n    \n    do_helper : DO\n    \n    condition : IF LPAREN expression_condition RPAREN body condition1\n    \n    expression_condition : expression\n    \n    condition1 : else_helper body EOL\n                | EOL\n    \n    else_helper : ELSE\n    \n    factor : LPAREN expression RPAREN\n            | PLUS factor1\n            | MINUS factor1\n            | factor1\n    \n    factor1 : ID\n            | cte\n    \n    exp : exp1\n    \n    exp1 : term PLUS exp1\n        | term MINUS exp1\n        | term\n    \n    term : term1\n    \n    term1 : factor MULTIPLY term1\n        | factor DIVIDE term1\n        | factor\n    \n    cte : CTE_INT\n        | CTE_FLOAT\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,10,24,],[0,-1,-2,-3,]),'ID':([2,8,9,13,14,15,16,17,27,28,30,32,39,40,43,51,59,61,62,63,64,65,68,69,72,73,74,76,78,79,90,91,96,98,103,104,],[3,18,23,18,-15,-16,-17,-18,34,34,34,55,34,34,34,-19,-25,34,34,34,34,34,34,34,34,-20,34,-21,94,94,-22,-23,-33,-36,-31,-35,]),'EOL':([3,25,34,35,36,37,38,41,42,44,45,46,47,57,58,60,66,67,75,80,81,82,83,84,85,86,87,88,100,102,],[4,-12,-42,59,-30,-44,-47,-48,-51,-41,-43,-52,-53,78,79,-26,-39,-40,91,-27,-28,-29,-45,-46,-49,-50,-38,98,103,104,]),'LBRACKET':([4,7,20,22,31,56,71,77,78,79,92,93,95,97,99,101,],[8,8,8,-32,-4,-6,8,-5,-9,-9,-10,-8,-11,8,-37,-7,]),'VAR':([4,],[9,]),'END':([6,11,25,],[10,24,-12,]),'RBRACKET':([8,12,13,14,15,16,17,26,51,59,73,76,90,91,96,98,103,104,],[-14,25,-14,-15,-16,-17,-18,-13,-19,-25,-20,-21,-22,-23,-33,-36,-31,-35,]),'IF':([8,13,14,15,16,17,51,59,73,76,90,91,96,98,103,104,],[19,19,-15,-16,-17,-18,-19,-25,-20,-21,-22,-23,-33,-36,-31,-35,]),'COUT':([8,13,14,15,16,17,51,59,73,76,90,91,96,98,103,104,],[21,21,-15,-16,-17,-18,-19,-25,-20,-21,-22,-23,-33,-36,-31,-35,]),'DO':([8,13,14,15,16,17,51,59,73,76,90,91,96,98,103,104,],[22,22,-15,-16,-17,-18,-19,-25,-20,-21,-22,-23,-33,-36,-31,-35,]),'EQUAL':([18,],[27,]),'LPAREN':([19,21,27,28,30,43,50,61,62,63,64,65,68,69,72,74,],[28,30,43,43,43,43,72,43,43,43,43,43,43,43,43,43,]),'COMMA':([23,34,36,37,38,41,42,44,45,46,47,52,53,54,55,60,66,67,80,81,82,83,84,85,86,87,94,],[32,-42,-30,-44,-47,-48,-51,-41,-43,-52,-53,74,74,-24,32,-26,-39,-40,-27,-28,-29,-45,-46,-49,-50,-38,32,]),'COLON':([23,55,94,],[33,33,33,]),'WHILE':([25,29,],[-12,50,]),'ELSE':([25,88,],[-12,99,]),'PLUS':([27,28,30,34,38,41,42,43,44,45,46,47,61,62,63,64,65,66,67,68,69,72,74,85,86,87,],[39,39,39,-42,64,-48,-51,39,-41,-43,-52,-53,39,39,39,39,39,-39,-40,39,39,39,39,-49,-50,-38,]),'MINUS':([27,28,30,34,38,41,42,43,44,45,46,47,61,62,63,64,65,66,67,68,69,72,74,85,86,87,],[40,40,40,-42,65,-48,-51,40,-41,-43,-52,-53,40,40,40,40,40,-39,-40,40,40,40,40,-49,-50,-38,]),'CTE_INT':([27,28,30,39,40,43,61,62,63,64,65,68,69,72,74,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'CTE_FLOAT':([27,28,30,39,40,43,61,62,63,64,65,68,69,72,74,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'CTE_STRING':([30,74,],[53,53,]),'INT':([33,],[57,]),'FLOAT':([33,],[58,]),'MULTIPLY':([34,42,44,45,46,47,66,67,87,],[-42,68,-41,-43,-52,-53,-39,-40,-38,]),'DIVIDE':([34,42,44,45,46,47,66,67,87,],[-42,69,-41,-43,-52,-53,-39,-40,-38,]),'GREATER':([34,36,37,38,41,42,44,45,46,47,66,67,83,84,85,86,87,],[-42,61,-44,-47,-48,-51,-41,-43,-52,-53,-39,-40,-45,-46,-49,-50,-38,]),'LESS':([34,36,37,38,41,42,44,45,46,47,66,67,83,84,85,86,87,],[-42,62,-44,-47,-48,-51,-41,-43,-52,-53,-39,-40,-45,-46,-49,-50,-38,]),'NOTEQUAL':([34,36,37,38,41,42,44,45,46,47,66,67,83,84,85,86,87,],[-42,63,-44,-47,-48,-51,-41,-43,-52,-53,-39,-40,-45,-46,-49,-50,-38,]),'RPAREN':([34,36,37,38,41,42,44,45,46,47,48,49,52,53,54,60,66,67,70,80,81,82,83,84,85,86,87,89,],[-42,-30,-44,-47,-48,-51,-41,-43,-52,-53,71,-34,75,75,-24,-26,-39,-40,87,-27,-28,-29,-45,-46,-49,-50,-38,100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'programa1':([4,],[5,]),'body':([4,7,20,71,97,],[6,11,29,88,102,]),'vars':([4,],[7,]),'body1':([8,13,],[12,26,]),'statement':([8,13,],[13,13,]),'assign':([8,13,],[14,14,]),'condition':([8,13,],[15,15,]),'cycle':([8,13,],[16,16,]),'print':([8,13,],[17,17,]),'do_helper':([8,13,],[20,20,]),'vars1':([23,55,94,],[31,77,101,]),'expression':([27,28,30,43,72,74,],[35,49,54,70,89,54,]),'exp':([27,28,30,43,61,62,63,72,74,],[36,36,36,36,80,81,82,36,36,]),'exp1':([27,28,30,43,61,62,63,64,65,72,74,],[37,37,37,37,37,37,37,83,84,37,37,]),'term':([27,28,30,43,61,62,63,64,65,72,74,],[38,38,38,38,38,38,38,38,38,38,38,]),'term1':([27,28,30,43,61,62,63,64,65,68,69,72,74,],[41,41,41,41,41,41,41,41,41,85,86,41,41,]),'factor':([27,28,30,43,61,62,63,64,65,68,69,72,74,],[42,42,42,42,42,42,42,42,42,42,42,42,42,]),'factor1':([27,28,30,39,40,43,61,62,63,64,65,68,69,72,74,],[44,44,44,66,67,44,44,44,44,44,44,44,44,44,44,]),'cte':([27,28,30,39,40,43,61,62,63,64,65,68,69,72,74,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'expression_condition':([28,],[48,]),'print1':([30,74,],[51,90,]),'expression_print':([30,74,],[52,52,]),'type':([33,],[56,]),'expression1':([36,],[60,]),'print2':([52,53,],[73,76,]),'vars3':([78,79,],[92,95,]),'vars2':([78,79,],[93,93,]),'condition1':([88,],[96,]),'else_helper':([88,],[97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID EOL programa1','programa',4,'p_programa','miniProyectoPt4.py',202),
  ('programa1 -> body END','programa1',2,'p_programa1','miniProyectoPt4.py',209),
  ('programa1 -> vars body END','programa1',3,'p_programa1','miniProyectoPt4.py',210),
  ('vars -> VAR ID vars1','vars',3,'p_vars','miniProyectoPt4.py',216),
  ('vars1 -> COMMA ID vars1','vars1',3,'p_vars1','miniProyectoPt4.py',224),
  ('vars1 -> COLON type','vars1',2,'p_vars1','miniProyectoPt4.py',225),
  ('vars2 -> ID vars1','vars2',2,'p_vars2','miniProyectoPt4.py',232),
  ('vars3 -> vars2','vars3',1,'p_vars3','miniProyectoPt4.py',239),
  ('vars3 -> <empty>','vars3',0,'p_vars3','miniProyectoPt4.py',240),
  ('type -> INT EOL vars3','type',3,'p_type','miniProyectoPt4.py',245),
  ('type -> FLOAT EOL vars3','type',3,'p_type','miniProyectoPt4.py',246),
  ('body -> LBRACKET body1 RBRACKET','body',3,'p_body','miniProyectoPt4.py',252),
  ('body1 -> statement body1','body1',2,'p_body1','miniProyectoPt4.py',257),
  ('body1 -> <empty>','body1',0,'p_body1','miniProyectoPt4.py',258),
  ('statement -> assign','statement',1,'p_statement','miniProyectoPt4.py',264),
  ('statement -> condition','statement',1,'p_statement','miniProyectoPt4.py',265),
  ('statement -> cycle','statement',1,'p_statement','miniProyectoPt4.py',266),
  ('statement -> print','statement',1,'p_statement','miniProyectoPt4.py',267),
  ('print -> COUT LPAREN print1','print',3,'p_print','miniProyectoPt4.py',272),
  ('print1 -> expression_print print2','print1',2,'p_print1','miniProyectoPt4.py',278),
  ('print1 -> CTE_STRING print2','print1',2,'p_print1','miniProyectoPt4.py',279),
  ('print2 -> COMMA print1','print2',2,'p_print2','miniProyectoPt4.py',285),
  ('print2 -> RPAREN EOL','print2',2,'p_print2','miniProyectoPt4.py',286),
  ('expression_print -> expression','expression_print',1,'p_expression_print','miniProyectoPt4.py',292),
  ('assign -> ID EQUAL expression EOL','assign',4,'p_assign','miniProyectoPt4.py',299),
  ('expression -> exp expression1','expression',2,'p_expression','miniProyectoPt4.py',307),
  ('expression1 -> GREATER exp','expression1',2,'p_expression1','miniProyectoPt4.py',312),
  ('expression1 -> LESS exp','expression1',2,'p_expression1','miniProyectoPt4.py',313),
  ('expression1 -> NOTEQUAL exp','expression1',2,'p_expression1','miniProyectoPt4.py',314),
  ('expression1 -> <empty>','expression1',0,'p_expression1','miniProyectoPt4.py',315),
  ('cycle -> do_helper body WHILE LPAREN expression RPAREN EOL','cycle',7,'p_cycle','miniProyectoPt4.py',323),
  ('do_helper -> DO','do_helper',1,'p_do_helper','miniProyectoPt4.py',330),
  ('condition -> IF LPAREN expression_condition RPAREN body condition1','condition',6,'p_condition','miniProyectoPt4.py',337),
  ('expression_condition -> expression','expression_condition',1,'p_expression_condition','miniProyectoPt4.py',345),
  ('condition1 -> else_helper body EOL','condition1',3,'p_condition1','miniProyectoPt4.py',353),
  ('condition1 -> EOL','condition1',1,'p_condition1','miniProyectoPt4.py',354),
  ('else_helper -> ELSE','else_helper',1,'p_else_helper','miniProyectoPt4.py',360),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','miniProyectoPt4.py',369),
  ('factor -> PLUS factor1','factor',2,'p_factor','miniProyectoPt4.py',370),
  ('factor -> MINUS factor1','factor',2,'p_factor','miniProyectoPt4.py',371),
  ('factor -> factor1','factor',1,'p_factor','miniProyectoPt4.py',372),
  ('factor1 -> ID','factor1',1,'p_factor1','miniProyectoPt4.py',380),
  ('factor1 -> cte','factor1',1,'p_factor1','miniProyectoPt4.py',381),
  ('exp -> exp1','exp',1,'p_exp','miniProyectoPt4.py',389),
  ('exp1 -> term PLUS exp1','exp1',3,'p_exp1','miniProyectoPt4.py',394),
  ('exp1 -> term MINUS exp1','exp1',3,'p_exp1','miniProyectoPt4.py',395),
  ('exp1 -> term','exp1',1,'p_exp1','miniProyectoPt4.py',396),
  ('term -> term1','term',1,'p_term','miniProyectoPt4.py',404),
  ('term1 -> factor MULTIPLY term1','term1',3,'p_term1','miniProyectoPt4.py',409),
  ('term1 -> factor DIVIDE term1','term1',3,'p_term1','miniProyectoPt4.py',410),
  ('term1 -> factor','term1',1,'p_term1','miniProyectoPt4.py',411),
  ('cte -> CTE_INT','cte',1,'p_cte','miniProyectoPt4.py',419),
  ('cte -> CTE_FLOAT','cte',1,'p_cte','miniProyectoPt4.py',420),
]
