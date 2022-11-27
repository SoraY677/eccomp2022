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

def union(
    arr1: list,
    arr2: list
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
  result, graph_path = generator.generate_new_solution(union_origin_result)

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
    new_arr.append((arr1[i] + arr2[i]) ** 1.6 )
  return new_arr
