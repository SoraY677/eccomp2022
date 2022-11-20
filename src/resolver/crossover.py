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
  project_dir = current_dir[:current_dir.find("{PROJECT_NAME}")+len("{PROJECT_NAME}")]
  sys.path.append(os.path.join(project_dir, 'src'))
import logger

def cross(
    arr1,
    arr2,
    cross_point_num,
    length,
    unit_second_min,
    unit_second_max,):
  logger.log_info('cross')
  logger.log_info(f'arr1: {arr1}')
  logger.log_info(f'arr2: {arr2}')
  if len(arr1) != len(arr2):
    logger.log_error('cross over arr length not correct!')
  cross_origin_result = _cross_2solutions(arr1, arr2, cross_point_num)
  result = _create_new_solution(cross_origin_result, length, unit_second_min, unit_second_max)

  logger.log_info(f'cross result: {result}')

  logger.log_info(f'agent length check....: [length]{length} : [sum]{sum(result)}')
  if sum(result) == length:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  isSizePass = max(result) < (unit_second_max - unit_second_min)
  logger.log_info(f'agent size over check....: {isSizePass}')
  if isSizePass:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent size check fail!')

  return result

def union(
    arr1,
    arr2,
    length,
    unit_second_min,
    unit_second_max
  ):
  logger.log_info('union')
  logger.log_info(f'arr1: {arr1}')
  logger.log_info(f'arr2: {arr2}')
  if len(arr1) != len(arr2):
    logger.log_error('cross over arr length not correct!')
  union_origin_result = _union_2solutions(arr1, arr2)
  result = _create_new_solution(union_origin_result, length, unit_second_min, unit_second_max)

  logger.log_info(f'union result: {result}')

  logger.log_info(f'agent length check....: [length]{length} : [sum]{sum(result)}')
  if sum(result) == length:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  isSizePass = max(result) < (unit_second_max - unit_second_min)
  logger.log_info(f'agent size over check....: {isSizePass}')
  if isSizePass:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent size check fail!')
  return result

def _cross_2solutions(arr1, arr2, cross_point_num):
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

def _union_2solutions(arr1, arr2):
  new_arr = []
  for i in range(len(arr1)):
    new_arr.append(arr1[i] + arr2[i])
  return new_arr

def _approximate_function(crossed_arr):
  t = np.arange(len(crossed_arr))
  x = np.array(crossed_arr)
  func = interp1d(t,x,kind='cubic')
  return func

def _create_new_solution(
    origin_result,
    length,
    unit_second_min,
    unit_second_max,
  ):
  approximate_function = _approximate_function(origin_result)
  origin_result_arr = [approximate_function(i) for i in range(len(origin_result))]
  origin_result_sum = sum(origin_result_arr)
  origin_result_len = len(origin_result_arr)

  select_list = [0 for _ in range(origin_result_len)]
  weights = [item / origin_result_sum for item in origin_result_arr]
  for _ in range(length):
    selected_index = random.choices(list(range(origin_result_len)), k=1, weights=weights)[0]
    select_list[selected_index] += 1
    if select_list[selected_index] == (unit_second_max - unit_second_min):
      weights[selected_index] = 0

  return select_list

