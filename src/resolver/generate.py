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

def random_generate(
      time_max: int,
      unit_minute_min: int,
      unit_minute_max: int,
      agent_sum: int
    ) -> list:
  '''
  初期解生成
  ランダムに解を生成
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
  
  logger.log_debug(f'agent length check....: [length]{agent_sum} : [sum]{sum(count_list)}')
  if sum(count_list) == agent_sum:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  isSizePass = max(count_list) <= ( unit_minute_max - unit_minute_min )
  logger.log_debug(f'agent size over check....: {max(count_list)}')
  if isSizePass:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent size check fail!')

  return count_list
