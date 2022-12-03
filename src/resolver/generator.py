'''

解生成用関数
実際に提出用に条件付きで解が生成される部分

'''

import os
import sys
import random
import copy

import numpy as np
if __name__ == '__main__':
  sys.path.append(os.path.abspath('../..'))
else:
  from dotenv import load_dotenv
  load_dotenv()
  PROJECT_NAME = os.getenv('PROJECT_NAME')
  current_dir = os.path.abspath(os.curdir)
  project_dir = current_dir[:current_dir.find(f"{PROJECT_NAME}")+len(f"{PROJECT_NAME}")]
  src_dir = os.path.join(project_dir, 'src')
  if src_dir not in sys.path: sys.path.append(src_dir)
import logger
import graph_plotter

import resolver_config as conf
import checker

def _calc_approximate_function(
   origin_arr: list
  ) -> any:
  '''
  解から平滑化した近似関数を求める
  '''
  result = []
  arr_len = len(origin_arr)
  dif_list = (-3, -2, -1, 0, 1, 2, 3)
  for i in range(arr_len):
    effective_dif_count = 0
    item = 0
    for dif in dif_list:
      index = i + dif 
      if index < 0 or index > arr_len - 1 :
        continue
      item += origin_arr[i+dif]
      effective_dif_count += 1
    result.append(item / effective_dif_count)
  return result

def generate_new_solution(
    # 制約条件無視で生成させたい配列
    origin_list: list
  ) -> list:
  '''
  関数を確率に見立てて、制約条件から解を生成
  '''
  comp_map_per_time = []
  origin_list_sum = sum(origin_list)
  weights = []
  # 各エージェントタイプごとに近似関数他を生成
  for i in range(conf.type_sum):
    origin_list_per_time = copy.copy(origin_list[i*conf.time_max : (i+1)*conf.time_max])
    approximate = _calc_approximate_function(origin_list_per_time)
    origin_result_arr = [approximate[i] for i in range(len(origin_list_per_time))]
    weights.extend([item / origin_list_sum for item in origin_result_arr])
    comp_map_per_time.append({
      'approximate': approximate,
      'origin_result_arr': origin_result_arr,
      'origin_result_len': len(origin_result_arr),
    })

  # 各タイプを考慮したランダム選択
  select_list = [0 for _ in range(conf.time_max * conf.type_sum)]
  for _ in range(conf.agent_sum):
    selected_i = random.choices(list(range(conf.time_max * conf.type_sum)), k=1, weights=weights)[0]
    selected_time_i = selected_i % conf.time_max
    select_list[selected_i] += 1

    # 制約条件による生成時の制限
    time_sum = 0
    for i in range(conf.type_sum):
      time_sum += select_list[i * conf.time_max + selected_time_i]
    if time_sum == (conf.unit_minute_max - conf.unit_minute_min):
      for i in range(conf.type_sum):
        weights[selected_time_i + i * conf.time_max] = 0

  for i in range(conf.type_sum):
    logger.log_debug( f'create-ans-{i} : { select_list[i*conf.time_max : (i+1)*conf.time_max] }' )

  logger.log_debug(f'generate: {select_list}')

  checker.check_agent_length(select_list)
  checker.check_agent_sum(select_list)

  plot_map = {}
  select_sum_list = [0 for _ in range(conf.time_max)]
  approximate_sum_list = [0 for _ in range(conf.time_max)]
  for type_i in range(conf.type_sum):
    for time_i in range(conf.time_max):
      select_sum_list[time_i] += select_list[type_i * conf.time_max + time_i]
      approximate_sum_list[time_i] += comp_map_per_time[type_i]['approximate'][time_i]
  plot_map['select_sum_list'] =  select_sum_list
  plot_map['approximate_sum_list'] = approximate_sum_list
  plot_map['select_list_per_type'] = []
  for i in range(conf.type_sum):
    plot_map['select_list_per_type'].append({
      'approximate': comp_map_per_time[i]['approximate'],
      'select_list': select_list[i*conf.time_max : (i+1)*conf.time_max]
    })
  graph_name = graph_plotter.plot_person_per_time_and_approximate_function(np.arange(conf.time_max), plot_map)

  return select_list, graph_name
