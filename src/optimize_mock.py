import numpy as np
import random
import graph_plotter
import logger
import math
import copy

_gauss_function_result_list = []
_mock_result = []

def gauss(x, a=1, mu=0, sigma=1):
  return a * np.exp(-(x - mu)**2 / (2*sigma**2))

def generate_answer(
  gauss_function_result_list,
  time_max, 
  unit_minute_min,
  unit_minute_max,
  agent_sum,
  type_sum
):
  weights_copy_list = copy.deepcopy(gauss_function_result_list)
  select_list = [0] * (time_max * type_sum)
  for _ in range(agent_sum):
    selected_type_index = random.randint(0, type_sum - 1)
    selected_time_index = random.choices(list(range(time_max)), k=1, weights=weights_copy_list[selected_type_index])[0]
    select_list[selected_time_index + selected_type_index * time_max] += 1
    time_sum = 0
    for i in range(type_sum):
      time_sum += select_list[selected_time_index + i * time_max]
    if time_sum == (unit_minute_max - unit_minute_min):
      for _ in range(type_sum):
        weights_copy_list[selected_type_index][selected_time_index] = 0
  
  logger.log_debug(f'agent length check....: [length]{agent_sum} : [sum]{sum(select_list)}')
  if sum(select_list) != agent_sum:
    logger.log_error('agent length check fail!')

  isSizePass = max(select_list) <= ( unit_minute_max - unit_minute_min )
  logger.log_debug(f'agent size over check....: {max(select_list)}')
  if not isSizePass:
    logger.log_error('agent size check fail!')

  return select_list

def calc_least_squares_error(test_solution):
  global _mock_result
  answer_solution = copy.copy(_mock_result)
  test_solution_length = len(test_solution)
  answer_solution_length = len(answer_solution)
  logger.log_debug(f'length check....: [length]{test_solution_length} : [ans_length]{answer_solution_length}')
  if test_solution_length != answer_solution_length:
    logger.log_error('length check fail!')

  result = 0.0
  for i in range(test_solution_length):
    result += math.sqrt((test_solution[i] - answer_solution[i]) ** 2)
  return result

def init(
    time_max, 
    unit_minute_min,
    unit_minute_max,
    agent_sum,
    type_sum
  ):
  global _gauss_function_result_list
  x = np.arange(0, time_max, 1)
  multi_gauss_result = [0] * x
  for _ in range(type_sum):
    gauss_function_result = gauss(x, a=random.random(), mu=time_max/4 + random.randint(0, time_max/2), sigma=50)
    _gauss_function_result_list.append(gauss_function_result)
    multi_gauss_result = [x + y for (x, y) in zip(multi_gauss_result, gauss_function_result)]

  global _mock_result
  _mock_result = generate_answer(
    _gauss_function_result_list,
    time_max, 
    unit_minute_min,
    unit_minute_max,
    agent_sum,
    type_sum
  )

  mock_result_unit = [0] * time_max
  for i in range(time_max):
    for j in range(type_sum):
      mock_result_unit[i] += _mock_result[i + j * time_max]

  graph_plotter.plot_practice_gauss(x, _gauss_function_result_list, np.array(multi_gauss_result), np.array(mock_result_unit))

def optimize(solution_list):
  score_list = []
  for solution in solution_list:
    score = calc_least_squares_error(solution)
    score_list.append(score)
  return score_list
