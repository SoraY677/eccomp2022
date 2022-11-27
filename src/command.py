import sys

import constraint

def _check_option_exist(
    option_list: list, #オプション一覧
    default: str #コマンドが存在しない場合のデフォルト返り血
  ):
  '''
  コマンドオプションが存在するか探索
  '''
  for item in option_list:
     if f'-{item}' in sys.argv:
      return item
  return default

def get_option() -> list:
  '''
  コマンドライン引数を取得
  '''
  # デフォルト
  mode = constraint.MODE_PRACTICE
  optimize_mode = constraint.OPTIMIZE_MODE_SINGLE
  optimize_number = constraint.OPTIMIZE_NUMBER_1

  mode = _check_option_exist([constraint.MODE_PRACTICE, constraint.MODE_DEMO, constraint.MODE_PROD], constraint.MODE_PRACTICE)
  optimize_mode = _check_option_exist([constraint.OPTIMIZE_MODE_SINGLE, constraint.OPTIMIZE_MODE_MULTI], constraint.OPTIMIZE_MODE_SINGLE)
  optimize_number = _check_option_exist([constraint.OPTIMIZE_NUMBER_1, constraint.OPTIMIZE_NUMBER_2], constraint.OPTIMIZE_NUMBER_1)

  # -clearコマンドがあったときはクリアモードをオン
  is_clear = not (_check_option_exist(["clear"], None) is None)

  return mode, optimize_mode, optimize_number, is_clear
