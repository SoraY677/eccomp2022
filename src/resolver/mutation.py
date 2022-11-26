import os
import sys
import random
import copy

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
      origin_solution: list,
      unit_minute_min: int,
      unit_minute_max: int,
      agent_sum: int
    ) -> list:
  '''
  突然変異
  = 初期解生成時のランダム生成
  '''
  logger.log_info('[mutate]')
  new_solution = copy.copy(origin_solution)
  new_solution_len = len(new_solution)
  LOOP_MAX = random.randint(1, agent_sum)

  for _ in range(LOOP_MAX):
    weights = [1 if origin_item > 0 else 0 for origin_item in new_solution]
    subtract_i = random.choices(list(range(new_solution_len)), k=1, weights=weights)[0]
    new_solution[subtract_i] -= 1

    weights = [1 if origin_item < (unit_minute_max - unit_minute_min) else 0 for origin_item in new_solution]
    add_i = random.choices(list(range(new_solution_len)), k=1, weights=weights)[0]
    new_solution[add_i] +=1

  return new_solution
