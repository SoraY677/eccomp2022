import os
import sys
import random

import numpy as np
from scipy.interpolate import interp1d

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
import graph_plotter

def _approximate_function(
   arr: list
  ) -> any:
  '''
  近似関数を求める
  '''
  result = []
  arr_len = len(arr)
  dif_list = (-3,-2, -1, 0, 1, 2, 3)
  for i in range(arr_len):
    item = 0
    for dif in dif_list:
      index = i + dif 
      if index < 0 or index > arr_len - 1 :
        continue
      item += arr[i+dif]
    result.append(item / len(dif_list))
  graph_name = graph_plotter.plot_person_per_time_and_approximate_function(np.arange(arr_len), np.array(arr), result)
  return result, graph_name

def create_new_solution(
    origin_result: list,
    unit_minute_min: int,
    unit_minute_max: int,
    agent_sum: int,
  ) -> list:
  '''
  新規に解を生成
  '''
  approximate, graph_name = _approximate_function(origin_result)
  origin_result_arr = [approximate[i] for i in range(len(origin_result))]
  origin_result_sum = sum(origin_result_arr)
  origin_result_len = len(origin_result_arr)

  select_list = [0 for _ in range(origin_result_len)]
  weights = [item / origin_result_sum for item in origin_result_arr]
  for _ in range(agent_sum):
    selected_index = random.choices(list(range(origin_result_len)), k=1, weights=weights)[0]
    select_list[selected_index] += 1
    if select_list[selected_index] == (unit_minute_max - unit_minute_min):
      weights[selected_index] = 0

  return select_list, graph_name
