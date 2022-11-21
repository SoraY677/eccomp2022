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
  '''
  設定読み込み
  '''
  global _config
  with open(os.path.join(project_dir, 'config.yml')) as file:
    _config = yaml.safe_load(file)
    logger.log_info(f'config.yml: {_config}')
_read_config()

def get_config():
  '''
  設定変数を返す

  Returns:
    Map: 設定変数
  '''
  global _config
  return _config
