import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import datetime

import logger
import constraint
from exec import run
import submit
import store
import graph_plotter

def _check_command_exist(arr: list, default: str):
  for item in arr:
     if f'-{item}' in sys.argv:
      return item
  return default

def get_argv() -> None:
  '''
  コマンドライン引数を取得
  '''
  mode = constraint.MODE_PRACTICE
  optimize_mode = constraint.OPTIMIZE_MODE_SINGLE
  optimize_number = constraint.OPTIMIZE_NUMBER_1

  mode = _check_command_exist([constraint.MODE_PRACTICE, constraint.MODE_DEMO, constraint.MODE_PROD], constraint.MODE_PRACTICE)
  optimize_mode = _check_command_exist([constraint.OPTIMIZE_MODE_SINGLE, constraint.OPTIMIZE_MODE_MULTI], constraint.OPTIMIZE_MODE_SINGLE)
  optimize_number = _check_command_exist([constraint.OPTIMIZE_NUMBER_1, constraint.OPTIMIZE_NUMBER_2], constraint.OPTIMIZE_NUMBER_1)

  # -clearコマンドがあったときにログを削除
  is_clear = not (_check_command_exist(["clear"],None) is None)


  return mode, optimize_mode, optimize_number, is_clear

def process() -> None:
  '''
  処理実施
  + 処理時間計測
  '''
  mode, optimize_mode, optimize_number, is_clear = get_argv()
  
  id = f"{optimize_mode}-{mode}-{optimize_number}"

  logger.init(id, is_clear)
  logger.log_info('process start')

  logger.log_info(f'mode:{mode} / sop,mop:{optimize_mode} / number:{optimize_number}')
  submit.init(id, is_clear)
  store_map = store.init(id, is_clear)
  graph_plotter.init(id, is_clear)

  logger.log_info(f'app start')
  logger.log_info(f'[mode] {mode}')

  dt_start =  datetime.datetime.today()
  logger.log_info(f'[start]{dt_start.year}-{dt_start.month}-{dt_start.day} {dt_start.hour}:{dt_start.minute}:{dt_start.second}')

  run(
    mode,
    optimize_mode,
    optimize_number,
    store_map
  )

  dt_end = datetime.datetime.today()
  logger.log_info(f'[end]{dt_end.year}-{dt_end.month}-{dt_end.day} {dt_end.hour}:{dt_end.minute}:{dt_end.second}')

  logger.log_info(f'----------------------------------')

  dt_dif = dt_end - dt_start
  logger.log_info(f'[process result]{dt_dif.days}d {dt_dif.seconds}.{dt_dif.microseconds}s')

  best_score_list = submit.get_best_score_list()
  graph_plotter.plot_best_score_list(best_score_list)
  
__all__ = ['process']
