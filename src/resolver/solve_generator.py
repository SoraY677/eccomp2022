def generate_origin_agent(
      length,
      unit_second_min,
      unit_second_max
    ):
  '''
  各エージェントの出発時刻を生成

  Args:
    - length            決定変数の長さ
    - unit_second_min   各単位時間ごとの最少人数
    - unit_second_max   各単位時間ごとの最大人数

  Returns:
    Array<Int>: 各エージェントの出発時刻の配列
  '''

  return []

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
      - type_guided_max, # エージェントタイプ:Guidedの総人数
      - type_busy_max,   # エージェントタイプ:Busyの総人数
      - type_slow_max    # エージェントタイプ:Slowの総人数

    Returns:
      Array<Int>: 各エージェントの性格を考慮した出発時刻の配列
    '''
    return []


