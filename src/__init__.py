import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import datetime

import logger
import config
import constraint
from exec import run

_mode = constraint.MODE_DEMO
_optimize_mode = constraint.OPTIMIZE_MODE_SINGLE
_optimize_number = constraint.OPTIMIZE_NUMBER_1

def get_argv():
  '''
  コマンドライン引数を取得
  '''
  try:
    _mode = sys.argv[1]
    _optimize_mode = sys.argv[2]
    _optimize_number = sys.argv[3]
  except:
    logger.log_info(f'mode:{_mode} / sop,mop:{_optimize_mode} / number:{_optimize_number}')

  if _mode not in [constraint.MODE_DEMO, constraint.MODE_PROD]:
    logger.log_error(f'mode was specified {_mode}')
    exit(-1)

  if _optimize_mode not in [constraint.OPTIMIZE_MODE_SINGLE, constraint.OPTIMIZE_MODE_MULTI]:
    logger.log_error(f'optimize_mode(sop or mop) was specified {_optimize_mode}')
    exit(-1)
  
  if _optimize_number not in [constraint.OPTIMIZE_NUMBER_1, constraint.OPTIMIZE_NUMBER_2]:
    logger.log_error(f'optimize_number(1 or 2) was specified {_optimize_number}')
    exit(-1)

def process():
  '''
  処理実施
  + 処理時間計測
  '''
  logger.log_info('process start')


  if len(sys.argv) != 2:
    logger.log_error('mode not specified!')
    return
  mode = sys.argv[1]

  logger.log_info(f'app start')
  logger.log_info(f'[mode] {mode}')

  dt_start =  datetime.datetime.today()
  logger.log_info(f'[start]{dt_start.year}-{dt_start.month}-{dt_start.day} {dt_start.hour}:{dt_start.minute}:{dt_start.second}')

  run(
    _mode,
    _optimize_mode,
    _optimize_number
  )

  dt_end = datetime.datetime.today()
  logger.log_info(f'[end]{dt_end.year}-{dt_end.month}-{dt_end.day} {dt_end.hour}:{dt_end.minute}:{dt_end.second}')

  logger.log_info(f'----------------------------------')

  dt_dif = dt_end - dt_start
  logger.log_info(f'[process result]{dt_dif.days}d {dt_dif.seconds}.{dt_dif.microseconds}s')
  
__all__ = ['process']

if __name__ == "__main__":
  print(sys.argv)
