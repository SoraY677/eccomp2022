import resolver
import config

def run(
    mode,
    optimize_mode,
    optimize_number
  ):
  '''
  実行

  Args:
    - mode (String)
    - optimize_mode (String)
    - optimize_number (String)
  '''
  config_map = config.get_config()[mode][optimize_mode][optimize_number]
  try:
    time_max = config_map['time_max']
    unit_second_min = config_map['unit_second_min']
    unit_second_max = config_map['unit_second_max']
    agent_sum = config_map['agent_sum']
  except:
    pass

  