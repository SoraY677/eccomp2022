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
  project_dir = current_dir[:current_dir.find("{PROJECT_NAME}")+len("{PROJECT_NAME}")]
  sys.path.append(os.path.join(project_dir, 'src'))
import logger

def select(
    score_list: list
  ) -> int:
  '''
  2個体選択
  '''
  score_list_sum = sum(score_list)
  select_priority_list = [score_list_sum - score for score in score_list]
  select_priority_min = min(select_priority_list)
  selected_weights = [priority / select_priority_min for priority in select_priority_list]
  logger.log_debug(f'selected weight: {selected_weights}')

  selected_index_list = random.choices(list(range(len(score_list))), k=2, weights=selected_weights)
  logger.log_debug(f'select index: {selected_index_list}')
  
  return selected_index_list[0], selected_index_list[1]
