import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import random
import copy

if __name__ == '__main__':
  sys.path.append(os.path.abspath('../..'))
else:
  from dotenv import load_dotenv
  load_dotenv()
  PROJECT_NAME = os.getenv('PROJECT_NAME')
  current_dir = os.path.abspath(os.curdir)
  project_dir = current_dir[:current_dir.find("{PROJECT_NAME}")+len("{PROJECT_NAME}")]
  sys.path.append(os.path.join(project_dir, 'src'))
import logger


import resolver_config as conf
from resolver_config import set_config
from initialize import run as init_generate
from crossover import run as cross
from union import run as union
from selecter import select
from mutation import mutate
import store

__all__ = [
  'exec',
]

_store_map = None

def _setup(
    id,
    config_map,
    is_clear
  ):
  global _store_map
  _store_map = store.init(id, is_clear)
  set_config(config_map)

def _init():
  init_generated_list = [init_generate() for _ in range(conf.individual_num)] \
    if _store_map is None \
    else [[_store_map['solution_list'][i], _store_map['graph_path_list'][i]] for i in range(conf.individual_num) ]
  solution_list = [item[0] for item in init_generated_list]
  graph_path_list = [item[1] for item in init_generated_list]
  score_list = [ sys.maxsize ] * conf.individual_num if _store_map is None else _store_map['score_list']
  loop_start = 1 if _store_map is None else _store_map['count_index']
  return solution_list, graph_path_list, score_list, loop_start

def exec(
  config_map,
  id,
  is_clear,
  is_practice,
  optimize_function
):
  '''
  一連の実行
  '''
  _setup(id, config_map, is_clear)
  solution_list, graph_path_list, score_list, loop_start = _init()
  best_solution_map_list = [{
    'score': score_list[i],
    'solution': solution_list[i],
    'graph': graph_path_list[i]
  } for i in range(conf.individual_num)]

  for count in range(loop_start, conf.evolve_max + 1):
    logger.log_info(f'+++++ calculation {count} +++++')

    score_list = optimize_function(solution_list, conf.match_number, is_practice)

    for solution_i in range(len(solution_list)):
      solution = solution_list[solution_i]
      score = score_list[solution_i]
      graph_path = graph_path_list[solution_i]
      best_solution_map_list.append({
        'score': score,
        'solution': solution,
        'graph_path': graph_path
      })
    score_solution_map_list_sorted = sorted(best_solution_map_list, key=lambda x: x['score'])
    solution_list = [ score_solution_map_list_sorted[i]['solution'] for i in range(conf.individual_num)]
    score_list    = [ score_solution_map_list_sorted[i]['score'] for i in range(conf.individual_num)]
    graph_path_list = [ score_solution_map_list_sorted[i]['graph_path'] for i in range(conf.individual_num) ]

    for i in range(len(solution_list)):
      logger.log_info(f'{i}:')
      logger.log_debug(f'{solution_list[i]}')
      logger.log_info(f'{score_list[i]}')
      logger.log_info(f'{graph_path_list[i]}')
    store.save(count, solution_list, score_list, graph_path_list)

    new_solution_list = []
    graph_path_list = []
    for _ in range(conf.individual_num):
      select_i1, select_i2 = select(score_list)
      selected_solution1 = solution_list[select_i1]
      selected_solution2 = solution_list[select_i2]
      # 突然変異
      if random.random() < 0.1:
        logger.log_info(f'[mutate] {select_i1}')
        solution, graph_path = mutate(selected_solution1)
        graph_path_list.append(graph_path)
        new_solution_list.append(solution)
        continue
      # 合成
      if random.random() < 0.5:
        logger.log_info(f'[union] {select_i1}:{select_i2}')
        solution, graph_path = union(selected_solution1, selected_solution2)
        graph_path_list.append(graph_path)
        new_solution_list.append(solution)
        continue
      # 交叉
      else:
        logger.log_info(f'[cross] {select_i1}:{select_i2}')
        solution, graph_path = cross(selected_solution1, selected_solution2, 2)
        graph_path_list.append(graph_path)
        new_solution_list.append(solution)
        continue
    solution_list = copy.copy(new_solution_list)
    logger.log_info(f'calculation {count} result:{min(score_list)}')
