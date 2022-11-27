'''

最適化手法のうちチューニングできる一部を
設定ファイルから値を受け取り管理

'''
#
# コンフィグ変数一覧
#

# 外部から取得
time_max = 300
unit_minute_min = 0
unit_minute_max = 45
agent_sum = 4500
type_sum = 1
submit_max = 1000

individual_num = 20 # 個体数
evolve_max = None # 進化回数

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

  global_map['evolve_max'] = global_map['submit_max'] / global_map['individual_num']
