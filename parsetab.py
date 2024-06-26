
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CONVERT FORMAT INPATH INTEGER OUTPATH RESIZE ROTATEstatement : RESIZE INPATH OUTPATH INTEGER INTEGERstatement : CONVERT INPATH OUTPATH FORMATstatement : ROTATE INPATH OUTPATH INTEGER'
    
_lr_action_items = {'RESIZE':([0,],[2,]),'CONVERT':([0,],[3,]),'ROTATE':([0,],[4,]),'$end':([1,12,13,14,],[0,-2,-3,-1,]),'INPATH':([2,3,4,],[5,6,7,]),'OUTPATH':([5,6,7,],[8,9,10,]),'INTEGER':([8,10,11,],[11,13,14,]),'FORMAT':([9,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> RESIZE INPATH OUTPATH INTEGER INTEGER','statement',5,'p_statement_resize','image_tools.py',52),
  ('statement -> CONVERT INPATH OUTPATH FORMAT','statement',4,'p_statement_convert','image_tools.py',57),
  ('statement -> ROTATE INPATH OUTPATH INTEGER','statement',4,'p_statement_rotate','image_tools.py',62),
]
