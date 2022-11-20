import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import datetime

import logger
import config
from exec import run


def process():
  logger.log_info('process start')
  if len(sys.argv) != 2:
    logger.log_error('mode not specified!')
    return
  mode = sys.argv[1]

  logger.log_info(f'app start')
  logger.log_info(f'[mode] {mode}')

  dt_start =  datetime.datetime.today()
  logger.log_info(f'[start]{dt_start.year}-{dt_start.month}-{dt_start.day} {dt_start.hour}:{dt_start.minute}:{dt_start.second}')

  run()

  dt_end = datetime.datetime.today()
  logger.log_info(f'[end]{dt_end.year}-{dt_end.month}-{dt_end.day} {dt_end.hour}:{dt_end.minute}:{dt_end.second}')

  logger.log_info(f'----------------------------------')

  dt_dif = dt_end - dt_start
  logger.log_info(f'[process result]{dt_dif.days}d {dt_dif.seconds}.{dt_dif.microseconds}s')
  
__all__ = ['process']
