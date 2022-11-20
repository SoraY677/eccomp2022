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
      length,
      unit_second_min,
      unit_second_max,
      time_max
    ):
  logger.log_info('[mutate]')
  solution = random_generate(length,unit_second_min,unit_second_max,time_max)
  logger.log_info(f'mutate solution: {solution}')
  return solution

