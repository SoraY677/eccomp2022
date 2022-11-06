import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import logger

from genetic_algorithms import generate

count = 0

def generate_solve(
      length,
      unit_second_min,
      unit_second_max,
      type_guided_max,
      type_busy_max,
      type_slow_max,
      time_max
    ):
  sol = generate(length, unit_second_min, unit_second_max, time_max)
  return sol

__all__ = ['generate_solve']
