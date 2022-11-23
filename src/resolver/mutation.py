import os
import sys

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

from generate import random_generate

def mutate(
      time_max: int,
      unit_minute_min: int,
      unit_minute_max: int,
      agent_sum: int
    ) -> list:
  '''
  突然変異
  = 初期解生成時のランダム生成
  '''

  logger.log_info('[mutate]')
  solution = random_generate(time_max, unit_minute_min, unit_minute_max, agent_sum)
  logger.log_info(f'mutate solution: {solution}')
  return solution
