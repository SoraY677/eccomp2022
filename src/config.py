import os
import yaml

import logger

current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find("eccomp2022")+len("eccomp2022")]

_config = {}

def _read_config():
  global _config
  root_path = project_dir
  with open(os.path.join(root_path, 'config.yml')) as file:
    _config = yaml.safe_load(file)
    logger.log_info(f'config.yml: {_config}')
_read_config()

def get_config():
  global _config
  return _config

if __name__ == '__main__':
  print(get_config())
