import os

PROJECT_NAME = 'eccomp2022'
_root_path = ''

def _calc_root_path():
  global _root_path
  current_dir = os.path.abspath(os.curdir)
  pos = current_dir.find(PROJECT_NAME) + len(PROJECT_NAME) + 1
  _root_path = current_dir[:pos]
_calc_root_path()

def get_root_path():
  return _root_path
