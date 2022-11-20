import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate import first_generate, process_generate
from crossover import cross
from selecter import select
from mutation import mutate
from union import union



