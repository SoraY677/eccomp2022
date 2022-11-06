import os
import yaml
from util import root_path as rp

_config = {}

def _read_config():
  global _config
  root_path = rp.get_root_path()
  with open(os.path.join(root_path + 'config.yml')) as file:
    _config = yaml.safe_load(file)
_read_config()

def get_config():
  global _config
  return _config

if __name__ == '__main__':
  print(get_config())
