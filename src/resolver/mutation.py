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
import resolver_config as conf
import generator

def mutate(
      origin_solution: list
    ) -> map:
  '''
  変異
  
  '''
  result = copy.copy(origin_solution)
  result_len = len(result)

  LOOP_MAX = random.randint(int(conf.agent_sum / 2), conf.agent_sum)
  for _ in range(LOOP_MAX):
    weights = [1 if origin_item > 0 else 0 for origin_item in origin_solution]
    subtract_i = random.choices(list(range(result_len)), k=1, weights=weights)[0]
    result[subtract_i] -= 1

    add_i = random.randint(0, result_len - 1)
    result[add_i] +=1

  return generator.generate_new_solution(result)
