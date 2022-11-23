import resolver
import config
import logger

def run(
    mode : str,
    optimize_mode: str,
    optimize_number: str
  ) -> None:
  '''
  実行
  '''
  
  config_map = config.get_config()[optimize_mode][mode][optimize_number]
  logger.log_info(f'{config_map}')
  
  time_max = config_map['time_max']
  unit_minute_min = ['unit_minute_min']
  unit_minute_max = ['unit_minute_max']
  agent_sum = config_map['agent_sum']

  if config_map['is_type_categorize']:
    categorized_exec(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum,
      config_map['type_guided_sum'],
      config_map['type_busy_sum'],
      config_map['type_slow_sum']
    )

  else:
    not_categorized_exec(
      time_max,
      unit_minute_min,
      unit_minute_max,
      agent_sum
    )


def categorized_exec(
      time_max:int,
      unit_minute_min:int,
      unit_minute_max:int,
      agent_sum:int,
      type_guided_sum:int,
      type_busy_sum:int,
      type_slow_sum:int,
    ) -> None:
  '''
  カテゴリ分けアリの実行
  '''

  pass

def not_categorized_exec(
      time_max: int,
      unit_minute_min: int,
      unit_minute_max: int,
      agent_sum: int
    ) -> None:
  '''
  カテゴリ分けナシの実行
  '''
  pass


