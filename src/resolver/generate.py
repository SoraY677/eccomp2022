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

def random_generate(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum
    ):
  '''
  初期解生成
  ランダムに解を生成

  Args:
    - time_max (Int)
    - unit_minute_min (Int)
    - unit_minute_max (Int)
    - agent_sum (Int)

  Returns:
      list<int>: 生成解
  '''
  logger.log_info('[random generate]')
  # 各時刻分×最大人数 の配列を生成
  lottery_list = [i for i in range(time_max)] * (unit_minute_max - unit_minute_min)
  # 最大数まで選び出し、数字をカウント
  select_list = []
  for _ in range(agent_sum):
    selected_i = random.randint(0, len(lottery_list) - 1)
    select_list.append(lottery_list.pop(selected_i))
  select_list.sort()
  select_list = tuple(select_list)
  count_list = [0 for _ in range(time_max)]
  for i in range(time_max):
    count_list[i] = select_list.count(i)

  logger.log_info(count_list)
  logger.log_info(f'agent length check....: [length]{agent_sum} : [sum]{sum(count_list)}')
  if sum(count_list) == agent_sum:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  isSizePass = max(count_list) < (unit_minute_max - unit_minute_min)
  logger.log_info(f'agent size over check....: {isSizePass}')
  if isSizePass:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent size check fail!')

  return count_list
