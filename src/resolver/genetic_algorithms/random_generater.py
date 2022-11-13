import os
import sys
import random

if __name__ == '__main__':
  sys.path.append(os.path.abspath('../..'))
  import logger
else:
  current_dir = os.path.abspath(os.curdir)
  project_dir = current_dir[:current_dir.find("eccomp2022")+len("eccomp2022")]
  sys.path.append(os.path.join(project_dir, 'src'))
  import logger

def generate(
      length,
      unit_second_min,
      unit_second_max,
      time_max
    ):
  # 各時刻分×最大人数 の配列を生成
  lottery_list = [i for i in range(time_max)] * (unit_second_max - unit_second_min)
  # 最大数まで選び出し、数字をカウント
  select_list = []
  for _ in range(length):
    selected_i = random.randint(0, len(lottery_list))
    select_list.append(lottery_list.pop(selected_i))
  select_list.sort()
  select_list = tuple(select_list)
  count_list = [0 for _ in range(time_max)]
  for i in range(time_max):
    count_list[i] = select_list.count(i)

  logger.log_info(count_list)
  logger.log_info(f'agent length check....: [length]{length} : [sum]{sum(count_list)}')
  if sum(count_list) == length:
    logger.log_info('no problem!!')
  else:
    logger.log_error('agent length check fail!')

  return count_list

if __name__ == '__main__':
  import graph_plotter
  length = 300
  unit_second_min = 0
  unit_second_max = 45
  time_max = 300
  count_list = generate(length, unit_second_min, unit_second_max, time_max)
  print(len(count_list))
  graph_plotter.plotPersonPerTime(count_list)
  

