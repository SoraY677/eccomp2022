import os
import sys

if __name__ == '__main__':
  sys.path.append(os.path.abspath('../..'))
else:
  from dotenv import load_dotenv
  load_dotenv()
  PROJECT_NAME = os.getenv('PROJECT_NAME')
  current_dir = os.path.abspath(os.curdir)
  project_dir = current_dir[:current_dir.find("{PROJECT_NAME}")+len("{PROJECT_NAME}")]
  sys.path.append(os.path.join(project_dir, 'src'))
import logger

def select():
  logger.log_info('[select]')
