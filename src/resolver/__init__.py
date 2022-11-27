import os
import sys
import copy
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import resolver_config as conf
from resolver_config import set_config
from generate import random_generate as first_generate
from crossover import run as cross
from union import run as union
from selecter import select
from mutation import mutate
import store

__all__ = [
  'exec',
]

def _setup(
    config_map,
    is_clear
  ):
  # graph_plotter.init(id, is_clear)
  store_map = store.init(id, is_clear)
  set_config(config_map)

def _init(
    store_map
  ):
  solution_list = \
    [first_generate() for _ in range(conf.individual_num)] if store_map is None \
    else store_map['solution_list'] 
  loop_start = 0 if store_map is None else store_map['count_index']
  score_list = [ sys.maxsize ] * conf.individual_num if store_map is None else store_map['score_list']


  new_solution_list = copy.copy(solution_list)

def exec(
  config_map,
  id,
  is_clear,
  optimize_function
):
  '''
  一連の実行
  '''
  _setup(config_map, is_clear)
  _init()
  for i in range(conf.evolve_max):
    pass
