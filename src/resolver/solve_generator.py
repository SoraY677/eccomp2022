import genetic_algorithms

def generate_origin_agent(
      length,
      unit_second_min,
      unit_second_max,
      time_max
    ):
  '''
  各エージェントの出発時刻を生成

  Args:
    - length            決定変数の長さ
    - unit_second_min   各単位時間ごとの最少人数
    - unit_second_max   各単位時間ごとの最大人数
    - time_max          最大時間

  Returns:
    Array<Int>: 各エージェントの出発時刻の配列
  '''

  return genetic_algorithms.generate(
      length,
      unit_second_min,
      unit_second_max,
      time_max
      )

def generate_origin_agent_consider_type(
      length,
      unit_second_min,
      unit_second_max,
      type_guided_max,
      type_busy_max,
      type_slow_max
    ):
    '''
    各エージェントの性格を考慮した出発時刻を生成

    Args:
      - length            決定変数の長さ
      - unit_second_min   各単位時間ごとの最少人数
      - unit_second_max   各単位時間ごとの最大人数
      - type_guided_max,  エージェントタイプ:Guidedの総人数
      - type_busy_max,    エージェントタイプ:Busyの総人数
      - type_slow_max     エージェントタイプ:Slowの総人数
      - time_max          最大時間

    Returns:
      Array<Int>: 各エージェントの性格を考慮した出発時刻の配列
    '''
    return []


if __name__ == "__main__":
  generate_origin_agent(300, 0, 45, 299)
