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
import logger

import util

def cross(
    arr1: list,
    arr2: list,
    cross_point_num: int,
    unit_minute_min: int,
    unit_minute_max: int,
    agent_sum: int
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
  result, graph_path = util.create_new_solution(cross_origin_result, unit_minute_min, unit_minute_max, agent_sum)

  logger.log_info(f'cross result: {result}')

  logger.log_debug(f'agent length check....: [length]{agent_sum} : [sum]{sum(result)}')
  if sum(result) == agent_sum:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  isSizePass = max(result) <= ( unit_minute_max - unit_minute_min )
  logger.log_debug(f'agent size over check....: {max(result)}')
  if isSizePass:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent size check fail!')

  return result, graph_path

def union(
    arr1: list,
    arr2: list,
    unit_minute_min: int,
    unit_minute_max: int,
    agent_sum: int
  ) -> list:
  '''
  合成
  '''
  logger.log_info('[union]')
  logger.log_info(f'arr1: {arr1}')
  logger.log_info(f'arr2: {arr2}')
  if len(arr1) != len(arr2):
    logger.log_error('cross over arr length not correct!')
  union_origin_result = _union_2solutions(arr1, arr2)
  result, graph_path = util.create_new_solution(union_origin_result, unit_minute_min, unit_minute_max, agent_sum)

  logger.log_info(f'union result: {result}')

  logger.log_debug(f'agent length check....: [length]{agent_sum} : [sum]{sum(result)}')
  if sum(result) == agent_sum:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  isSizePass = max(result) <= ( unit_minute_max - unit_minute_min )
  logger.log_debug(f'agent size over check....: {max(result)}')
  if isSizePass:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent size check fail!')
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

def _union_2solutions(
    arr1: int,
    arr2: int
  ) -> list:
  '''
  実際の合成部
  '''
  new_arr = []
  for i in range(len(arr1)):
    new_arr.append((arr1[i] + arr2[i]) ** 2 )
  return new_arr

