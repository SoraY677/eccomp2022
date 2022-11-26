import random
import copy
import sys

import resolver
import config
import logger
import submit
import store
import constraint
import mock_server

def run(
    mode : str,
    optimize_mode: str,
    optimize_number: str,
    store_map: map,
    is_practice: bool
  ) -> None:
  '''
  実行
  '''
  config_map = config.get_config()[optimize_mode][mode][optimize_number]
  logger.log_info(f'{config_map}')

  time_max = config_map['time_max']
  unit_minute_min = config_map['unit_minute_min']
  unit_minute_max = config_map['unit_minute_max']
  agent_sum = config_map['agent_sum']
  solution_list_max = config_map['solution_list_max']
  submit_max = config_map['submit_max']
  endpoint = ''
  try:
    endpoint = config_map['endpoint'] 
  except:
    pass

  if is_practice:
    mock_server.init(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum
    )

  if config_map['is_type_categorize']:
    categorized_exec(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum,
      config_map['type_guided_sum'],
      config_map['type_busy_sum'],
      config_map['type_slow_sum'],
      solution_list_max,
      submit_max,
      store_map,
      endpoint,
      is_practice
    )

  else:
    not_categorized_exec(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum,
      solution_list_max,
      submit_max,
      store_map,
      endpoint,
      is_practice
    )


def categorized_exec(
      time_max:int,
      unit_minute_min:int,
      unit_minute_max:int,
      agent_sum:int,
      type_guided_sum:int,
      type_busy_sum:int,
      type_slow_sum:int,
      solution_list_max: int,
      submit_max: int,
      store_map: map,
      endpoint: str,
      is_practice: bool
    ) -> None:
  '''
  カテゴリ分けアリの実行
  '''

  pass

def not_categorized_exec(
      time_max: int,
      unit_minute_min: int,
      unit_minute_max: int,
      agent_sum: int,
      solution_list_max: int,
      submit_max: int,
      store_map: map,
      endpoint: str,
      is_practice: bool
    ) -> None:
  '''
  カテゴリ分けナシの実行
  '''
  # ストアからデータを取得 or 初期化
  solution_list = \
    [resolver.first_generate(time_max, unit_minute_min, unit_minute_max, agent_sum) for _ in range(solution_list_max)] if store_map is None \
    else store_map['solution_list'] 
  new_solution_list = copy.copy(solution_list)
  loop_start = 0 if store_map is None else store_map['count_index']
  score_list = [ sys.maxsize ] * solution_list_max if store_map is None else store_map['score_list']
  graph_path_list = [''] * solution_list_max
    
  LOOP_MAX = int(submit_max / solution_list_max)
  logger.log_debug(f'loop  : {loop_start} to {LOOP_MAX}')
  for i in range(loop_start, LOOP_MAX):
    count = i + 1
    logger.log_info(f'+++++calculation {count} +++++')
    best_solution_map_list = [{
        'score': score_list[i],
        'solution': solution_list[i]
      } for i in range(solution_list_max)]
    for solution_i in range(len(solution_list)):
      solution = new_solution_list[solution_i]
      score = submit.run(solution, endpoint, is_practice, graph_path_list[solution_i])
      best_solution_map_list.append({
        'score': score,
        'solution': solution
      })
    score_solution_map_list_sorted = sorted(best_solution_map_list ,key=lambda x:x['score'])
    solution_list = [ score_solution_map_list_sorted[i]['solution'] for i in range(solution_list_max)]
    score_list    = [ score_solution_map_list_sorted[i]['score'] for i in range(solution_list_max)]

    logger.log_debug(f'[score list]: {score_list}')
    graph_path_list = []

    # 記録
    store.save(i, solution_list, score_list)

    new_solution_list = []
    score_list_sum = sum(score_list)
    for _ in range(solution_list_max):
      select_i1, select_i2 = resolver.select(score_list, score_list_sum)
      selected_solution1 = solution_list[select_i1]
      selected_solution2 = solution_list[select_i2]
      # 突然変異
      if random.random() < 0.2:
        solution = resolver.mutate(selected_solution1, unit_minute_min, unit_minute_max, agent_sum)
        graph_path_list.append('')
        new_solution_list.append(solution)
        continue
      # 合成
      if random.random() < 0.5:
        solution, graph_path = resolver.union(selected_solution1, selected_solution2, unit_minute_min, unit_minute_max, agent_sum)
        graph_path_list.append(graph_path)
        new_solution_list.append(solution)
        continue
      # 交叉
      else:
        solution, graph_path = resolver.cross(selected_solution1, selected_solution2, 2, unit_minute_min, unit_minute_max, agent_sum)
        graph_path_list.append(graph_path)
        new_solution_list.append(solution)
        continue
    solution_list = copy.copy(new_solution_list)
    logger.log_info(f'calculation {count} result:{min(score_list)}')

  return graph_path
