import resolver
import config
import logger
import constraint
import optimize_mock
import submit

def run(
    mode : str,
    optimize_mode: str,
    optimize_number: str,
    id: str,
    is_clear: bool
  ) -> None:
  '''
  実行
  '''
  config_map = config.get_config()[optimize_mode][mode][optimize_number]
  logger.log_info(f'setting data: {config_map}')
  resolver.set_config(config_map)

  is_practice = mode == constraint.MODE_PRACTICE
  if is_practice:
    optimize_mock.init(config_map['time_max'], config_map['unit_minute_min'], config_map['unit_minute_max'], config_map['agent_sum'], config_map['type_sum'])

  resolver.exec(config_map, id, is_clear, is_practice, submit.run)
