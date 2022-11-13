import os
import yaml

import logger

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(PROJECT_NAME)+len(PROJECT_NAME)]

_config = {}

def _read_config():
  global _config
  with open(os.path.join(project_dir, 'config.yml')) as file:
    _config = yaml.safe_load(file)
    logger.log_info(f'config.yml: {_config}')
_read_config()

def get_config():
  global _config
  return _config

if __name__ == '__main__':
  print(get_config())
