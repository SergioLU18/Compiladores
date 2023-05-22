
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA COUT CTE_FLOAT CTE_INT CTE_STRING DIVIDE DO ELSE END EOL EQUAL FLOAT GREATER ID IF INT LBRACKET LESS LPAREN MINUS MULTIPLY NOTEQUAL PLUS PROGRAM RBRACKET RPAREN VAR WHILE\n    programa : PROGRAM ID EOL programa1\n    \n    programa1 : body END\n                | vars body END\n    \n    vars : VAR ID vars1\n    \n    vars1 : COMMA ID vars1\n            | COLON type EOL vars3\n    \n    vars2 : ID vars1\n    \n    vars3 : vars2\n        |\n    \n    type : INT\n        | FLOAT\n    \n    body : LBRACKET body1 RBRACKET\n    \n    body1 : statement body1\n        |\n    \n    statement : assign\n                | condition\n                | cycle\n                | print\n    \n    print : COUT LPAREN print1\n    \n    print1 : expression print2\n        | CTE_STRING print2\n    \n    print2 : COMMA print1\n        | RPAREN EOL\n    \n    assign : ID EQUAL expression EOL\n    \n    expression : exp expression1\n    \n    expression1 : GREATER exp\n                | LESS exp\n                | NOTEQUAL exp\n                |\n    \n    cycle : DO body WHILE LPAREN expression RPAREN EOL\n    \n    condition : IF LPAREN expression RPAREN body condition1\n    \n    condition1 : ELSE body EOL\n                | EOL\n    \n    factor : LPAREN expression RPAREN\n            | PLUS factor1\n            | MINUS factor1\n            | factor1\n    \n    factor1 : ID\n            | cte\n    \n    exp : exp1\n    \n    exp1 : term PLUS exp1\n        | term MINUS exp1\n        | term\n    \n    term : term1\n    \n    term1 : factor MULTIPLY term1\n        | factor DIVIDE term1\n        | factor\n    \n    cte : CTE_INT\n        | CTE_FLOAT\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,10,23,],[0,-1,-2,-3,]),'ID':([2,8,9,13,14,15,16,17,26,27,29,31,38,39,42,49,56,58,59,60,61,62,65,66,69,70,71,73,75,86,87,91,93,97,98,],[3,18,22,18,-15,-16,-17,-18,33,33,33,52,33,33,33,-19,-24,33,33,33,33,33,33,33,33,-20,33,-21,90,-22,-23,-31,-33,-30,-32,]),'EOL':([3,24,33,34,35,36,37,40,41,43,44,45,46,53,54,55,57,63,64,72,76,77,78,79,80,81,82,83,84,94,96,],[4,-12,-38,56,-29,-40,-43,-44,-47,-37,-39,-48,-49,75,-10,-11,-25,-35,-36,87,-26,-27,-28,-41,-42,-45,-46,-34,93,97,98,]),'LBRACKET':([4,7,20,30,68,74,75,88,89,92,95,],[8,8,8,-4,8,-5,-9,-6,-8,8,-7,]),'VAR':([4,],[9,]),'END':([6,11,24,],[10,23,-12,]),'RBRACKET':([8,12,13,14,15,16,17,25,49,56,70,73,86,87,91,93,97,98,],[-14,24,-14,-15,-16,-17,-18,-13,-19,-24,-20,-21,-22,-23,-31,-33,-30,-32,]),'IF':([8,13,14,15,16,17,49,56,70,73,86,87,91,93,97,98,],[19,19,-15,-16,-17,-18,-19,-24,-20,-21,-22,-23,-31,-33,-30,-32,]),'DO':([8,13,14,15,16,17,49,56,70,73,86,87,91,93,97,98,],[20,20,-15,-16,-17,-18,-19,-24,-20,-21,-22,-23,-31,-33,-30,-32,]),'COUT':([8,13,14,15,16,17,49,56,70,73,86,87,91,93,97,98,],[21,21,-15,-16,-17,-18,-19,-24,-20,-21,-22,-23,-31,-33,-30,-32,]),'EQUAL':([18,],[26,]),'LPAREN':([19,21,26,27,29,42,48,58,59,60,61,62,65,66,69,71,],[27,29,42,42,42,42,69,42,42,42,42,42,42,42,42,42,]),'COMMA':([22,33,35,36,37,40,41,43,44,45,46,50,51,52,57,63,64,76,77,78,79,80,81,82,83,90,],[31,-38,-29,-40,-43,-44,-47,-37,-39,-48,-49,71,71,31,-25,-35,-36,-26,-27,-28,-41,-42,-45,-46,-34,31,]),'COLON':([22,52,90,],[32,32,32,]),'WHILE':([24,28,],[-12,48,]),'ELSE':([24,84,],[-12,92,]),'PLUS':([26,27,29,33,37,40,41,42,43,44,45,46,58,59,60,61,62,63,64,65,66,69,71,81,82,83,],[38,38,38,-38,61,-44,-47,38,-37,-39,-48,-49,38,38,38,38,38,-35,-36,38,38,38,38,-45,-46,-34,]),'MINUS':([26,27,29,33,37,40,41,42,43,44,45,46,58,59,60,61,62,63,64,65,66,69,71,81,82,83,],[39,39,39,-38,62,-44,-47,39,-37,-39,-48,-49,39,39,39,39,39,-35,-36,39,39,39,39,-45,-46,-34,]),'CTE_INT':([26,27,29,38,39,42,58,59,60,61,62,65,66,69,71,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'CTE_FLOAT':([26,27,29,38,39,42,58,59,60,61,62,65,66,69,71,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'CTE_STRING':([29,71,],[51,51,]),'INT':([32,],[54,]),'FLOAT':([32,],[55,]),'MULTIPLY':([33,41,43,44,45,46,63,64,83,],[-38,65,-37,-39,-48,-49,-35,-36,-34,]),'DIVIDE':([33,41,43,44,45,46,63,64,83,],[-38,66,-37,-39,-48,-49,-35,-36,-34,]),'GREATER':([33,35,36,37,40,41,43,44,45,46,63,64,79,80,81,82,83,],[-38,58,-40,-43,-44,-47,-37,-39,-48,-49,-35,-36,-41,-42,-45,-46,-34,]),'LESS':([33,35,36,37,40,41,43,44,45,46,63,64,79,80,81,82,83,],[-38,59,-40,-43,-44,-47,-37,-39,-48,-49,-35,-36,-41,-42,-45,-46,-34,]),'NOTEQUAL':([33,35,36,37,40,41,43,44,45,46,63,64,79,80,81,82,83,],[-38,60,-40,-43,-44,-47,-37,-39,-48,-49,-35,-36,-41,-42,-45,-46,-34,]),'RPAREN':([33,35,36,37,40,41,43,44,45,46,47,50,51,57,63,64,67,76,77,78,79,80,81,82,83,85,],[-38,-29,-40,-43,-44,-47,-37,-39,-48,-49,68,72,72,-25,-35,-36,83,-26,-27,-28,-41,-42,-45,-46,-34,94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'programa1':([4,],[5,]),'body':([4,7,20,68,92,],[6,11,28,84,96,]),'vars':([4,],[7,]),'body1':([8,13,],[12,25,]),'statement':([8,13,],[13,13,]),'assign':([8,13,],[14,14,]),'condition':([8,13,],[15,15,]),'cycle':([8,13,],[16,16,]),'print':([8,13,],[17,17,]),'vars1':([22,52,90,],[30,74,95,]),'expression':([26,27,29,42,69,71,],[34,47,50,67,85,50,]),'exp':([26,27,29,42,58,59,60,69,71,],[35,35,35,35,76,77,78,35,35,]),'exp1':([26,27,29,42,58,59,60,61,62,69,71,],[36,36,36,36,36,36,36,79,80,36,36,]),'term':([26,27,29,42,58,59,60,61,62,69,71,],[37,37,37,37,37,37,37,37,37,37,37,]),'term1':([26,27,29,42,58,59,60,61,62,65,66,69,71,],[40,40,40,40,40,40,40,40,40,81,82,40,40,]),'factor':([26,27,29,42,58,59,60,61,62,65,66,69,71,],[41,41,41,41,41,41,41,41,41,41,41,41,41,]),'factor1':([26,27,29,38,39,42,58,59,60,61,62,65,66,69,71,],[43,43,43,63,64,43,43,43,43,43,43,43,43,43,43,]),'cte':([26,27,29,38,39,42,58,59,60,61,62,65,66,69,71,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'print1':([29,71,],[49,86,]),'type':([32,],[53,]),'expression1':([35,],[57,]),'print2':([50,51,],[70,73,]),'vars3':([75,],[88,]),'vars2':([75,],[89,]),'condition1':([84,],[91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID EOL programa1','programa',4,'p_programa','miniProyectoPt1.py',88),
  ('programa1 -> body END','programa1',2,'p_programa1','miniProyectoPt1.py',94),
  ('programa1 -> vars body END','programa1',3,'p_programa1','miniProyectoPt1.py',95),
  ('vars -> VAR ID vars1','vars',3,'p_vars','miniProyectoPt1.py',100),
  ('vars1 -> COMMA ID vars1','vars1',3,'p_vars1','miniProyectoPt1.py',105),
  ('vars1 -> COLON type EOL vars3','vars1',4,'p_vars1','miniProyectoPt1.py',106),
  ('vars2 -> ID vars1','vars2',2,'p_vars2','miniProyectoPt1.py',111),
  ('vars3 -> vars2','vars3',1,'p_vars3','miniProyectoPt1.py',116),
  ('vars3 -> <empty>','vars3',0,'p_vars3','miniProyectoPt1.py',117),
  ('type -> INT','type',1,'p_type','miniProyectoPt1.py',122),
  ('type -> FLOAT','type',1,'p_type','miniProyectoPt1.py',123),
  ('body -> LBRACKET body1 RBRACKET','body',3,'p_body','miniProyectoPt1.py',128),
  ('body1 -> statement body1','body1',2,'p_body1','miniProyectoPt1.py',134),
  ('body1 -> <empty>','body1',0,'p_body1','miniProyectoPt1.py',135),
  ('statement -> assign','statement',1,'p_statement','miniProyectoPt1.py',141),
  ('statement -> condition','statement',1,'p_statement','miniProyectoPt1.py',142),
  ('statement -> cycle','statement',1,'p_statement','miniProyectoPt1.py',143),
  ('statement -> print','statement',1,'p_statement','miniProyectoPt1.py',144),
  ('print -> COUT LPAREN print1','print',3,'p_print','miniProyectoPt1.py',149),
  ('print1 -> expression print2','print1',2,'p_print1','miniProyectoPt1.py',155),
  ('print1 -> CTE_STRING print2','print1',2,'p_print1','miniProyectoPt1.py',156),
  ('print2 -> COMMA print1','print2',2,'p_print2','miniProyectoPt1.py',162),
  ('print2 -> RPAREN EOL','print2',2,'p_print2','miniProyectoPt1.py',163),
  ('assign -> ID EQUAL expression EOL','assign',4,'p_assign','miniProyectoPt1.py',168),
  ('expression -> exp expression1','expression',2,'p_expression','miniProyectoPt1.py',173),
  ('expression1 -> GREATER exp','expression1',2,'p_expression1','miniProyectoPt1.py',178),
  ('expression1 -> LESS exp','expression1',2,'p_expression1','miniProyectoPt1.py',179),
  ('expression1 -> NOTEQUAL exp','expression1',2,'p_expression1','miniProyectoPt1.py',180),
  ('expression1 -> <empty>','expression1',0,'p_expression1','miniProyectoPt1.py',181),
  ('cycle -> DO body WHILE LPAREN expression RPAREN EOL','cycle',7,'p_cycle','miniProyectoPt1.py',186),
  ('condition -> IF LPAREN expression RPAREN body condition1','condition',6,'p_condition','miniProyectoPt1.py',191),
  ('condition1 -> ELSE body EOL','condition1',3,'p_condition1','miniProyectoPt1.py',196),
  ('condition1 -> EOL','condition1',1,'p_condition1','miniProyectoPt1.py',197),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','miniProyectoPt1.py',202),
  ('factor -> PLUS factor1','factor',2,'p_factor','miniProyectoPt1.py',203),
  ('factor -> MINUS factor1','factor',2,'p_factor','miniProyectoPt1.py',204),
  ('factor -> factor1','factor',1,'p_factor','miniProyectoPt1.py',205),
  ('factor1 -> ID','factor1',1,'p_factor1','miniProyectoPt1.py',210),
  ('factor1 -> cte','factor1',1,'p_factor1','miniProyectoPt1.py',211),
  ('exp -> exp1','exp',1,'p_exp','miniProyectoPt1.py',216),
  ('exp1 -> term PLUS exp1','exp1',3,'p_exp1','miniProyectoPt1.py',221),
  ('exp1 -> term MINUS exp1','exp1',3,'p_exp1','miniProyectoPt1.py',222),
  ('exp1 -> term','exp1',1,'p_exp1','miniProyectoPt1.py',223),
  ('term -> term1','term',1,'p_term','miniProyectoPt1.py',228),
  ('term1 -> factor MULTIPLY term1','term1',3,'p_term1','miniProyectoPt1.py',233),
  ('term1 -> factor DIVIDE term1','term1',3,'p_term1','miniProyectoPt1.py',234),
  ('term1 -> factor','term1',1,'p_term1','miniProyectoPt1.py',235),
  ('cte -> CTE_INT','cte',1,'p_cte','miniProyectoPt1.py',240),
  ('cte -> CTE_FLOAT','cte',1,'p_cte','miniProyectoPt1.py',241),
]
