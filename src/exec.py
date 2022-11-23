import random
import copy

import resolver
import config
import logger
import submit

def run(
    mode : str,
    optimize_mode: str,
    optimize_number: str
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
      submit_max
    )

  else:
    not_categorized_exec(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum,
      solution_list_max,
      submit_max
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
      submit_max: int
    ) -> None:
  '''
  カテゴリ分けナシの実行
  '''
  solution_list = [resolver.first_generate(time_max, unit_minute_min, unit_minute_max, agent_sum) for _ in range(solution_list_max)]
  LOOP_MAX = int(submit_max / solution_list_max)
  logger.log_info(f'loop max : {LOOP_MAX}')
  for i in range(LOOP_MAX):
    count = i + 1
    logger.log_info(f'+++++calculation {count} +++++')
    score_list = []
    for solution in solution_list:
      score = submit.run(solution)
      score_list.append(score)
    logger.log_info(f'[score list]: {score_list}')

    new_solution_list = []
    score_list_sum = sum(score_list)
    for _ in range(solution_list_max):
      select_i1, select_i2 = resolver.select(score_list, score_list_sum)
      selected_solution1 = solution_list[select_i1]
      selected_solution2 = solution_list[select_i2]
      # 突然変異
      if random.random() < 0.15:
        solution = resolver.mutate(time_max, unit_minute_min, unit_minute_max, agent_sum)
        new_solution_list.append(solution)
        continue
      # 合成 = 選ばれた解が同じなら
      if select_i1 == select_i2:
        solution = resolver.union(selected_solution1, selected_solution2, unit_minute_min, unit_minute_max, agent_sum)
        new_solution_list.append(solution)
        continue
      # 交叉 = 選ばれた解が異なる
      else:
        solution = resolver.cross(selected_solution1, selected_solution2, 2, unit_minute_min, unit_minute_max, agent_sum)
        new_solution_list.append(solution)
        continue

    solution_list = copy.copy(new_solution_list)
    logger.log_info(f'calculation {count} result:{min(score_list)}')





