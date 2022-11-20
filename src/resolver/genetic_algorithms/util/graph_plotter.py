import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(PROJECT_NAME)+len(PROJECT_NAME)]


def plot_person_per_time(person_arr):
  t = np.arange(0, len(person_arr), 1)
  ft = np.array(person_arr)
  plt.plot(t, ft, linewidth=2.0)
  save_file(plt)

def plot_person_per_time_and_approximate_function(t, x, func):
  ax1 = plt.subplots(figsize=(17, 4))
  ax2 = ax1.twinx()
  ax1.bar(t, x, color='gray', alpha=0.5)
  ax2.plot(t, func(t), linewidth=3, alpha=0.5)
  plt.show()
  

def save_file(plt):
  dt =  datetime.datetime.today()
  time = f'{dt.year}-{dt.month}-{dt.day}-{dt.hour}-{dt.minute}-{dt.second}'
  filepath = os.path.join(project_dir, 'log', time + '.png')
  plt.savefig(filepath, format="png", dpi=300)
  return filepath
