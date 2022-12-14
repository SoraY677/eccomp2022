import os
import sys
import random

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

import generator
import util

def run(
    arr1: list,
    arr2: list
  ) -> list:
  '''
  合成
  '''
  logger.log_debug(f'arr1: {arr1}')
  logger.log_debug(f'arr2: {arr2}')
  if len(arr1) != len(arr2):
    logger.log_error('cross over arr length not correct!')
  arr_per_time1 = util.get_select_list_per_type(arr1)
  arr_per_time2 = util.get_select_list_per_type(arr2)
  union_arrange_list = []
  for i in range(len(arr_per_time1)):
    union_arrange_list.extend(_union_2solutions(arr_per_time1[i], arr_per_time2[i]))
  result, graph_path = generator.generate_new_solution(union_arrange_list)

  return result, graph_path

def _union_2solutions(
    arr1: int,
    arr2: int
  ) -> list:
  '''
  実際の合成部
  '''
  new_arr = []
  for i in range(len(arr1)):
    new_arr.append(int(arr1[i] + arr2[i]))
  return new_arr
