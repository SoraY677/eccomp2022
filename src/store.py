import os
import json

import logger

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(f"{PROJECT_NAME}")+len(f"{PROJECT_NAME}")]

filepath = ""

def init(filename):
  global filepath
  save_dir = os.path.join(project_dir, 'log', 'store')
  os.makedirs(save_dir, exist_ok=True)
  filepath = os.path.join(save_dir, f'{filename}.json')

  try:
    logger.log_info(f'search {filepath}')
    with open(filepath, 'r') as f:
      store_map = json.load(f)
  except:
      logger.log_info('not found prev score file')
      store_map = None

  return store_map

def save(
    count_index, 
    solution_list,
    score_list
  ):
  global filepath
  save_data = {
    'count_index': count_index,
    'solution_list' : solution_list,
    'score_list': score_list
  }

  try:
    logger.log_info(f'save {filepath}')
    with open(filepath, 'w') as f:
      json.dump(save_data, f, indent=2, ensure_ascii=False)
  except:
      logger.log_info(f'can`t write {filepath}')
