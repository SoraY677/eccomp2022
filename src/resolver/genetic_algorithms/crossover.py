import os
import sys
import random

if __name__ == '__main__':
  sys.path.append(os.path.abspath('../..'))
else:
  current_dir = os.path.abspath(os.curdir)
  project_dir = current_dir[:current_dir.find("eccomp2022")+len("eccomp2022")]
  sys.path.append(os.path.join(project_dir, 'src'))
import logger

def create_probability_density_function(arr1, arr2, cross_point_num):
  logger.log_info('arr1: {arr1}')
  logger.log_info('arr2: {arr2}')
  if len(arr1) != len(arr2):
    logger.log_error('cross over arr length not correct!')

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
      new_solve += arr[prev_point_index:i+1]
      is_target_arr1 = not is_target_arr1
      prev_point_index = i + 1
  result += arr[prev_point_index:]
  logger.log_info('new solve: {result}')
  return result


if __name__ == '__main__':
  for i in range(1000):
    result = create_probability_density_function([1,2,3,4,5],[6,7,8,9,0],6)
    print(result)
