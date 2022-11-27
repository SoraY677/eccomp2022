import os
import sys

if __name__ == '__main__':
  sys.path.append(os.path.abspath('../../..'))
else:
  from dotenv import load_dotenv
  load_dotenv()
  PROJECT_NAME = os.getenv('PROJECT_NAME')
  current_dir = os.path.abspath(os.curdir)
  project_dir = current_dir[:current_dir.find(f"{PROJECT_NAME}")+len(f"{PROJECT_NAME}")]
  src_dir = os.path.join(project_dir, 'src')
  if src_dir not in sys.path: sys.path.append(src_dir)
import logger

def is_valid_agent_sum(agent_sum, count_list):
  logger.log_debug(f'agent length check....: [length]{agent_sum} : [count list sum]{sum(count_list)}')
  if sum(count_list) == agent_sum:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent length check fail!')

def is_reach_max_per_time(time_index, time_max, count_list, max_num):
  time_valid_checker = count_list[time_index] + count_list[time_max + time_index] + count_list[time_max * 2 + time_index]
  if time_valid_checker == max_num:
      return True
  return False

def check_reach_max_per_type(time_max, count_list, type_guided_sum, type_busy_sum, type_slow_sum):  
  for i in range(3):
    if count_list[time_max*i : time_max*(i+1)-1] == (type_guided_sum, type_busy_sum, type_slow_sum)[i]:
      return i
  return -1

def check_agent_length(result, agent_sum):
  sum_num = sum(result)
  logger.log_debug(f'agent length check....: [length]{agent_sum} : [sum]{sum_num}')
  if sum_num == agent_sum:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent length check fail!')

def check_agent_size_per_time(result, max_per_time):
  max_num = max(result)
  isSizePass = max_num <= ( max_per_time )
  logger.log_debug(f'agent size over check....: {max_num}')
  if isSizePass:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent size check fail!')
