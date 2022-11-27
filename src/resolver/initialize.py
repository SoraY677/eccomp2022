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

def run() -> list:
  '''
  初期解生成
  ランダムに解を生成
  '''
  logger.log_info('[random generate]')
  selected_list = [0 for _ in range(conf.time_max * conf.type_sum)]
  for _ in range(conf.agent_sum):
    selected_type_i = random.randint(0, conf.type_sum - 1)
    selected_time_i = random.randint(0, conf.time_max - 1)
    selected_list[selected_time_i + selected_type_i * conf.time_max] += 1

  result, graph_path = generator.generate_new_solution(selected_list)
  return result, graph_path
