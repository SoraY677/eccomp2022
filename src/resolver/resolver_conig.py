'''

最適化手法のうちチューニングできる一部を
設定ファイルから値を受け取り管理

'''
#
# このファイル内で指定するコンフィグ
#
individual_num = 20 # 個体数

#
# 外部からの指定で変化するコンフィグ
#
time_max = 300
unit_minute_min = 0
unit_minute_max = 45
agent_sum = 4500
type_sum = 1

def set_config(
    config_map: map
  ) -> None:
  '''
  情報設定
  '''
  global_map = globals()
  for key in (
    'time_max',
    'unit_minute_min',
    'unit_minute_max',
    'agent_sum',
    'type_sum'
  ):
    global_map[key] = config_map[key]
