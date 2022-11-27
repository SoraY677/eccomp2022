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

import resolver_config as conf
import generator

def random_generate() -> list:
  '''
  初期解生成
  ランダムに解を生成
  '''
  logger.log_info('[random generate]')
  selected_list = [0] * conf.time_max * conf.type_sum
  for _ in range(conf.agent_sum):
    selected_i = random.randint(0, len(conf.time_max) - 1)
    selected_list[selected_i] += 1

  result, graphpath = generator.generate_new_solution(selected_list)
  return result, graphpath
