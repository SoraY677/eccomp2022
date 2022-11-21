import os
import sys

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

from generate import random_generate

def mutate(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum
    ):
  '''
  突然変異
  = 初期解生成時のランダム生成

  Args:
      time_max (Int)
      unit_minute_min (Int)
      unit_minute_max (Int)
      agent_sum (Int)

  Returns:
      List<Int>: 生成した解
  '''

  logger.log_info('[mutate]')
  solution = random_generate(time_max, unit_minute_min, unit_minute_max, agent_sum)
  logger.log_info(f'mutate solution: {solution}')
  return solution

