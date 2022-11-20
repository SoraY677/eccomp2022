import numpy as np
from scipy.interpolate import interp1d

def create(crossed_arr):
  '''
  近似した関数生成

  Args:
    - crossed_arr (ilst<int>)

  Returns:
      function : 近似関数
  '''
  t = np.arange(len(crossed_arr))
  x = np.array(crossed_arr)
  func = interp1d(t,x,kind='cubic')

  return func
