import numpy as np
import random
import graph_plotter
import logger
import math

_gauss_function_result_list = []
_mock_result = []

def gauss(x, a=1, mu=0, sigma=1):
  return a * np.exp(-(x - mu)**2 / (2*sigma**2))

def generate_answer(
  weights,
  time_max, 
  unit_minute_min,
  unit_minute_max,
  agent_sum
):
  global _mock_result
  select_list = [0] * time_max
  for _ in range(agent_sum):
    selected_index = random.choices(list(range(time_max)), k=1, weights=weights)[0]
    select_list[selected_index] += 1
    if select_list[selected_index] == (unit_minute_max - unit_minute_min):
      weights[selected_index] = 0
  
  logger.log_info(select_list)
  logger.log_info(f'agent length check....: [length]{agent_sum} : [sum]{sum(select_list)}')
  if sum(select_list) == agent_sum:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  isSizePass = max(select_list) < ( unit_minute_max - unit_minute_min )
  logger.log_info(f'agent size over check....: {max(select_list)}')
  if isSizePass:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent size check fail!')

  return select_list

def calc_least_squares_error(test_solution, answer_solution):
  test_solution_length = len(test_solution)
  answer_solution_length = len(answer_solution)
  logger.log_info(f'length check....: [length]{test_solution_length} : [sum]{sum(answer_solution_length)}')
  if sum(test_solution_length) == answer_solution_length:
    logger.log_info('no problem!!')
  else:
    logger.log_error('length check fail!')

  result = 0.0
  for i in test_solution_length:
    result += math.sqrt((test_solution[i] - answer_solution[i]) ** 2)

  return result




def init(
    time_max, 
    unit_minute_min,
    unit_minute_max,
    agent_sum
  ):
  global _gauss_function_result_list
  x = np.arange(0, time_max, 1)
  multi_gauss_result = [0] * x
  for _ in range(1):
    gauss_function_result = gauss(x, a=0.1, mu=time_max/2, sigma=100)
    _gauss_function_result_list.append(gauss_function_result)
    multi_gauss_result = [x + y for (x, y) in zip(multi_gauss_result, gauss_function_result)]

  answer = generate_answer(
    multi_gauss_result,
    time_max, 
    unit_minute_min,
    unit_minute_max,
    agent_sum
  )
  graph_plotter.plot_practice_gauss(x, _gauss_function_result_list, np.array(multi_gauss_result), np.array(answer))


def response(solution):
  
  return random.random()
