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
    x, 
    func
  ):
  
  _, ax1 = plt.subplots(figsize=(17, 4))
  ax2 = ax1.twinx()
  ax1.bar(t, x, color='gray', alpha=0.5)
  ax2.plot(t, func(t), linewidth=3, alpha=0.5)
  save_file(plt)

def plot_best_score_list(best_score_list):
  t = np.arange(0, len(best_score_list), 1)
  ft = np.array(best_score_list)
  plt.plot(t, ft, linewidth=2.0)
  save_file(plt)

def save_file(plt):
  global save_image_dir
  time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')[:-3]
  filepath = os.path.join(save_image_dir, time + '.png')
  plt.savefig(filepath, format="png", dpi=300)
  logger.log_info(f'graph: {filepath}')
  plt.close()
  return filepath
