import resolver_config as conf

def get_select_list_per_type(
    select_list
  ):
  '''
  全タイプ合体した配列を各タイプごとに分離させる
  '''
  result = []
  for i in range(conf.type_sum):
    result.append(select_list[i*conf.time_max : (i+1)*conf.time_max])
  return result
