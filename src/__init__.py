import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import datetime

import logger
import command
from exec import run
import submit
import store
import graph_plotter

def process() -> None:
  '''
  処理実施
  + 処理時間計測
  '''
  mode, optimize_mode, optimize_number, is_clear = command.get_option()

  # 対象問題から生成するID
  id = f"{optimize_mode}-{mode}-{optimize_number}"

  logger.init(id, is_clear)
  submit.init(id, is_clear)
  store_map = store.init(id, is_clear)
  graph_plotter.init(id, is_clear)

  logger.log_info(f'[mode] {mode}')

  dt_start =  datetime.datetime.today()
  logger.log_info(f'[start]{dt_start.strftime("%Y-%m-%d %H:%M:%S")}')

  run(mode, optimize_mode,optimize_number, store_map)

  dt_end = datetime.datetime.today()
  logger.log_info(f'[end]{dt_end.strftime("%Y-%m-%d %H:%M:%S")}')

  logger.log_info(f'----------------------------------')

  dt_dif = dt_end - dt_start
  logger.log_info(f'[process result]{dt_dif.days}d {dt_dif.seconds}.{dt_dif.microseconds}s')

  best_score_list = submit.get_best_score_list()
  graph_plotter.plot_best_score_list(best_score_list)
  
__all__ = ['process']
