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

def run(
    arr1: list,
    arr2: list,
    cross_point_num: int
  ) -> list:
  '''
  交叉
  '''
  logger.log_info('[cross]')
  logger.log_info(f'arr1: {arr1}')
  logger.log_info(f'arr2: {arr2}')
  if len(arr1) != len(arr2):
    logger.log_error('cross over arr length not correct!')
  cross_origin_result = _cross_2solutions(arr1, arr2, cross_point_num)
  result, graph_path = generator.generate_new_solution(cross_origin_result)

  logger.log_info(f'cross result: {result}')
  return result, graph_path

def _cross_2solutions(
    arr1: list,
    arr2: list,
    cross_point_num: int
  ) -> list:
  '''
  実際の交叉部
  '''
  is_selected_point_arr = [False for _ in range(len(arr1) - 1)]
  for _ in range(cross_point_num):
    point_index = random.randint(0, len(is_selected_point_arr)-1)
    is_selected_point_arr[point_index] = True

  result = []
  prev_point_index = 0
  is_target_arr1 = True
  for i in range(len(is_selected_point_arr)):
    if is_selected_point_arr[i]:
      arr = arr1 if is_target_arr1 else arr2
      result += arr[prev_point_index:i+1]
      is_target_arr1 = not is_target_arr1
      prev_point_index = i + 1
  result += arr[prev_point_index:]

  return result
