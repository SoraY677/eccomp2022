import os
import logging
import datetime

from dotenv import load_dotenv
load_dotenv()
PROJECT_NAME = os.getenv('PROJECT_NAME')
current_dir = os.path.abspath(os.curdir)
project_dir = current_dir[:current_dir.find(PROJECT_NAME)+len(PROJECT_NAME)]

_dt =  datetime.datetime.today()
_time = f'{_dt.year}-{_dt.month}-{_dt.day}-{_dt.hour}-{_dt.minute}-{_dt.second}'
WRITE_FILE_PATH = os.path.join(project_dir, 'log', _time + '.log')

logging.basicConfig(filename=WRITE_FILE_PATH, level=logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s | %(message)s')
ch.setFormatter(formatter)

def log_debug(message):
  logging.debug(message)

def log_info(message):
  logging.info(message)

def log_warn(message):
  logging.warn(message)

def log_error(message):
  logging.error(message)
