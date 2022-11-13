import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(PROJECT_NAME)+len(PROJECT_NAME)]

_dt =  datetime.datetime.today()
_time = f'{_dt.year}-{_dt.month}-{_dt.day}-{_dt.hour}-{_dt.minute}-{_dt.second}'
WRITE_FILE_PATH = os.path.join(project_dir, 'log', _time + '.png')

def plotPersonPerTime(person_arr):
  t = np.arange(0, len(person_arr), 1)
  ft = np.array(person_arr)
  plt.plot(t, ft, 'b:')
  plt.savefig(WRITE_FILE_PATH, format="png", dpi=300)
