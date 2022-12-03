import sys
import json
import subprocess

import logger

def _decode_response(response):
  decoded_response = json.loads(response)
  logger.log_info(f'response result: {decoded_response}')
  return float(decoded_response['objective'])

def _request_score_list(solution_list, match_number, time_max, type_sum):
  score_list = []
  proc_list = []
  for solution in solution_list:
    if type_sum == 1:
      command = f'echo {solution} | opt submit --match={match_number}'
    else: 
      solution_per_type = []
      for i in range(type_sum):
        solution_per_type.append(solution[i*time_max : (i+1)*time_max-1])
      command = f'echo {solution_per_type} | opt submit --match={match_number}'
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    proc_list.append(proc)

  for proc in proc_list:
    try:
      response = proc.communicate()[0]
      score = _decode_response(response)
      score_list.append(score)
    except:
      logger.log_warn('submit fail! (or solution broken)')
      score_list.append(sys.maxsize)

  for proc in proc_list:
    proc.terminate()
  return score_list

def optimize(solution_list, match_number, time_max, type_sum):
  score_list = _request_score_list(solution_list, match_number, time_max, type_sum)
  return score_list

if __name__ == "__main__":
  import datetime
  dt_start =  datetime.datetime.today()
  print(f'[start]{dt_start.strftime("%Y-%m-%d %H:%M:%S")}')
  solution_list = [
    [6,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,12,12,12,12,13,13,13,14,14,14,15,15,15,16,16,16,17,17,17,18,18,18,19,19,19,20,20,20,21,21,21,22,22,22,23,23,23,24,24,24,25,25,25,26,26,26,26,27,27,27,28,28,28,28,29,29,29,29,29,30,30,30,30,30,31,31,31,31,31,31,31,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,31,31,31,31,31,31,31,30,30,30,30,30,29,29,29,29,28,28,28,28,27,27,27,27,26,26,26,25,25,25,24,24,24,24,23,23,23,22,22,22,21,21,21,20,20,19,19,19,18,18,18,17,17,17,16,16,16,15,15,15,15,14,14,14,13,13,13,12,12,12,11,11,11,11,10,10,10,10,9,9,9,8,8,8,8,8,7,7,7,7,6,6,6,6,6,5,5,5,5,5,5,4,4,4,4,4,4,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    * 5
  ]
