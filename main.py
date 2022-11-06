import sys
from src import constraint
from src import logger

_mode = ''

def _get_mode():
  global _mode
  if len(sys.argv) != 2:
    _mode = ''
  else:
    _mode = sys.argv[1]
_get_mode()

def _switch_process(mode):
  if(mode == constraint.MODE_DEMO):
    logger.log_info('demo process')
  elif(mode == constraint.MODE_PROD):
    logger.log_info('prod process')
  else:
    logger.log_error('mode wrong!')
  
def _run():
  global _mode
  _switch_process(_mode)

if __name__ == '__main__':
  _run()
