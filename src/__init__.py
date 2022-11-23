import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import datetime

import logger
import constraint
from exec import run

def get_argv() -> None:
  '''
  コマンドライン引数を取得
  '''
  mode = constraint.MODE_DEMO
  optimize_mode = constraint.OPTIMIZE_MODE_SINGLE
  optimize_number = constraint.OPTIMIZE_NUMBER_1
  try:
    mode = sys.argv[1]
    optimize_mode = sys.argv[2]
    optimize_number = sys.argv[3]
  except:
    logger.log_info(f'mode:{mode} / sop,mop:{optimize_mode} / number:{optimize_number}')

  if mode not in [constraint.MODE_DEMO, constraint.MODE_PROD]:
    logger.log_error(f'mode was specified {mode}')

  if optimize_mode not in [constraint.OPTIMIZE_MODE_SINGLE, constraint.OPTIMIZE_MODE_MULTI]:
    logger.log_error(f'optimize_mode(sop or mop) was specified {optimize_mode}')
  
  if optimize_number not in [constraint.OPTIMIZE_NUMBER_1, constraint.OPTIMIZE_NUMBER_2]:
    logger.log_error(f'optimize_number(1 or 2) was specified {optimize_number}')

  return mode, optimize_mode, optimize_number

def process() -> None:
  '''
  処理実施
  + 処理時間計測
  '''
  logger.log_info('process start')

  mode, optimize_mode, optimize_number = get_argv()

  logger.log_info(f'app start')
  logger.log_info(f'[mode] {mode}')

  dt_start =  datetime.datetime.today()
  logger.log_info(f'[start]{dt_start.year}-{dt_start.month}-{dt_start.day} {dt_start.hour}:{dt_start.minute}:{dt_start.second}')

  run(
    mode,
    optimize_mode,
    optimize_number
  )

  dt_end = datetime.datetime.today()
  logger.log_info(f'[end]{dt_end.year}-{dt_end.month}-{dt_end.day} {dt_end.hour}:{dt_end.minute}:{dt_end.second}')

  logger.log_info(f'----------------------------------')

  dt_dif = dt_end - dt_start
  logger.log_info(f'[process result]{dt_dif.days}d {dt_dif.seconds}.{dt_dif.microseconds}s')
  
__all__ = ['process']

if __name__ == "__main__":
  print(sys.argv)
