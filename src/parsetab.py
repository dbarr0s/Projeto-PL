
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AT BEGIN COLON DIVIDE DO DOT DROP DUP ELSE EQUAL EXCLAMATION EXIT GREATER_THAN IF LEFT_PAREN LESS_THAN LOOP MINUS MOD NUMBER OVER PLUS POWER REPEAT RIGHT_PAREN ROT SEMICOLON STRING SWAP THEN TIMES VARIABLE WHILEprogram : statementsstatements : statement\n                  | statements statementstatement : expression\n                 | flow_controlexpression : NUMBER\n                  | STRING\n                  | VARIABLE\n                  | special_expressionexpression : expression arithmetic_op expressionarithmetic_op : PLUS\n                     | MINUS\n                     | TIMES\n                     | DIVIDE\n                     | MOD\n                     | POWERexpression : expression relational_op expressionrelational_op : EQUAL\n                      | LESS_THAN\n                      | GREATER_THANspecial_expression : EXCLAMATION\n                           | AT\n                           | DOT\n                           | COLON\n                           | SEMICOLON\n                           | LEFT_PAREN\n                           | RIGHT_PARENflow_control : if_statement\n                    | else_statement\n                    | while_loop\n                    | repeat_loop\n                    | exit_statement\n                    | drop_statement\n                    | dup_statement\n                    | swap_statement\n                    | rot_statement\n                    | over_statementif_statement : IF expression THENelse_statement : ELSEwhile_loop : WHILE expression DO statements LOOPrepeat_loop : BEGIN statements WHILE expression REPEATexit_statement : EXITdrop_statement : DROPdup_statement : DUPswap_statement : SWAProt_statement : ROTover_statement : OVER'
    
_lr_action_items = {'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[6,6,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,6,-39,6,6,-42,-43,-44,-45,-46,-47,-3,6,6,-11,-12,-13,-14,-15,-16,-18,-19,-20,6,-10,-17,-38,6,6,6,-40,-41,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[7,7,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,7,-39,7,7,-42,-43,-44,-45,-46,-47,-3,7,7,-11,-12,-13,-14,-15,-16,-18,-19,-20,7,-10,-17,-38,7,7,7,-40,-41,]),'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[8,8,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,8,-39,8,8,-42,-43,-44,-45,-46,-47,-3,8,8,-11,-12,-13,-14,-15,-16,-18,-19,-20,8,-10,-17,-38,8,8,8,-40,-41,]),'EXCLAMATION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[20,20,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,20,-39,20,20,-42,-43,-44,-45,-46,-47,-3,20,20,-11,-12,-13,-14,-15,-16,-18,-19,-20,20,-10,-17,-38,20,20,20,-40,-41,]),'AT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[21,21,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,21,-39,21,21,-42,-43,-44,-45,-46,-47,-3,21,21,-11,-12,-13,-14,-15,-16,-18,-19,-20,21,-10,-17,-38,21,21,21,-40,-41,]),'DOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[22,22,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,22,-39,22,22,-42,-43,-44,-45,-46,-47,-3,22,22,-11,-12,-13,-14,-15,-16,-18,-19,-20,22,-10,-17,-38,22,22,22,-40,-41,]),'COLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[23,23,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,23,-39,23,23,-42,-43,-44,-45,-46,-47,-3,23,23,-11,-12,-13,-14,-15,-16,-18,-19,-20,23,-10,-17,-38,23,23,23,-40,-41,]),'SEMICOLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[24,24,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,24,-39,24,24,-42,-43,-44,-45,-46,-47,-3,24,24,-11,-12,-13,-14,-15,-16,-18,-19,-20,24,-10,-17,-38,24,24,24,-40,-41,]),'LEFT_PAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[25,25,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,25,-39,25,25,-42,-43,-44,-45,-46,-47,-3,25,25,-11,-12,-13,-14,-15,-16,-18,-19,-20,25,-10,-17,-38,25,25,25,-40,-41,]),'RIGHT_PAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,59,60,],[26,26,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,26,-39,26,26,-42,-43,-44,-45,-46,-47,-3,26,26,-11,-12,-13,-14,-15,-16,-18,-19,-20,26,-10,-17,-38,26,26,26,-40,-41,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[27,27,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,27,-42,-43,-44,-45,-46,-47,-3,27,-10,-17,-38,27,27,-40,-41,]),'ELSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[28,28,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,28,-42,-43,-44,-45,-46,-47,-3,28,-10,-17,-38,28,28,-40,-41,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[29,29,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,29,-42,-43,-44,-45,-46,-47,-3,56,-10,-17,-38,29,29,-40,-41,]),'BEGIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[30,30,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,30,-42,-43,-44,-45,-46,-47,-3,30,-10,-17,-38,30,30,-40,-41,]),'EXIT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[31,31,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,31,-42,-43,-44,-45,-46,-47,-3,31,-10,-17,-38,31,31,-40,-41,]),'DROP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[32,32,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,32,-42,-43,-44,-45,-46,-47,-3,32,-10,-17,-38,32,32,-40,-41,]),'DUP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[33,33,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,33,-42,-43,-44,-45,-46,-47,-3,33,-10,-17,-38,33,33,-40,-41,]),'SWAP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[34,34,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,34,-42,-43,-44,-45,-46,-47,-3,34,-10,-17,-38,34,34,-40,-41,]),'ROT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[35,35,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,35,-42,-43,-44,-45,-46,-47,-3,35,-10,-17,-38,35,35,-40,-41,]),'OVER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,31,32,33,34,35,36,37,51,52,53,54,55,57,59,60,],[36,36,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,36,-42,-43,-44,-45,-46,-47,-3,36,-10,-17,-38,36,36,-40,-41,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,31,32,33,34,35,36,37,52,53,54,59,60,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,-42,-43,-44,-45,-46,-47,-3,-10,-17,-38,-40,-41,]),'LOOP':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,31,32,33,34,35,36,37,52,53,54,57,59,60,],[-2,-4,-5,-6,-7,-8,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-21,-22,-23,-24,-25,-26,-27,-39,-42,-43,-44,-45,-46,-47,-3,-10,-17,-38,59,-40,-41,]),'PLUS':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[40,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,40,40,40,40,40,]),'MINUS':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[41,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,41,41,41,41,41,]),'TIMES':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[42,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,42,42,42,42,42,]),'DIVIDE':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[43,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,43,43,43,43,43,]),'MOD':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[44,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,44,44,44,44,44,]),'POWER':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[45,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,45,45,45,45,45,]),'EQUAL':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[46,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,46,46,46,46,46,]),'LESS_THAN':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[47,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,47,47,47,47,47,]),'GREATER_THAN':([4,6,7,8,9,20,21,22,23,24,25,26,49,50,52,53,58,],[48,-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,48,48,48,48,48,]),'THEN':([6,7,8,9,20,21,22,23,24,25,26,49,52,53,],[-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,54,-10,-17,]),'DO':([6,7,8,9,20,21,22,23,24,25,26,50,52,53,58,],[-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,55,-10,-17,55,]),'REPEAT':([6,7,8,9,20,21,22,23,24,25,26,52,53,58,],[-6,-7,-8,-9,-21,-22,-23,-24,-25,-26,-27,-10,-17,60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,30,55,],[2,51,57,]),'statement':([0,2,30,51,55,57,],[3,37,3,37,3,37,]),'expression':([0,2,27,29,30,38,39,51,55,56,57,],[4,4,49,50,4,52,53,4,4,58,4,]),'flow_control':([0,2,30,51,55,57,],[5,5,5,5,5,5,]),'special_expression':([0,2,27,29,30,38,39,51,55,56,57,],[9,9,9,9,9,9,9,9,9,9,9,]),'if_statement':([0,2,30,51,55,57,],[10,10,10,10,10,10,]),'else_statement':([0,2,30,51,55,57,],[11,11,11,11,11,11,]),'while_loop':([0,2,30,51,55,57,],[12,12,12,12,12,12,]),'repeat_loop':([0,2,30,51,55,57,],[13,13,13,13,13,13,]),'exit_statement':([0,2,30,51,55,57,],[14,14,14,14,14,14,]),'drop_statement':([0,2,30,51,55,57,],[15,15,15,15,15,15,]),'dup_statement':([0,2,30,51,55,57,],[16,16,16,16,16,16,]),'swap_statement':([0,2,30,51,55,57,],[17,17,17,17,17,17,]),'rot_statement':([0,2,30,51,55,57,],[18,18,18,18,18,18,]),'over_statement':([0,2,30,51,55,57,],[19,19,19,19,19,19,]),'arithmetic_op':([4,49,50,52,53,58,],[38,38,38,38,38,38,]),'relational_op':([4,49,50,52,53,58,],[39,39,39,39,39,39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','forthYacc.py',9),
  ('statements -> statement','statements',1,'p_statements','forthYacc.py',13),
  ('statements -> statements statement','statements',2,'p_statements','forthYacc.py',14),
  ('statement -> expression','statement',1,'p_statement','forthYacc.py',22),
  ('statement -> flow_control','statement',1,'p_statement','forthYacc.py',23),
  ('expression -> NUMBER','expression',1,'p_expression','forthYacc.py',27),
  ('expression -> STRING','expression',1,'p_expression','forthYacc.py',28),
  ('expression -> VARIABLE','expression',1,'p_expression','forthYacc.py',29),
  ('expression -> special_expression','expression',1,'p_expression','forthYacc.py',30),
  ('expression -> expression arithmetic_op expression','expression',3,'p_expression_arithmetic','forthYacc.py',34),
  ('arithmetic_op -> PLUS','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',53),
  ('arithmetic_op -> MINUS','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',54),
  ('arithmetic_op -> TIMES','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',55),
  ('arithmetic_op -> DIVIDE','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',56),
  ('arithmetic_op -> MOD','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',57),
  ('arithmetic_op -> POWER','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',58),
  ('expression -> expression relational_op expression','expression',3,'p_expression_relational','forthYacc.py',62),
  ('relational_op -> EQUAL','relational_op',1,'p_relational_op','forthYacc.py',74),
  ('relational_op -> LESS_THAN','relational_op',1,'p_relational_op','forthYacc.py',75),
  ('relational_op -> GREATER_THAN','relational_op',1,'p_relational_op','forthYacc.py',76),
  ('special_expression -> EXCLAMATION','special_expression',1,'p_special_expression','forthYacc.py',80),
  ('special_expression -> AT','special_expression',1,'p_special_expression','forthYacc.py',81),
  ('special_expression -> DOT','special_expression',1,'p_special_expression','forthYacc.py',82),
  ('special_expression -> COLON','special_expression',1,'p_special_expression','forthYacc.py',83),
  ('special_expression -> SEMICOLON','special_expression',1,'p_special_expression','forthYacc.py',84),
  ('special_expression -> LEFT_PAREN','special_expression',1,'p_special_expression','forthYacc.py',85),
  ('special_expression -> RIGHT_PAREN','special_expression',1,'p_special_expression','forthYacc.py',86),
  ('flow_control -> if_statement','flow_control',1,'p_flow_control','forthYacc.py',90),
  ('flow_control -> else_statement','flow_control',1,'p_flow_control','forthYacc.py',91),
  ('flow_control -> while_loop','flow_control',1,'p_flow_control','forthYacc.py',92),
  ('flow_control -> repeat_loop','flow_control',1,'p_flow_control','forthYacc.py',93),
  ('flow_control -> exit_statement','flow_control',1,'p_flow_control','forthYacc.py',94),
  ('flow_control -> drop_statement','flow_control',1,'p_flow_control','forthYacc.py',95),
  ('flow_control -> dup_statement','flow_control',1,'p_flow_control','forthYacc.py',96),
  ('flow_control -> swap_statement','flow_control',1,'p_flow_control','forthYacc.py',97),
  ('flow_control -> rot_statement','flow_control',1,'p_flow_control','forthYacc.py',98),
  ('flow_control -> over_statement','flow_control',1,'p_flow_control','forthYacc.py',99),
  ('if_statement -> IF expression THEN','if_statement',3,'p_if_statement','forthYacc.py',103),
  ('else_statement -> ELSE','else_statement',1,'p_else_statement','forthYacc.py',107),
  ('while_loop -> WHILE expression DO statements LOOP','while_loop',5,'p_while_loop','forthYacc.py',111),
  ('repeat_loop -> BEGIN statements WHILE expression REPEAT','repeat_loop',5,'p_repeat_loop','forthYacc.py',115),
  ('exit_statement -> EXIT','exit_statement',1,'p_exit_statement','forthYacc.py',119),
  ('drop_statement -> DROP','drop_statement',1,'p_drop_statement','forthYacc.py',123),
  ('dup_statement -> DUP','dup_statement',1,'p_dup_statement','forthYacc.py',127),
  ('swap_statement -> SWAP','swap_statement',1,'p_swap_statement','forthYacc.py',131),
  ('rot_statement -> ROT','rot_statement',1,'p_rot_statement','forthYacc.py',135),
  ('over_statement -> OVER','over_statement',1,'p_over_statement','forthYacc.py',139),
]