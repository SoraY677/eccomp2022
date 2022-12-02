import os
import random
import shutil

import logger
import optimize_mock

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(f"{PROJECT_NAME}")+len(f"{PROJECT_NAME}")]

filepath = ""
best_score_list = []

def init(
  filename:str,
  is_clear: bool
) -> None:
  '''
  初期化
  - ファイルパス記録
  - ファイルに既に値が入っていれば読み出し
  '''
  global best_score_list
  global filepath
  save_dir = os.path.join(project_dir, 'log', 'score')
  
  if is_clear:
    try:
      shutil.rmtree(save_dir)
    except:
      pass
  os.makedirs(save_dir, exist_ok=True)
  filepath = os.path.join(save_dir, filename)
  try:
    logger.log_info(f'search {filepath}')
    with open(filepath, 'r') as f:
      score_text = f.read()
      if score_text != "":
        best_score_list = [float(score) for score in score_text.split('\n')]
  except:
      logger.log_info('not found prev score file')
      best_score_list = []

def submit_server(solution, match_number, is_practice):
  if is_practice:
    return optimize_mock.optimize(solution)
  score = random.random()
  return score

def run(
  solution,
  match_number,
  is_practice
):
  '''
  解提出
  '''
  global best_score_list
  global filepath
  logger.log_info(f'[solution-submit]')
  score = submit_server(solution, match_number, is_practice)
  logger.log_info(f'score: {score}')

  # ベストスコア更新
  best_score = score if(len(best_score_list) == 0) else best_score_list[-1]
  if(score < best_score):
    message = f'[++++best score updated!+++++]{score}'
    logger.log_info(f'{message}')
    best_score = score
  best_score_list.append(best_score)
  # スコアを保存
  with open(filepath, 'w') as f:
      score_text = "\n".join([str(best_score) for best_score in best_score_list])
      f.write(f'{score_text}')
  return score

def get_best_score_list():
  global best_score_list
  return best_score_list
