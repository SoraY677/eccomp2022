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

import resolver_config as conf

def is_valid_agent_sum(count_list):
  logger.log_debug(f'agent length check....: [length]{conf.agent_sum} : [count list sum]{sum(count_list)}')
  if sum(count_list) == conf.agent_sum:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent length check fail!')

def check_agent_length(result):
  sum_num = sum(result)
  logger.log_debug(f'agent length check....: [length]{conf.agent_sum} : [sum]{sum_num}')
  if sum_num == conf.agent_sum:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent length check fail!')

def check_agent_size_per_time(result):
  max_per_time = conf.unit_minute_max - conf.unit_minute_min
  max_num = max(result)
  isSizePass = max_num <= ( max_per_time )
  logger.log_debug(f'agent size over check....: {max_num}')
  if isSizePass:
    logger.log_debug('no problem!!')
  else:
    logger.log_error('agent size check fail!')
