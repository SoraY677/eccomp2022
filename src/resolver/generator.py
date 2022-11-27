'''

解生成用関数
実際に提出用に条件付きで解が生成される部分

'''

import os
import sys
import random

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
    origin_arr: list
  ) -> list:
  '''
  関数を確率に見立てて、制約条件から解を生成
  '''
  approximate = _calc_approximate_function(origin_arr)
  origin_result_arr = [approximate[i] for i in range(len(origin_arr))]
  origin_result_sum = sum(origin_result_arr)
  origin_result_len = len(origin_result_arr)

  select_list = [0 for _ in range(origin_result_len)]
  weights = [item / origin_result_sum for item in origin_result_arr]
  for _ in range(conf.agent_sum):
    selected_index = random.choices(list(range(origin_result_len)), k=1, weights=weights)[0]
    select_list[selected_index] += 1
    if select_list[selected_index] == (conf.unit_minute_max - conf.unit_minute_min):
      weights[selected_index] = 0

  logger.log_info(f'generate: {select_list}')

  checker.check_agent_length(select_list)
  checker.check_agent_size_per_time(select_list)
  graph_name = graph_plotter.plot_person_per_time_and_approximate_function(np.arange(len(select_list)), np.array(select_list), approximate)

  return select_list, graph_name
