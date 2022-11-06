import os
import logging
import datetime
from util import root_path as rp

_dt =  datetime.datetime.today()
_time = f'{_dt.year}-{_dt.month}-{_dt.day}-{_dt.hour}-{_dt.minute}-{_dt.second}'
WRITE_FILE_PATH = os.path.join(rp.get_root_path(), 'log', _time + '.log')

logging.basicConfig(filename=WRITE_FILE_PATH, level=logging.DEBUG)

def log_debug(message):
  logging.debug(message)

def log_info(message):
  logging.info(message)

def log_warn(message):
  logging.warn(message)

def log_error(message):
  logging.error(message)
