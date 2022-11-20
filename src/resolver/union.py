import os
import sys

if __name__ == '__main__':
  sys.path.append(os.path.abspath('../..'))
else:
  current_dir = os.path.abspath(os.curdir)
  project_dir = current_dir[:current_dir.find("eccomp2022")+len("eccomp2022")]
  sys.path.append(os.path.join(project_dir, 'src'))
import logger

def union():
  logger.log_info('[select]')
