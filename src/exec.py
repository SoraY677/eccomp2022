import resolver
import config

def run():
  config_map = config.get_config()['sop']['demo'][1]
  length = config_map['agent_sum']
  unit_second_min = config_map['unit_second_min']
  unit_second_max = config_map['unit_second_max']
  time_max = config_map['time_max']

  solution = resolver.first_generate(
    length,
    unit_second_min,
    unit_second_max,
    time_max
  )
  # solution2 = resolver.first_generate(
  #   length,
  #   unit_second_min,
  #   unit_second_max,
  #   time_max
  # )
  # resolver.cross(solution, solution2, 2, length, unit_second_min, unit_second_max)
  # resolver.select()
  resolver.mutate(length,
    unit_second_min,
    unit_second_max,
    time_max)
  # resolver.union(solution, solution2, length, unit_second_min, unit_second_max)
