import os
import logging
from .util import root_path as rp

WRITE_FILE_PATH = os.path.join(rp.get_root_path(), 'app.log')

def set_log_write_file():
  logging.basicConfig(filename=WRITE_FILE_PATH)

def log_debug(message):
  logging.debug(message)

def log_info(message):
  logging.info(message)

def log_warn(message):
  logging.warn(message)

def log_error(message):
  logging.error(message)
