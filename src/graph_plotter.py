import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import shutil

import logger

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(PROJECT_NAME)+len(PROJECT_NAME)]

save_image_dir = None

def init(
  id: str,
  is_clear: bool
):
  global save_image_dir
  if is_clear:
    try:
      shutil.rmtree(os.path.join(project_dir, 'log', 'graph-image', id,))
    except:
      pass
  save_image_dir = os.path.join(project_dir, 'log', 'graph-image', id, datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
  logger.log_info(f'save graph image dir: {save_image_dir}')
  os.makedirs(save_image_dir, exist_ok=True)

def plot_person_per_time_and_approximate_function(
    t,
    plot_map
  ):
  color_list = ['blue', 'green', 'yellow']
  _, ax1 = plt.subplots(figsize=(17, 4))
  select_sum_list = plot_map['select_sum_list']
  ax1.bar(t, select_sum_list, color='gray', alpha=0.2)
  select_list_per_type = plot_map['select_list_per_type']
  ax2 = ax1.twinx()
  ax2.plot(t, plot_map['select_sum_list'], color='red', linewidth=1, alpha=1)
  for i in range(len(select_list_per_type)):
    ax2.plot(t, select_list_per_type[i]['select_list'], color=color_list[i % 3], linewidth=1, alpha=1)
  return save_file(plt)

def plot_best_score_list(best_score_list):
  t = np.arange(0, len(best_score_list), 1)
  ft = np.array(best_score_list)
  plt.plot(t, ft, linewidth=2.0)
  save_file(plt)

def plot_practice_gauss(
    x, 
    f_list, 
    multi_gauss_result,
    answer
  ):
  _, ax1 = plt.subplots(figsize=(17, 4))
  ax1.grid()
  for f in f_list:
    ax1.plot(x, f)
  ax1.plot(x, multi_gauss_result, color="red")

  ax2 = ax1.twinx()
  ax2.bar(x, answer, color='gray', alpha=0.5)
  save_file(plt)

def save_file(plt):
  global save_image_dir
  time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')[:-3]
  filepath = os.path.join(save_image_dir, time + '.png')
  plt.savefig(filepath, format="png", dpi=300)
  plt.close()
  return filepath
