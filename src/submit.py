import os
import shutil

import logger
import optimize_mock
import optimize_server

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

def submit_server(solution_list, match_number, is_practice, time_max, type_sum):
  if is_practice:
    return optimize_mock.optimize(solution_list, type_sum)

  return optimize_server.optimize(solution_list, match_number, time_max, type_sum)

def run(
  solution_list,
  match_number,
  is_practice,
  time_max,
  type_sum
):
  '''
  解提出
  '''
  global best_score_list
  global filepath
  logger.log_info(f'[solution-list-submit]')
  score_list = submit_server(solution_list, match_number, is_practice, time_max, type_sum)

  submit_min_score = min(score_list)
  # ベストスコア更新
  best_score = submit_min_score if(len(best_score_list) == 0) else best_score_list[-1]
  if(submit_min_score < best_score):
    message = f'[++++best score updated!+++++]{submit_min_score}'
    print(f'best:{submit_min_score}')
    logger.log_info(f'{message}')
    best_score = submit_min_score
  best_score_list.append(best_score)
  # スコアを保存
  with open(filepath, 'w') as f:
      score_text = "\n".join([str(best_score) for best_score in best_score_list])
      f.write(f'{score_text}')
  return score_list

def get_best_score_list():
  global best_score_list
  return best_score_list
