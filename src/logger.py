import os
import logging
import datetime
import shutil

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(PROJECT_NAME)+len(PROJECT_NAME)]

_logger = logging.getLogger()

def init(
    id: str,
    is_clear: bool
  ):
  global project_dir
  global _logger
  save_dir = os.path.join(project_dir, 'log', 'all', id)

  if is_clear:
    try:
      shutil.rmtree(save_dir)
    except:
      pass
  os.makedirs(save_dir, exist_ok=True)

  filepath = os.path.join(save_dir, datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S") + '.log')
  filehandler = logging.FileHandler(filepath, 'a')
  formatter = logging.Formatter('[%(levelname)s] %(asctime)-15s : %(message)s')
  filehandler.setFormatter(formatter)
  _logger.addHandler(filehandler)
  _logger.setLevel(logging.INFO)

  log_info(f'log file path: {filepath}')

def log_debug(message:str) -> None:
  global _logger
  _logger.debug(message)

def log_info(message:str) -> None:
  global _logger
  _logger.info(message)

def log_warn(message:str) -> None:
  global _logger
  _logger.warn(message)

def log_error(message:str) -> None:
  global _logger
  _logger.error(message)
  print(f'[error] {message}')
  exit(-1)
